import argparse
import csv
import json
import re
from pathlib import Path


ORDER = {"PASS": 0, "WARN": 1, "BLOCK": 2}


def worst(*statuses):
    return max(statuses, key=lambda status: ORDER.get(status, 2))


def has_machine_witness(block):
    return any(w.get("machine_reviewable") is True for w in block.get("witnesses", []))


def base_gate(block, row_id=None):
    if row_id is not None and not re.match(r"^C2T-AUDIT-[0-9]{4}$", row_id):
        return "BLOCK"
    if block.get("contradictions"):
        return "BLOCK"
    if block.get("missing_fields"):
        return "BLOCK"
    if block.get("free_text_only_fields") or not has_machine_witness(block):
        return "WARN"
    return "PASS"


def gate_required_fields(payload):
    return base_gate(payload["required_joined_fields_presence"], payload.get("row_id"))


def gate_same_sample(payload):
    block = payload["same_sample_crosswalk"]
    if block.get("contradictions") or block.get("missing_fields"):
        return "BLOCK"
    record = block.get("sample_id_creation_record") or {}
    if record.get("created_before_label_access") is not True:
        return "BLOCK"
    if block.get("identity_basis") not in {"same_sample_id", "matched_structure_id"}:
        return "BLOCK"
    required_values = ["structure_id", "snapshot_id_or_window", "label_provenance_id"]
    if any(not block.get(value) for value in required_values):
        return "BLOCK"
    mismatch = block.get("cross_source_mismatch_screen", {})
    if any(value == "BLOCK" for value in mismatch.values()):
        return "BLOCK"
    if any(value == "WARN" for value in mismatch.values()) or block.get("free_text_only_fields"):
        return "WARN"
    return "PASS"


def gate_graph_lock(payload):
    block = payload["graph_convention_lock"]
    attack = block.get("attack_gap_protocol") or {}
    if block.get("contradictions") or block.get("missing_fields"):
        return "BLOCK"
    if block.get("protocol_predates_label_access") is not True:
        return "BLOCK"
    if block.get("laplacian_convention") != "L_sym":
        return "BLOCK"
    required_values = [
        "graph_convention_provenance_id",
        "graph_cutoff_rule",
        "rho_budget_normalization_rule",
        "same_graph_identity_record",
    ]
    if any(not block.get(value) for value in required_values):
        return "BLOCK"
    if attack.get("targeted_attack_defined") is not True:
        return "BLOCK"
    if attack.get("matched_random_control") is not True:
        return "BLOCK"
    if attack.get("removed_budget_accounting") is not True:
        return "BLOCK"
    if not attack.get("seed_policy"):
        return "BLOCK"
    if block.get("free_text_only_fields"):
        return "WARN"
    return "PASS"


def gate_external_label(payload):
    block = payload["external_label_independence"]
    if block.get("contradictions") or block.get("missing_fields"):
        return "BLOCK"
    if not block.get("label_provenance_id"):
        return "BLOCK"
    if not block.get("external_label_payload"):
        return "BLOCK"
    if block.get("is_external_to_graph_proxy") is not True:
        return "BLOCK"
    if block.get("synthetic_label_flag") is not False:
        return "BLOCK"
    if block.get("label_source_type") not in {"external_measurement", "external_literature_digitization"}:
        return "BLOCK"
    evidence = block.get("graph_proxy_exclusion_evidence") or []
    if not evidence:
        return "BLOCK"
    if not all(item.get("machine_reviewable") is True for item in evidence if isinstance(item, dict)):
        return "WARN"
    if block.get("free_text_only_fields"):
        return "WARN"
    return "PASS"


def gate_forbidden_control(payload):
    block = payload["forbidden_control_row_audit"]
    if block.get("contradictions"):
        return "BLOCK"
    subchecks = block.get("subchecks") or {}
    if not subchecks:
        return "BLOCK"
    statuses = []
    if block.get("missing_fields"):
        statuses.append("WARN")
    for subcheck in subchecks.values():
        status = subcheck.get("status")
        if status == "NOT_APPLICABLE_WITH_RATIONALE":
            if subcheck.get("rationale"):
                statuses.append("WARN")
                continue
            return "BLOCK"
        if status not in ORDER:
            return "BLOCK"
        if status == "PASS" and not subcheck.get("machine_reviewable_evidence_ids"):
            statuses.append("WARN")
        else:
            statuses.append(status)
    if not block.get("audit_timestamp_or_version"):
        statuses.append("WARN")
    if block.get("free_text_only_fields"):
        statuses.append("WARN")
    return worst(*statuses)


def gate_oi(payload):
    block = payload["OI_Srivastava_reproduction"]
    if block.get("applies_to_row") is False:
        return "NOT_APPLICABLE"
    if block.get("contradictions") or block.get("missing_fields"):
        return "BLOCK"
    required_values = [
        "exact_overlap_formula_or_code_ref",
        "normalization_rule_ref",
        "same_structure_mapping_ref",
    ]
    if any(not block.get(value) for value in required_values):
        return "BLOCK"
    if block.get("free_text_only_fields") or not has_machine_witness(block):
        return "WARN"
    return "PASS"


def decide(payload):
    statuses = {
        "required_joined_fields_presence": gate_required_fields(payload),
        "same_sample_crosswalk": gate_same_sample(payload),
        "graph_convention_lock": gate_graph_lock(payload),
        "external_label_independence": gate_external_label(payload),
        "forbidden_control_row_audit": gate_forbidden_control(payload),
        "OI_Srivastava_reproduction": gate_oi(payload),
    }
    required = [
        statuses["required_joined_fields_presence"],
        statuses["same_sample_crosswalk"],
        statuses["graph_convention_lock"],
        statuses["external_label_independence"],
        statuses["forbidden_control_row_audit"],
    ]
    optional = statuses["OI_Srivastava_reproduction"]
    row_decision = worst(*required)
    if optional != "NOT_APPLICABLE":
        row_decision = worst(row_decision, optional)
    material_allowed = (
        row_decision == "PASS"
        and payload.get("material_validation_claimed") is False
        and all(status == "PASS" for status in required)
        and optional in {"PASS", "NOT_APPLICABLE"}
    )
    statuses["row_decision"] = row_decision
    statuses["material_validation_allowed"] = str(material_allowed).lower()
    return statuses


def load_payloads(path):
    with Path(path).open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = []
    for payload in load_payloads(args.input):
        result = decide(payload)
        rows.append(
            {
                "row_id": payload["row_id"],
                "candidate_source": payload["candidate_source"],
                "required_joined_fields_presence_status": result["required_joined_fields_presence"],
                "same_sample_crosswalk_status": result["same_sample_crosswalk"],
                "graph_convention_lock_status": result["graph_convention_lock"],
                "external_label_independence_status": result["external_label_independence"],
                "forbidden_control_row_audit_status": result["forbidden_control_row_audit"],
                "OI_Srivastava_reproduction_status": result["OI_Srivastava_reproduction"],
                "row_decision": result["row_decision"],
                "material_validation_allowed": result["material_validation_allowed"],
            }
        )

    with Path(args.output).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
