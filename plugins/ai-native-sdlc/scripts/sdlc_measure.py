"""Report the AI-native SDLC indicators from git history.

Every play in the playbook names a leading and a lagging indicator, and
almost all of them are already sitting in git. This reads them out.

Usage:
    python sdlc_measure.py [--since 90.days] [--json]
"""

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

ARTIFACT_PATTERNS = {
    "intent": re.compile(r"^intent/(?!README|TEMPLATE)(.+)\.md$"),
    "spec": re.compile(r"^docs/sdlc/(.+)/spec\.md$"),
    "plan": re.compile(r"^docs/sdlc/(.+)/plan\.md$"),
}


def run_git(args):
    """Return stdout of a git command, or an empty string on failure."""
    result = subprocess.run(
        ["git"] + args, capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def read_artifact_history(since):
    """Map each change slug to the first commit time of each artifact."""
    log = run_git(
        ["log", "--since", since, "--reverse", "--name-only",
         "--pretty=format:@@%H|%ct"]
    )
    history = {}
    timestamp = None
    for line in log.splitlines():
        if line.startswith("@@"):
            timestamp = int(line.split("|")[1])
            continue
        if not line.strip() or timestamp is None:
            continue
        for kind, pattern in ARTIFACT_PATTERNS.items():
            match = pattern.match(line.strip())
            if not match:
                continue
            slug = normalise_slug(match.group(1))
            entry = history.setdefault(slug, {})
            entry.setdefault(kind, timestamp)
    return history


def normalise_slug(raw):
    """Strip the ISO date prefix so intent and spec paths line up."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", raw).strip("/")


def measure_stage_gaps(history):
    """Elapsed hours between consecutive artifacts, per change."""
    gaps = {"intent_to_spec": [], "spec_to_plan": []}
    for entry in history.values():
        if "intent" in entry and "spec" in entry:
            gaps["intent_to_spec"].append(
                (entry["spec"] - entry["intent"]) / 3600
            )
        if "spec" in entry and "plan" in entry:
            gaps["spec_to_plan"].append((entry["plan"] - entry["spec"]) / 3600)
    return gaps


def measure_survival(history):
    """Share of intents that reached a spec — the survival rate."""
    intents = [e for e in history.values() if "intent" in e]
    if not intents:
        return None
    survived = [e for e in intents if "spec" in e]
    return len(survived) / len(intents)


def measure_rework(since):
    """Count spec commits dated after the first plan commit for a change."""
    log = run_git(
        ["log", "--since", since, "--name-only", "--pretty=format:@@%ct"]
    )
    first_plan = {}
    late_specs = 0
    timestamp = None
    entries = []
    for line in log.splitlines():
        if line.startswith("@@"):
            timestamp = int(line[2:])
            continue
        stripped = line.strip()
        if not stripped or timestamp is None:
            continue
        entries.append((timestamp, stripped))
    for timestamp, path in sorted(entries):
        plan_match = ARTIFACT_PATTERNS["plan"].match(path)
        if plan_match:
            slug = normalise_slug(plan_match.group(1))
            first_plan.setdefault(slug, timestamp)
        spec_match = ARTIFACT_PATTERNS["spec"].match(path)
        if spec_match:
            slug = normalise_slug(spec_match.group(1))
            if slug in first_plan and timestamp > first_plan[slug]:
                late_specs += 1
    return late_specs


def summarise(values):
    """Return count, median and mean for a list of hours."""
    if not values:
        return None
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    return {
        "n": len(ordered),
        "median_hours": round(median, 1),
        "mean_hours": round(sum(ordered) / len(ordered), 1),
    }


def build_report(since):
    """Assemble every indicator into one dictionary."""
    history = read_artifact_history(since)
    gaps = measure_stage_gaps(history)
    return {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "since": since,
        "changes_seen": len(history),
        "intent_to_spec": summarise(gaps["intent_to_spec"]),
        "spec_to_plan": summarise(gaps["spec_to_plan"]),
        "intent_survival_rate": measure_survival(history),
        "specs_reworked_after_plan": measure_rework(since),
    }


def print_report(report):
    """Print the report in a form a human can scan."""
    print(f"SDLC indicators (since {report['since']})")
    print(f"  changes with artifacts: {report['changes_seen']}")
    for stage in ("intent_to_spec", "spec_to_plan"):
        stats = report[stage]
        if stats is None:
            print(f"  {stage}: no completed pairs yet")
            continue
        print(
            f"  {stage}: median {stats['median_hours']}h "
            f"(n={stats['n']}, mean {stats['mean_hours']}h)"
        )
    survival = report["intent_survival_rate"]
    if survival is None:
        print("  intent survival rate: no intents yet")
    else:
        print(f"  intent survival rate: {survival:.0%}")
    print(f"  specs reworked after plan: {report['specs_reworked_after_plan']}")
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", default="90.days")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not Path(".git").exists():
        raise SystemExit("Run this from the root of a git repository.")

    report = build_report(args.since)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    return None


if __name__ == "__main__":
    main()
