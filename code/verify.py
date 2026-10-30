"""Run the repository's finite scientific checks and navigation check."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import re
import sys
from urllib.parse import unquote

import numpy as np

from core_checks import run_checks as run_core_checks
from fidelity_checks import run_checks as run_fidelity_checks

ROOT = Path(__file__).resolve().parents[1]


def navigation_check():
    checked = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text()
        text = re.sub(r"(?ms)^```.*?^```[^\n]*", "", text)
        text = re.sub(r"(?s)\$\$.*?\$\$", "", text)
        text = re.sub(r"(?s)(?<!\\)\$(?!\$).*?(?<!\\)\$", "", text)
        text = re.sub(r"`[^`]*`", "", text)
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                raise AssertionError(f"Broken or escaping relative link in {path.relative_to(ROOT)}: {target}")
            checked += 1
    return {"status": "pass", "relative_file_links_checked": checked,
            "scope": "Relative file destinations; hosted anchor rendering is reviewed separately."}


def input_hashes():
    paths = list((ROOT / "code").glob("*.py"))
    paths += list(ROOT.rglob("*.md"))
    paths += [ROOT / "requirements.txt"]
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(paths) if ".git" not in path.parts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "verification.json")
    args = parser.parse_args()
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "core": run_core_checks(),
        "fidelity": run_fidelity_checks(),
        "input_sha256": input_hashes(),
        "scope": "Finite formula, instrument and score checks. Analytical proofs establish the asymptotic claims.",
        "status": "numerical_checks_passed_navigation_pending",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    report["navigation"] = navigation_check()
    report["status"] = "pass"
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": report["status"], "output": str(args.output),
        "max_mean_standard_errors": report["core"]["max_mean_standard_errors"],
        "max_adaptive_probability_error": report["core"]["maximum_adaptive_probability_error"],
        "max_interleaved_kl_error": report["core"]["maximum_interleaved_kl_error"],
        "fidelity_passed": report["fidelity"]["passed"],
        "navigation": report["navigation"],
    }, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1) from error
