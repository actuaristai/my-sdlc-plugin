---
name: verification-loop
description: Verify your own work with real command output before claiming anything is complete, fixed, working or passing. Use this every single time you are about to report a task done, hand back to the user, commit, or open a PR — and whenever you are fixing a bug, where the failing test must be written and committed first. Never claim success on the basis of having written code that looks correct.
---

# Verify before you claim

The session checks its own work and fixes its own mistakes before a human
sees them. A claim of "done" with no command output attached is not a
claim, it is a guess.

## The rule

Before reporting any task complete, run:

```
just test
just lint
```

Paste the output. If a test fails, fix the code, not the test.

## Fixing a bug

Order matters, and this order is not optional:

1. Reproduce the bug as a failing test.
2. Run it. Confirm it fails, and that it fails for the reason you expect
   — a test that fails for the wrong reason proves nothing.
3. Commit that test on its own.
4. Only now fix the code, without editing the test.

A hook blocks edits to test files during a fix. If it fires, that is the
control working — do not look for a way around it. A test that existed
before the fix, and that you could not rewrite, is the proof the bug is
gone.


## Making the target checkable

State the target so you can check it without asking:

- "all tests in `test_x` pass"
- "the endpoint returns 200 with the new field"
- "the screenshot matches the attached mock"

Vague targets ("it works now") cannot be verified, so they always come
back to the user for checking. That defeats the point.

## For visual work

Give yourself a way to see the result — a browser tool or screenshot
utility. Implement, screenshot, compare against the mock, adjust. Two or
three rounds is normal, and each round should be visibly better than the
last.

## What counts as evidence

The literal output of the command, not your summary of it. Truncate long
output at the interesting part, but do not paraphrase a pass.
