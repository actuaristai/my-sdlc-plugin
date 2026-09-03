# my-sdlc-plugin

ai template

Keep this file under a page. Claude reads all of it at the start of every
session, so anything stale costs context for no benefit. Conditional or
task-specific knowledge belongs in a skill, which only loads when it
triggers.

## Commands

- Test: `just test` (all green; never skip or delete a failing test)
- Lint: `just lint` (zero warnings)
- Format: `just fmt`

## Verifying your work

Run the test and lint commands before reporting any task complete, and
paste the output. If a test fails, fix the code, not the test.

## Conventions

<!-- Replace with what is actually true here. Examples: -->
- Naming is `snake_case` for variables, functions and file names.
- Function names are verbs; variable names are nouns.
- Imports go at the top of the file, grouped standard / third party / local.

## Architecture

<!-- Where things live, and what talks to what. Two or three lines. -->

## SDLC artifacts

This repository follows the AI-native SDLC loop. Every stage commits an
artifact the next stage reads:

| Stage | Artifact | Location |
|---|---|---|
| Plan | `intent.md` | `intent/` |
| Design | `spec.md` | `docs/sdlc/<change>/spec.md` |
| Build | `plan.md` | `docs/sdlc/<change>/plan.md` |
| Build/Test | the diff and its tests | the branch |
| Deploy | review findings | the PR |
| Maintain | incident record | `intent/` as a new intent |

The repo is the source of truth. Markdown artifacts are the authoritative
record; any other system holds a link to the commit.

Agent PRs target `develop`. The agent has no route to push to
the default branch directly.

## Things Claude gets wrong

<!-- Working rule: when Claude makes the same mistake twice, the
     correction goes here. -->
- Do not edit anything matching `**/generated/**`.
- Do not edit test files while fixing a bug. Write the failing test first,
  commit it, then make it pass.

