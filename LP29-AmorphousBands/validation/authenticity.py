"""Proof-object authenticity precondition for O_s admission.

This module checks whether a proof object carries enough source, structure,
pair, arithmetic, execution, and comparison metadata to be converted into the
predicate-state payload consumed by validation.validate.
"""

from __future__ import annotations

import math
import re
from typing import Any, Callable


Predicate = Callable[[dict[str, Any]], bool]

HEX_RE = re.compile(r"^[0-9a-fA-F]+$")


def _get(obj: dict[str, Any], path: str) -> Any:
    current: Any = obj
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _stable_identifier(obj: dict[str, Any]) -> bool:
    value = _get(obj, "source.paper_id")
    return _nonempty_string(value) and (
        value.startswith("10.") or value.startswith("doi:") or value.startswith("arXiv:")
    )


def _exact_locator(obj: dict[str, Any]) -> bool:
    value = _get(obj, "source.exact_locator")
    if not _nonempty_string(value):
        return False
    lowered = value.lower()
    return any(token in lowered for token in ("page", "table", "figure", "fig.", "row"))


def _reported_scalar(obj: dict[str, Any]) -> bool:
    value = _get(obj, "source.reported_scalar")
    return (
        isinstance(value, dict)
        and _number(value.get("scalar"))
        and (_nonempty_string(value.get("units")) or value.get("dimensionless") is True)
    )


def _structure_identifier(obj: dict[str, Any]) -> bool:
    return _nonempty_string(_get(obj, "structure.identifier"))


def _canonical_structure(obj: dict[str, Any]) -> bool:
    value = _get(obj, "structure.canonical_representation")
    return isinstance(value, dict) and all(key in value for key in ("coordinates", "cell", "species"))


def _structure_hash(obj: dict[str, Any]) -> bool:
    value = _get(obj, "structure.hash")
    if not isinstance(value, dict):
        return False
    algorithm = value.get("algorithm")
    digest = value.get("hash")
    if algorithm not in {"sha256", "sha512", "blake2b"}:
        return False
    return _nonempty_string(digest) and bool(HEX_RE.fullmatch(digest))


def _mapping_rule(obj: dict[str, Any]) -> bool:
    value = _get(obj, "structure.same_structure_mapping_rule")
    return isinstance(value, dict) and all(
        key in value for key in ("atom_ordering", "coordinate_tolerance", "species_mapping")
    )


def _channel_definition(obj: dict[str, Any]) -> bool:
    value = _get(obj, "pairs.channel_definition")
    channels = value.get("channels") if isinstance(value, dict) else None
    return isinstance(channels, list) and bool(channels) and all(
        isinstance(item, dict) and _nonempty_string(item.get("species")) and _nonempty_string(item.get("orbital"))
        for item in channels
    )


def _cutoff_rule(obj: dict[str, Any]) -> bool:
    value = _get(obj, "pairs.cutoff_rule")
    return isinstance(value, dict) and _nonempty_string(value.get("neighbor_rule")) and (
        _number(value.get("cutoff")) or _nonempty_string(value.get("algorithm"))
    )


def _pair_convention(obj: dict[str, Any]) -> bool:
    return _get(obj, "pairs.convention") in {"ordered", "unordered", "directed_weighted"}


def _pair_list_or_hash(obj: dict[str, Any]) -> bool:
    value = _get(obj, "pairs.pair_list_or_hash")
    if not isinstance(value, dict):
        return False
    pair_list = value.get("pair_list")
    digest = value.get("hash")
    return (isinstance(pair_list, list) and bool(pair_list)) or (_nonempty_string(digest) and bool(HEX_RE.fullmatch(digest)))


def _n_pair(obj: dict[str, Any]) -> bool:
    value = _get(obj, "pairs.N_pair")
    if not isinstance(value, int) or value <= 0:
        return False
    pair_data = _get(obj, "pairs.pair_list_or_hash")
    if isinstance(pair_data, dict) and isinstance(pair_data.get("pair_list"), list):
        return len(pair_data["pair_list"]) == value
    return True


def _raw_sum(obj: dict[str, Any]) -> bool:
    return _number(_get(obj, "arithmetic.raw_overlap_sum"))


def _normalization_formula(obj: dict[str, Any]) -> bool:
    value = _get(obj, "arithmetic.normalization_formula")
    return _nonempty_string(value) and "raw_overlap_sum" in value and "N_pair" in value


def _normalization_code(obj: dict[str, Any]) -> bool:
    return _nonempty_string(_get(obj, "arithmetic.normalization_code_or_commit"))


def _basis_source(obj: dict[str, Any]) -> bool:
    value = _get(obj, "execution.basis_set_or_orbital_source")
    return isinstance(value, dict) and _nonempty_string(value.get("source")) and bool(value.get("method_settings"))


def _software(obj: dict[str, Any]) -> bool:
    value = _get(obj, "execution.software")
    return isinstance(value, dict) and _nonempty_string(value.get("name")) and _nonempty_string(value.get("version"))


