#!/usr/bin/env bash
# PostToolUse guardrail: format the file that just changed, so drift never
# accumulates into a review finding. Scoped to the changed file and kept
# fast — heavier checks belong at the commit or the PR.
set -uo pipefail

read_field() {
  python3 -c 'import json,sys
try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)
print(payload.get("tool_input", {}).get(sys.argv[1], ""))' "$1"
}

file_path=$(read_field file_path)
[ -z "$file_path" ] && exit 0
[ -f "$file_path" ] || exit 0

just fmt "$file_path" >/dev/null 2>&1
exit 0
