#!/usr/bin/env python3
"""PreToolUse approval gate: the agent may act up to the production gate and
cannot pass it. A block explains itself and names the route to approval.

Ported from production-gate.sh so the gate runs on Windows too, where a
POSIX shell (and grep) is not guaranteed. Invoked by hooks.json via
python3/python/py.
"""

import json
import os
import re
import sys

# Equivalent to: grep -Eqi '(deploy|release|migrate|apply).*(prod|production)'
PROD_ACTION = re.compile(
    r"(deploy|release|migrate|apply).*(prod|production)", re.IGNORECASE
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    command = payload.get("tool_input", {}).get("command", "")
    if not command:
        return 0

    if PROD_ACTION.search(command):
        approval = os.environ.get("RELEASE_APPROVAL", "")
        if not approval:
            print(
                "Blocked: production actions need a named release authorisation.",
                file=sys.stderr,
            )
            print(
                "Route: ask the release manager to authorise, then re-run with "
                "RELEASE_APPROVAL set to the authorisation reference.",
                file=sys.stderr,
            )
            return 2
        print(
            f"Production action proceeding under authorisation {approval}.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
