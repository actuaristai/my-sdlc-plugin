---
description: Report the playbook's leading and lagging indicators from git history
---

Run `python ${CLAUDE_PLUGIN_ROOT}/scripts/sdlc_measure.py $ARGUMENTS` and
interpret the output.

For each indicator, say whether it is moving in the right direction and
what would most likely be causing it. Where a number looks wrong, check
the underlying git history before explaining it — a broken measurement is
more common than a dramatic change.

Flag any stage where the elapsed time has not fallen. That stage is where
the bottleneck now sits.
