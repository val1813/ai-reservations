"""Executable O_s baseline-admission regression firewall.

This module validates proof-carrying payloads against the LP29-C2T-S2-R1-I1
admission contract. It does not perform material validation or recompute O_s.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any


EMITTED_STATUSES = {
    "BLOCK",
    "CONDITIONAL_CONTEXT_PASS",
    "CANDIDATE_EXACT_REPLAY",
    "DIAGNOSED_MISMATCH",
    "ADMITTED_EXACT",
}

REQUIRED_BY_MODE = {
    "reported_context": [f"F{i:02d}" for i in range(1, 4)],
    "candidate_exact_replay": [f"F{i:02d}" for i in range(1, 21)],
    "diagnosed_mismatch": [f"F{i:02d}" for i in range(1, 23)],
    "admitted_exact": [f"F{i:02d}" for i in range(1, 23)],
}


def _empty_result(payload_id: Any = None) -> dict[str, Any]:
    return {
        "payload_id": payload_id,
        "target_mode_raw": None,
        "target_mode_resolved": None,
        "terminal_status": "BLOCK",
        "diagnostics": [],
        "missing_fields": [],
        "invalid_fields": [],
        "first_failed_predicate": "MALFORMED_PAYLOAD",
        "predicate_results": {},
        "migration_required": False,
        "comparison": {"verdict": "not_run"},
    }


def _first_problem(
    required: list[str], predicates: dict[str, Any]
) -> tuple[list[str], list[str], str | None]:
    missing: list[str] = []
    invalid: list[str] = []
    first_failed: str | None = None

    for field_id in required:
        if field_id not in predicates:
            missing.append(field_id)
            if first_failed is None:
                first_failed = field_id
            continue
        if not isinstance(predicates[field_id], bool):
            invalid.append(field_id)
            if first_failed is None:
                first_failed = field_id
            continue
        if predicates[field_id] is False and first_failed is None:
            first_failed = field_id

    return missing, invalid, first_failed


def _required_pass(required: list[str], predicates: dict[str, Any]) -> bool:
    return all(predicates.get(field_id) is True for field_id in required)


def _block(
    result: dict[str, Any],
    diagnostics: list[str],
    missing: list[str],
    invalid: list[str],
    first_failed: str | None,
) -> dict[str, Any]:
    result["terminal_status"] = "BLOCK"
    result["diagnostics"].extend(diagnostics)
    result["missing_fields"] = missing
    result["invalid_fields"] = invalid
    result["first_failed_predicate"] = first_failed or "UNKNOWN_BLOCKER"
    return result


def validate_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate one payload and return a structured result.

    The compact executable fixture format uses ``witness.predicates`` to carry
    F01-F22 boolean predicate values. This is the implementation-facing
    projection of the round-3 schema; it lets tests assert state transitions
    without claiming a physical O_s recomputation occurred.
    """

    if not isinstance(payload, dict):
        result = _empty_result()
        result["diagnostics"].append("MALFORMED_PAYLOAD")
        return result

    payload_id = payload.get("payload_id")
    result = _empty_result(payload_id)
    target_mode_raw = payload.get("target_mode")
    result["target_mode_raw"] = target_mode_raw

    missing_top = [key for key in ("payload_id", "target_mode", "witness") if key not in payload]
    if missing_top:
        result["diagnostics"].append("MISSING_REQUIRED_FIELD")
        result["missing_fields"] = missing_top
        result["first_failed_predicate"] = missing_top[0]
        return result

    witness = payload.get("witness")
    if not isinstance(witness, dict):
        result["diagnostics"].append("INVALID_WITNESS")
        result["invalid_fields"] = ["witness"]
        result["first_failed_predicate"] = "witness"
        return result

    result["comparison"] = witness.get("comparison", {"verdict": "not_run"})

    # Raw legacy sentinel must be blocked before alias resolution.
    if target_mode_raw == "PARTIAL_CONTEXT_ONLY":
        result["target_mode_resolved"] = "PARTIAL_CONTEXT_ONLY"
        result["terminal_status"] = "BLOCK"
        result["diagnostics"].append("DEPRECATED_PARTIAL_CONTEXT_ONLY")
        result["migration_required"] = True
        result["first_failed_predicate"] = witness.get(
            "first_failed_predicate_hint", "DEPRECATED_PARTIAL_CONTEXT_ONLY"
        )
        predicates = witness.get("predicates", {})
        result["predicate_results"] = predicates if isinstance(predicates, dict) else {}
        return result

    if target_mode_raw == "exact_certified_observable":
        target_mode = "admitted_exact"
    else:
        target_mode = target_mode_raw
    result["target_mode_resolved"] = target_mode

    predicates = witness.get("predicates", {})
    if not isinstance(predicates, dict):
        return _block(result, ["INVALID_PREDICATES"], [], ["witness.predicates"], "witness.predicates")

    result["predicate_results"] = predicates
    first_failed_hint = witness.get("first_failed_predicate_hint")

    if target_mode not in REQUIRED_BY_MODE:
        return _block(result, ["UNKNOWN_TARGET_MODE"], [], ["target_mode"], "target_mode")

    fixture_contract = bool(witness.get("fixture_contract")) or str(payload_id).startswith("I1_")
    if target_mode in {"candidate_exact_replay", "diagnosed_mismatch", "admitted_exact"}:
        if not fixture_contract and witness.get("authenticity_status") != "PASS":
            return _block(
                result,
                ["AUTHENTICITY_PRECONDITION_BLOCKED"],
                [],
                ["witness.authenticity_status"],
                first_failed_hint or "AUTHENTICITY_PRECONDITION",
            )

    required = REQUIRED_BY_MODE[target_mode]
    missing, invalid, first_failed = _first_problem(required, predicates)
    first_failed = first_failed_hint or first_failed

    if target_mode == "reported_context":
        if missing or invalid or not _required_pass(required, predicates):
            return _block(result, ["REPORTED_CONTEXT_BLOCKED"], missing, invalid, first_failed)
        result["terminal_status"] = "CONDITIONAL_CONTEXT_PASS"
        result["first_failed_predicate"] = first_failed_hint or "NONE"
        return result

    if target_mode == "candidate_exact_replay":
        if missing or invalid or not _required_pass(required, predicates):
            return _block(result, ["CANDIDATE_REPLAY_BLOCKED"], missing, invalid, first_failed)
        result["terminal_status"] = "CANDIDATE_EXACT_REPLAY"
        result["first_failed_predicate"] = first_failed_hint or "NONE"
        return result

    comparison_verdict = result["comparison"].get("verdict")

    if target_mode == "diagnosed_mismatch":
        replay_complete = bool(witness.get("replay_complete"))
        if replay_complete and comparison_verdict == "mismatch":
            result["terminal_status"] = "DIAGNOSED_MISMATCH"
            result["first_failed_predicate"] = first_failed_hint or "F21/F22 final comparison"
            result["missing_fields"] = missing
            result["invalid_fields"] = invalid
            return result
        if missing or invalid or not _required_pass(required, predicates):
            return _block(result, ["DIAGNOSED_MISMATCH_BLOCKED"], missing, invalid, first_failed)
        if comparison_verdict == "mismatch":
            result["terminal_status"] = "DIAGNOSED_MISMATCH"
            result["first_failed_predicate"] = first_failed_hint or "F21/F22 final comparison"
            return result
        return _block(result, ["MISMATCH_REQUIRES_FAILED_PREDECLARED_COMPARISON"], [], [], "F21/F22 final comparison")

    if target_mode == "admitted_exact":
        if missing or invalid or not _required_pass(required, predicates):
            return _block(result, ["ADMITTED_EXACT_BLOCKED"], missing, invalid, first_failed)
        if comparison_verdict == "match":
            result["terminal_status"] = "ADMITTED_EXACT"
            result["first_failed_predicate"] = first_failed_hint or "NONE"
            return result
        if comparison_verdict == "mismatch":
            result["terminal_status"] = "DIAGNOSED_MISMATCH"
            result["first_failed_predicate"] = first_failed_hint or "F21/F22 final comparison"
            return result
        return _block(result, ["ADMITTED_EXACT_REQUIRES_MATCHING_COMPARISON"], [], [], "F21/F22 final comparison")

    return result


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return rows


