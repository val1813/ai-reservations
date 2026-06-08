from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

from validation.validate import validate_payload


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_FILES = [
    ROOT / "validation" / "fixtures" / "a_expected_cases.jsonl",
    ROOT / "validation" / "fixtures" / "legacy_partial_context.jsonl",
]
EXPECTED = ROOT / "validation" / "fixtures" / "expected_results.csv"


def _read_jsonl(path: Path) -> dict[str, dict]:
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rows[row["fixture_id"]] = row["payload"]
    return rows


def _load_payloads() -> dict[str, dict]:
    payloads = {}
    for path in FIXTURE_FILES:
        payloads.update(_read_jsonl(path))
    return payloads


def _load_expected() -> list[dict[str, str]]:
    with EXPECTED.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _split_semicolon(value: str) -> list[str]:
    return [part for part in value.split(";") if part]


def test_expected_manifest_has_fixture_for_every_row() -> None:
    payloads = _load_payloads()
    expected_ids = {row["fixture_id"] for row in _load_expected()}
    assert expected_ids == set(payloads)


def test_validate_payload_expected_results() -> None:
    payloads = _load_payloads()
    for expected in _load_expected():
        fixture_id = expected["fixture_id"]
        result = validate_payload(payloads[fixture_id])

        assert result["terminal_status"] == expected["expected_terminal_status"], fixture_id
        assert result["terminal_status"] != "PARTIAL_CONTEXT_ONLY", fixture_id
        assert result["first_failed_predicate"] == expected["expected_first_failed_predicate"], fixture_id
        assert result["migration_required"] is (expected["expected_migration_required"].lower() == "true")

        expected_diagnostic = expected["expected_diagnostic"]
        if expected_diagnostic:
            assert expected_diagnostic in result["diagnostics"], fixture_id

        expected_missing = _split_semicolon(expected["expected_missing_fields"])
        if expected_missing:
            assert result["missing_fields"] == expected_missing, fixture_id

        expected_invalid = _split_semicolon(expected["expected_invalid_fields"])
        if expected_invalid:
            assert result["invalid_fields"] == expected_invalid, fixture_id

        for forbidden in _split_semicolon(expected["forbidden_terminal_statuses"]):
            assert result["terminal_status"] != forbidden, fixture_id


def test_cli_single_case_contract() -> None:
    case_ref = "current/B/fixtures/I1_authoritative_cases_round3.jsonl::I1_FULL_EXACT_MATCH"
    completed = subprocess.run(
        [
            sys.executable,
            "validation/validate.py",
            "--case",
            case_ref,
            "--expect-status",
            "ADMITTED_EXACT",
            "--expect-first-failed",
            "NONE",
            "--strict-no-silent-upgrade",
            "--no-legacy-partial-context-only",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "test_id=I1_FULL_EXACT_MATCH status=ADMITTED_EXACT first_failed_predicate=NONE" in completed.stdout


def test_cli_suite_emits_actual_results_csv(tmp_path: Path) -> None:
    output_csv = tmp_path / "actual.csv"
    subprocess.run(
        [
            sys.executable,
            "validation/validate.py",
            "--suite",
            "current/B/fixtures/I1_authoritative_cases_round3.jsonl",
            "--expected",
            "current/B/artifacts/I1_regression_command_contract_round3.csv",
            "--emit-csv",
            str(output_csv),
            "--strict-no-silent-upgrade",
            "--no-legacy-partial-context-only",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    with output_csv.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 17
    assert {row["pass"] for row in rows} == {"true"}
    distribution = {}
    for row in rows:
        distribution[row["observed_status"]] = distribution.get(row["observed_status"], 0) + 1
    assert distribution == {
        "BLOCK": 8,
        "CONDITIONAL_CONTEXT_PASS": 2,
        "CANDIDATE_EXACT_REPLAY": 1,
        "ADMITTED_EXACT": 1,
        "DIAGNOSED_MISMATCH": 5,
    }


def test_cli_suite_fails_wrong_expected_contract(tmp_path: Path) -> None:
    wrong_expected = tmp_path / "wrong_expected.csv"
    source = ROOT / "current" / "B" / "artifacts" / "I1_regression_command_contract_round3.csv"
    rows = list(csv.DictReader(source.open("r", encoding="utf-8", newline="")))
    rows[0]["expected_status"] = "ADMITTED_EXACT"
    with wrong_expected.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    output_csv = tmp_path / "actual.csv"
    completed = subprocess.run(
        [
            sys.executable,
            "validation/validate.py",
            "--suite",
            "current/B/fixtures/I1_authoritative_cases_round3.jsonl",
            "--expected",
            str(wrong_expected),
            "--emit-csv",
            str(output_csv),
            "--strict-no-silent-upgrade",
            "--no-legacy-partial-context-only",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert completed.returncode == 1
    rows = list(csv.DictReader(output_csv.open("r", encoding="utf-8", newline="")))
    assert rows[0]["pass"] == "false"
    assert "EXPECTED_STATUS_MISMATCH:ADMITTED_EXACT" in rows[0]["diagnostic"]
