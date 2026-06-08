from __future__ import annotations

import copy
import json
from pathlib import Path

from validation.authenticity import payload_from_proof_object, validate_authenticity
from validation.validate import validate_payload


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "validation" / "fixtures" / "authenticity_cases.jsonl"


def _load_rows() -> list[dict]:
    return [json.loads(line) for line in CASES.read_text(encoding="utf-8").splitlines() if line.strip()]


def _set_path(obj: dict, path: str, value) -> None:
    current = obj
    parts = path.split(".")
    for part in parts[:-1]:
        current = current[part]
    current[parts[-1]] = value


def _remove_path(obj: dict, path: str) -> None:
    current = obj
    parts = path.split(".")
    for part in parts[:-1]:
        current = current[part]
    current.pop(parts[-1], None)


def _proof_for(row: dict, valid_proof: dict) -> dict:
    proof = copy.deepcopy(row.get("proof_object", valid_proof))
    if "set_path" in row:
        _set_path(proof, row["set_path"], row["set_value"])
    if "remove_path" in row:
        _remove_path(proof, row["remove_path"])
    return proof


def test_authenticity_cases() -> None:
    rows = _load_rows()
    valid_proof = rows[0]["proof_object"]
    for row in rows:
        proof = _proof_for(row, valid_proof)
        result = validate_authenticity(proof)
        assert result["authenticity_status"] == row["expected_authenticity_status"], row["fixture_id"]
        assert result["first_failed_predicate"] == row["expected_first_failed_predicate"], row["fixture_id"]


def test_valid_authenticity_can_enter_terminal_validator() -> None:
    valid_proof = _load_rows()[0]["proof_object"]
    payload = payload_from_proof_object(
        valid_proof,
        payload_id="AUTH_VALID_FULL_PROOF",
        target_mode="admitted_exact",
    )
    result = validate_payload(payload)
    assert result["terminal_status"] == "ADMITTED_EXACT"
    assert result["first_failed_predicate"] == "NONE"


def test_failed_authenticity_blocks_before_terminal_admission() -> None:
    rows = _load_rows()
    valid_proof = rows[0]["proof_object"]
    bad_row = next(row for row in rows if row["fixture_id"] == "AUTH_MISSING_LOCATOR")
    bad_proof = _proof_for(bad_row, valid_proof)
    authenticity = validate_authenticity(bad_proof)
    assert authenticity["authenticity_status"] == "BLOCK"

    payload = payload_from_proof_object(
        bad_proof,
        payload_id="AUTH_MISSING_LOCATOR",
        target_mode="admitted_exact",
    )
    result = validate_payload(payload)
    assert result["terminal_status"] == "BLOCK"
    assert result["first_failed_predicate"] == "F02"


def test_direct_forged_payload_without_authenticity_cannot_admit_exact() -> None:
    forged = {
        "payload_id": "FORGED_ALL_TRUE",
        "target_mode": "admitted_exact",
        "witness": {
            "predicates": {f"F{i:02d}": True for i in range(1, 23)},
            "comparison": {"verdict": "match"},
        },
    }
    result = validate_payload(forged)
    assert result["terminal_status"] == "BLOCK"
    assert result["first_failed_predicate"] == "AUTHENTICITY_PRECONDITION"


def test_direct_forged_payload_with_blocked_authenticity_cannot_admit_exact() -> None:
    forged = {
        "payload_id": "FORGED_AUTH_BLOCK",
        "target_mode": "admitted_exact",
        "witness": {
            "predicates": {f"F{i:02d}": True for i in range(1, 23)},
            "authenticity_status": "BLOCK",
            "comparison": {"verdict": "match"},
        },
    }
    result = validate_payload(forged)
    assert result["terminal_status"] == "BLOCK"
    assert result["first_failed_predicate"] == "AUTHENTICITY_PRECONDITION"


def test_self_contradictory_match_fails_authenticity() -> None:
    valid_proof = _load_rows()[0]["proof_object"]
    bad_proof = copy.deepcopy(valid_proof)
    bad_proof["verification"]["recomputed_value"] = 999.0
    bad_proof["verification"]["comparison"]["verdict"] = "match"
    result = validate_authenticity(bad_proof)
    assert result["authenticity_status"] == "BLOCK"
    assert result["first_failed_predicate"] == "F22"
