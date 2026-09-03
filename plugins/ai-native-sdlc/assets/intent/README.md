# Intent

One markdown file per idea, incident or request. This is where the loop
starts and where it restarts.

Anyone can add one — the originator does not need to be an engineer, and
does not need to use git directly. A connector to GitHub lets Claude
commit the file on their behalf from claude.ai or Cowork.

## Naming

`YYYY-MM-DD-short-slug.md`, lowercase, hyphenated. ISO dates only. Never
`final`, never `v2` — that is what git history is for.

## Lifecycle

1. Originator brainstorms with Claude until the idea is concrete.
2. Claude writes the file using `TEMPLATE.md`.
3. Originator corrects anything Claude misunderstood.
4. Commit. Author and timestamp join the record.
5. The product owner accepts or closes it. Acceptance starts the design
   pass and produces `docs/sdlc/<slug>/spec.md`.

The accept or reject decision is recorded as the merge or the closing
review. That is the evidence — do not keep it in a chat thread.