def _runtime(obj: dict[str, Any]) -> bool:
    value = _get(obj, "execution.runtime_environment")
    return isinstance(value, dict) and any(
        _nonempty_string(value.get(key))
        for key in ("container_digest", "environment_lockfile", "os_compiler_library_manifest")
    )


def _trace(obj: dict[str, Any]) -> bool:
    value = _get(obj, "execution.executor_trace_or_workflow_graph")
    return isinstance(value, dict) and all(key in value for key in ("inputs", "outputs", "code"))


def _precision_tolerance(obj: dict[str, Any]) -> bool:
    value = _get(obj, "execution.floating_point_precision_and_tolerance")
    return isinstance(value, dict) and value.get("precision") in {"float32", "float64", "extended", "decimal"} and (
        _number(value.get("abs_tol")) or _number(value.get("rel_tol"))
    )


def _recomputed_value(obj: dict[str, Any]) -> bool:
    return _number(_get(obj, "verification.recomputed_value"))


def _acceptance_tolerance(obj: dict[str, Any]) -> bool:
    value = _get(obj, "verification.acceptance_tolerance")
    if not isinstance(value, dict) or value.get("rule_predeclared") is not True:
        return False
    abs_tol = value.get("abs_tol")
    rel_tol = value.get("rel_tol")
    if not (_number(abs_tol) or _number(rel_tol)):
        return False

    reported = _get(obj, "source.reported_scalar.scalar")
    recomputed = _get(obj, "verification.recomputed_value")
    verdict = _get(obj, "verification.comparison.verdict")
    if not (_number(reported) and _number(recomputed)) or verdict not in {"match", "mismatch"}:
        return True

    tolerance = float(abs_tol) if _number(abs_tol) else abs(float(reported)) * float(rel_tol)
    within = abs(float(recomputed) - float(reported)) <= tolerance
    return within if verdict == "match" else not within


FIELD_CHECKS: list[tuple[str, str, Predicate]] = [
    ("F01", "source.paper_id", _stable_identifier),
    ("F02", "source.exact_locator", _exact_locator),
    ("F03", "source.reported_scalar", _reported_scalar),
    ("F04", "structure.identifier", _structure_identifier),
    ("F05", "structure.canonical_representation", _canonical_structure),
    ("F06", "structure.hash", _structure_hash),
    ("F07", "structure.same_structure_mapping_rule", _mapping_rule),
    ("F08", "pairs.channel_definition", _channel_definition),
    ("F09", "pairs.cutoff_rule", _cutoff_rule),
    ("F10", "pairs.convention", _pair_convention),
    ("F11", "pairs.pair_list_or_hash", _pair_list_or_hash),
    ("F12", "pairs.N_pair", _n_pair),
    ("F13", "arithmetic.raw_overlap_sum", _raw_sum),
    ("F14", "arithmetic.normalization_formula", _normalization_formula),
    ("F15", "arithmetic.normalization_code_or_commit", _normalization_code),
    ("F16", "execution.basis_set_or_orbital_source", _basis_source),
    ("F17", "execution.software", _software),
    ("F18", "execution.runtime_environment", _runtime),
    ("F19", "execution.executor_trace_or_workflow_graph", _trace),
    ("F20", "execution.floating_point_precision_and_tolerance", _precision_tolerance),
    ("F21", "verification.recomputed_value", _recomputed_value),
    ("F22", "verification.acceptance_tolerance", _acceptance_tolerance),
]


def validate_authenticity(proof_object: dict[str, Any]) -> dict[str, Any]:
    predicate_results: dict[str, bool] = {}
    missing_fields: list[str] = []
    invalid_fields: list[str] = []
    first_failed: str | None = None

    for field_id, path, check in FIELD_CHECKS:
        raw_value = _get(proof_object, path)
        if raw_value is None:
            predicate_results[field_id] = False
            missing_fields.append(field_id)
            if first_failed is None:
                first_failed = field_id
            continue

        passed = bool(check(proof_object))
        predicate_results[field_id] = passed
        if not passed:
            invalid_fields.append(field_id)
            if first_failed is None:
                first_failed = field_id

    passed_all = all(predicate_results.values())
    return {
        "authenticity_status": "PASS" if passed_all else "BLOCK",
        "predicate_results": predicate_results,
        "diagnostics": [] if passed_all else ["PROOF_OBJECT_AUTHENTICITY_BLOCKED"],
        "missing_fields": missing_fields,
        "invalid_fields": invalid_fields,
        "first_failed_predicate": first_failed or "NONE",
    }


def payload_from_proof_object(
    proof_object: dict[str, Any],
    *,
    payload_id: str,
    target_mode: str,
) -> dict[str, Any]:
    authenticity = validate_authenticity(proof_object)
    return {
        "payload_id": payload_id,
        "target_mode": target_mode,
        "witness": {
            "predicates": authenticity["predicate_results"],
            "first_failed_predicate_hint": authenticity["first_failed_predicate"],
            "comparison": proof_object.get("verification", {}).get("comparison", {"verdict": "not_run"}),
            "replay_complete": authenticity["authenticity_status"] == "PASS",
            "authenticity_status": authenticity["authenticity_status"],
        },
    }
