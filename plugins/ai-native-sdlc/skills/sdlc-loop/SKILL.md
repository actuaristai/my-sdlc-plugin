---
name: sdlc-loop
description: The artifact chain and stage gates for this repository's AI-native SDLC. Use this whenever work is starting, moving between stages, or you are unsure which artifact to write next — including when the user says "start a change", "what stage are we at", "write this up", asks where a decision should be recorded, or hands you a ticket, incident or half-formed idea. Read this before capturing intent, writing a spec, planning an implementation, or closing the loop after an incident.
---

# The SDLC loop

Work in my-sdlc-plugin moves through six stages. Each stage ends by
committing an artifact, and the next stage begins by reading it. The
chain of commits is the audit trail: who asked for what, what the agent
produced, and who approved it.

Do not skip forward. If the artifact the current stage needs does not
exist, go back and write it.

## The chain

| Stage | Reads | Writes | Human gate |
|---|---|---|---|
| 1 Plan | a problem, a ticket, an alert | `intent/<date>-<slug>.md` | product owner accepts |
| 2 Design | `intent.md` | `docs/sdlc/<slug>/spec.md` | product owner accepts, concerns routed |
| 3 Build | `spec.md` | `docs/sdlc/<slug>/plan.md`, then the diff | engineer accepts the plan |
| 4 Test | the diff | tests, verification output | none — the session checks itself |
| 5 Deploy | the diff, `spec.md`, `plan.md` | the PR and its findings | code owner approves |
| 6 Maintain | production signals | a new `intent.md` | service owner triages |

Stage 6 writes Stage 1. That is what makes it a loop.

## Which skill to load

- Starting from an idea, ticket or incident → `capture-intent`
- An `intent.md` has been accepted → `write-spec`
- A `spec.md` has been accepted → `implementation-plan`
- About to claim work is done → `verification-loop`
- Reviewing or answering review on a PR → `pr-review`
- A production signal needs diagnosing → `close-the-loop`

## Source of truth

The repo is authoritative. Markdown artifacts hold the record. Any
external system carries a link to the commit, not a copy that drifts.

## What never changes

Humans stay accountable for every decision that requires judgment. Your
job is to prepare the decision, not to make it. Specifically:

- You do not accept your own artifacts.
- You do not approve your own code.
- You do not pass the production gate.

If a gate is blocking you, say so and name the approval route. Do not
route around it.
