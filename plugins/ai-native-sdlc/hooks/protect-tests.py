#!/usr/bin/env python3
"""PreToolUse guardrail: an agent fixing code must not be able to weaken the
check on that code. Blocks edits to test files while SDLC_FIX_TASK=1.
Exit 2 blocks the action and sends the message back to Claude.

Ported from protect-tests.sh so the guardrail runs on Windows too, where
a POSIX shell is not guaranteed. Invoked by hooks.json via python3/python/py.
"""

import json
import os
import sys

# Same set as the shell glob patterns: *test_* *_test.* */tests/* *.test.*
# *.spec.* *testthat*. Backslashes are normalised to "/" first so Windows
# paths match the */tests/* case.
TEST_MARKERS = ("test_", "_test.", "/tests/", ".test.", ".spec.", "testthat")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not file_path:
        return 0
    if os.environ.get("SDLC_FIX_TASK", "0") != "1":
        return 0

    normalised = file_path.replace("\\", "/")
    if any(marker in normalised for marker in TEST_MARKERS):
        print("Blocked: test files are frozen during a fix task.", file=sys.stderr)
        print(
            "Write the failing test first, commit it, then fix the code without editing the test.",
            file=sys.stderr,
        )
        print(
            "If this test is genuinely wrong, unset SDLC_FIX_TASK and change it in its own commit.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
