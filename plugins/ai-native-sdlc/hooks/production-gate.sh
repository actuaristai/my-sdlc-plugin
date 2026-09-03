#!/usr/bin/env bash
# PreToolUse approval gate: the agent may act up to the production gate and
# cannot pass it. A block explains itself and names the route to approval.
set -uo pipefail

cmd=$(python3 -c 'import json,sys
try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)
print(payload.get("tool_input", {}).get("command", ""))')

[ -z "$cmd" ] && exit 0

if echo "$cmd" | grep -Eqi '(deploy|release|migrate|apply).*(prod|production)'; then
  if [ -z "${RELEASE_APPROVAL:-}" ]; then
    echo "Blocked: production actions need a named release authorisation." >&2
    echo "Route: ask the release manager to authorise, then re-run with RELEASE_APPROVAL set to the authorisation reference." >&2
    exit 2
  fi
  echo "Production action proceeding under authorisation ${RELEASE_APPROVAL}." >&2
fi
exit 0
