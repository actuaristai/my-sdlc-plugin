---
description: Sweep unresolved review comments and failing checks on a PR
---

Use the `pr-review` skill on PR $ARGUMENTS.

Work through every unresolved review comment and every failing check.
For each one: address it, push the fix, and reply on the thread saying
what you changed. Where you disagree with a finding, say so with your
reasoning instead of complying.

Stop when the PR is green and waiting only on code owner approval. Do not
approve it and do not merge it — report back instead.
