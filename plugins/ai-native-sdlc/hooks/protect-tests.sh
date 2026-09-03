#!/usr/bin/env bash
# PreToolUse guardrail: an agent fixing code must not be able to weaken the
# check on that code. Blocks edits to test files while SDLC_FIX_TASK=1.
# Exit 2 blocks the action and sends the message back to Claude.
set -uo pipefail

file_path=$(python3 -c 'import json,sys
try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)
print(payload.get("tool_input", {}).get("file_path", ""))')

[ -z "$file_path" ] && exit 0
[ "${SDLC_FIX_TASK:-0}" = "1" ] || exit 0

case "$file_path" in
  *test_*|*_test.*|*/tests/*|*.test.*|*.spec.*|*testthat*)
    echo "Blocked: test files are frozen during a fix task." >&2
    echo "Write the failing test first, commit it, then fix the code without editing the test." >&2
    echo "If this test is genuinely wrong, unset SDLC_FIX_TASK and change it in its own commit." >&2
    exit 2
    ;;
esac
exit 0