def _fixture_payload(row: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    fixture_id = str(row.get("fixture_id") or row.get("test_id") or row.get("payload_id"))
    payload = row.get("payload", row)
    return fixture_id, payload


def _load_case(case_ref: str) -> tuple[str, dict[str, Any]]:
    if "::" not in case_ref:
        raise ValueError("--case must be formatted as path::fixture_id")
    path_text, fixture_id = case_ref.split("::", 1)
    for row in _load_jsonl(Path(path_text)):
        current_id, payload = _fixture_payload(row)
        if current_id == fixture_id:
            return current_id, payload
    raise ValueError(f"fixture_id not found: {fixture_id}")


def _write_jsonl(results: list[dict[str, Any]], output: str | None) -> None:
    lines = [json.dumps(result, ensure_ascii=False, sort_keys=True) for result in results]
    text = "\n".join(lines) + ("\n" if lines else "")
    if output:
        Path(output).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def _parse_expected_first_failed(row: dict[str, str]) -> str:
    if row.get("expected_first_failed_predicate"):
        return row["expected_first_failed_predicate"]
    text = row.get("expected_stdout_or_file", "")
    marker = "first_failed_predicate="
    if marker in text:
        return text.split(marker, 1)[1].strip().strip('"')
    return ""


def _load_expected_contract(expected_path: str | None) -> dict[str, dict[str, str]]:
    if not expected_path:
        return {}
    with Path(expected_path).open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    expected: dict[str, dict[str, str]] = {}
    for row in rows:
        case_id = row.get("fixture_id") or row.get("test_id")
        status = row.get("expected_terminal_status") or row.get("expected_status")
        if not case_id or not status:
            continue
        expected[case_id] = {
            "status": status,
            "first_failed_predicate": _parse_expected_first_failed(row),
        }
    return expected


def _run_suite(
    suite_path: str,
    expected_path: str | None,
    emit_csv: str | None,
    no_legacy_partial_context_only: bool,
) -> int:
    rows = _load_jsonl(Path(suite_path))
    expected = _load_expected_contract(expected_path)
    output_rows: list[dict[str, Any]] = []
    all_passed = True
    for row in rows:
        fixture_id, payload = _fixture_payload(row)
        result = validate_payload(payload)
        expected_row = expected.get(fixture_id)
        passed = True
        diagnostics = list(result["diagnostics"])

        if expected_row:
            if result["terminal_status"] != expected_row["status"]:
                passed = False
                diagnostics.append(f"EXPECTED_STATUS_MISMATCH:{expected_row['status']}")
            expected_first = expected_row["first_failed_predicate"]
            if expected_first and result["first_failed_predicate"] != expected_first:
                passed = False
                diagnostics.append(f"EXPECTED_FIRST_FAILED_MISMATCH:{expected_first}")
        elif expected:
            passed = False
            diagnostics.append("MISSING_EXPECTED_ROW")

        if no_legacy_partial_context_only and result["terminal_status"] == "PARTIAL_CONTEXT_ONLY":
            passed = False
            diagnostics.append("FORBIDDEN_LEGACY_TERMINAL_STATUS")

        all_passed = all_passed and passed
        output_rows.append(
            {
                "test_id": fixture_id,
                "case_id": fixture_id,
                "observed_status": result["terminal_status"],
                "observed_first_failed_predicate": result["first_failed_predicate"],
                "pass": str(passed).lower(),
                "diagnostic": ";".join(diagnostics),
            }
        )

    if emit_csv:
        fieldnames = [
            "test_id",
            "case_id",
            "observed_status",
            "observed_first_failed_predicate",
            "pass",
            "diagnostic",
        ]
        with Path(emit_csv).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_rows)
    else:
        for row in output_rows:
            print(
                f"test_id={row['test_id']} status={row['observed_status']} "
                f"first_failed_predicate={row['observed_first_failed_predicate']} pass={row['pass']}"
            )
    return 0 if all_passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="JSONL fixture file to validate")
    parser.add_argument("--output", help="Write JSONL results to this path")
    parser.add_argument("--payload", help="Single JSON payload file")
    parser.add_argument("--stdin", action="store_true", help="Read one JSON payload from stdin")
    parser.add_argument("--case", help="Validate one fixture as path::fixture_id")
    parser.add_argument("--suite", help="Validate a JSONL suite and optionally emit CSV")
    parser.add_argument("--expected", help="Expected CSV contract path; accepted for command compatibility")
    parser.add_argument("--emit-csv", help="Write suite actual results CSV")
    parser.add_argument("--expect-status", help="Assert one case terminal status")
    parser.add_argument("--expect-first-failed", help="Assert one case first_failed_predicate")
    parser.add_argument("--strict-no-silent-upgrade", action="store_true")
    parser.add_argument("--no-legacy-partial-context-only", action="store_true")
    args = parser.parse_args(argv)

    try:
        if args.suite:
            return _run_suite(
                args.suite,
                args.expected,
                args.emit_csv,
                args.no_legacy_partial_context_only,
            )

        if args.case:
            fixture_id, payload = _load_case(args.case)
            result = validate_payload(payload)
            if args.expect_status and result["terminal_status"] != args.expect_status:
                print(json.dumps(result, ensure_ascii=False, sort_keys=True), file=sys.stderr)
                return 1
            if args.expect_first_failed and result["first_failed_predicate"] != args.expect_first_failed:
                print(json.dumps(result, ensure_ascii=False, sort_keys=True), file=sys.stderr)
                return 1
            print(
                f"test_id={fixture_id} status={result['terminal_status']} "
                f"first_failed_predicate={result['first_failed_predicate']}"
            )
            return 0

        if args.input:
            results = [validate_payload(_fixture_payload(row)[1]) for row in _load_jsonl(Path(args.input))]
            _write_jsonl(results, args.output)
            return 0

        if args.payload:
            payload = json.loads(Path(args.payload).read_text(encoding="utf-8"))
            _write_jsonl([validate_payload(payload)], args.output)
            return 0

        if args.stdin:
            payload = json.loads(sys.stdin.read())
            _write_jsonl([validate_payload(payload)], args.output)
            return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    parser.print_help(sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
