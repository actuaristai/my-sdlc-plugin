#!/usr/bin/env python3
"""PostToolUse guardrail: format the file that just changed, so drift never
accumulates into a review finding. Scoped to the changed file and kept
fast - heavier checks belong at the commit or the PR.

Ported from format-on-edit.sh so the guardrail runs on Windows too, where
a POSIX shell is not guaranteed. Invoked by hooks.json via python3/python/py.
"""

import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not file_path or not Path(file_path).is_file():
        return 0

    try:
        subprocess.run(
            ["just", "fmt", file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        # `just` not installed on this machine - formatting is best-effort.
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
