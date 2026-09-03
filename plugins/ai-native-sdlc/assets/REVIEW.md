# Review instructions

Applies to every pull request in my-sdlc-plugin. Findings do not
approve or block on their own — branch protection still requires a code
owner's approval. This file tells the reviewer what to look for and how
loud to be about it.

## Passes

Run three passes and tag each finding with its pass.

- **Bugs** — logic errors, broken edge cases, subtle regressions, wrong
  handling of nulls and empty inputs.
- **Security** — injection risks, authentication gaps, secrets in the
  diff, personally identifiable information in logs or error messages.
- **Compliance** — the change matches `spec.md` and `plan.md` for this
  change, and follows the conventions in `CLAUDE.md`.

## What Important means here

Reserve Important for findings that would break behaviour, leak data or
breach a policy. Style and naming are nits.

## Cap the nits

Report at most five nits per review. Summarise the rest as a count.

## Do not report

- Anything matching `**/generated/**`.
- Anything `just lint` already enforces.

## Feeding findings back

When a review flags the same mistake for the second time, add the
correction to `CLAUDE.md` as part of that review. Because review reads
`CLAUDE.md`, the mistake is caught from the next PR onwards. Also flag
when a change has made `CLAUDE.md` outdated.

## Tuning

Monthly, the tech lead rates findings and adjusts the nit cap and the
exclusions above. Rising nit volume means the cap is too high; rising
Important findings after merge means the passes are too narrow.
