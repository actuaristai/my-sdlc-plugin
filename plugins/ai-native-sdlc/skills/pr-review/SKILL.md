---
name: pr-review
description: Review a pull request against REVIEW.md, or address review comments on a PR you opened. Use whenever you are asked to review a diff, look over a change, check a branch, sweep unresolved comments, or when tagged on a PR thread. Also use before opening a PR, to self-check the diff against spec.md and plan.md. Findings are advisory — you never approve a PR, and you never merge one.
---

# PR review

Review runs in both directions here. You review incoming changes against
policy, and you address comments on changes you authored.

## Reviewing

Read `REVIEW.md` first — it defines the passes, what counts as Important
versus a nit, and what to skip. Then:

1. **Read `spec.md` and `plan.md` for this change** before reading the
   diff. Most valuable findings come from the gap between what was
   planned and what was built, and you cannot see that gap without both.
2. **Run the three passes** — bugs, security, compliance — and tag each
   finding with its pass and severity.
3. **Respect the nit cap.** Report at most the cap in `REVIEW.md` and
   summarise the rest as a count. A review of forty nits gets ignored
   wholesale, which is worse than a review of five.
4. **Justify each Important finding** with the concrete consequence:
   what breaks, what leaks, which policy is breached. "This is not best
   practice" is a nit.
5. **Say what you could not check.** Coverage you did not have is a
   finding in itself.

## Answering review

When tagged on a comment, address it and push the fix. The thread records
both the request and the change — do not resolve a comment silently.

If you disagree with a finding, say so with reasoning rather than
complying. A reviewer who is wrong wants to know.

## Feeding back

When a finding repeats a mistake that has now come up twice, add the
correction to `CLAUDE.md` as part of this review. Review reads
`CLAUDE.md`, so the mistake is caught from the next PR onwards. Also flag
when the change has made `CLAUDE.md` outdated.

## The line you do not cross

Separation of duties is the whole point: the agent that wrote the code
has no route to approve it. Branch protection requires a code owner. Do
not approve, do not merge, do not push to `develop` directly,
and do not suggest disabling a check to get a PR through.
