# my-sdlc-plugin

ai template

A Claude Code plugin marketplace implementing Anthropic's AI-native SDLC
playbook: the artifact chain, the stage gates, the verification loop and
the guardrails that keep governance running at agent speed.

## What it does

Every stage of the lifecycle ends by committing an artifact the next
stage reads. The chain of commits is the audit trail.

```
intent.md  →  spec.md  →  plan.md  →  diff + tests  →  PR + findings  →  production
    ↑                                                                        │
    └──────────────── a breached control band writes the next intent ────────┘
```

| Stage | Skill | Artifact | Who accepts it |
|---|---|---|---|
| 1 Plan | `capture-intent` | `intent/<date>-<slug>.md` | product owner |
| 2 Design | `write-spec` | `docs/sdlc/<slug>/spec.md` | product owner + policy owners |
| 3 Build | `implementation-plan` | `docs/sdlc/<slug>/plan.md`, then the diff | engineer |
| 4 Test | `verification-loop` | verification output | nobody — the session checks itself |
| 5 Deploy | `pr-review` | the PR and its findings | code owner |
| 6 Maintain | `close-the-loop` | a new intent | service owner |

`sdlc-loop` sits above all six as the dispatcher.

## Install

```powershell
just sdlc-check      # validate manifests and scripts
just sdlc-install    # register the marketplace and install locally
```

For everyone else, once this repository is pushed:

```bash
claude plugin marketplace add actuaristai/my-sdlc-plugin
claude plugin install ai-native-sdlc
```

The `marketplace add` argument is the GitHub `owner/repo` (it clones the
default branch). `ai-native-sdlc-marketplace` is the marketplace *name*
from the manifest — use it as the `@marketplace` suffix in
`claude plugin install ai-native-sdlc@ai-native-sdlc-marketplace` or in
`claude plugin marketplace remove`.

## Use it in a repository

```
/sdlc-init                                   # scaffold CLAUDE.md, REVIEW.md, intent/
/intent    customers keep phoning about claim status
/spec      intent/2026-09-01-claims-status.md
/plan      docs/sdlc/claims-status/spec.md
/review-sweep 412
/sdlc-measure --since 90.days
```

## What is a control and what is a suggestion

This distinction is the one to hold onto.

- **Skills are advisory.** They make the policy likely to be applied
  while the code is written. Nothing forces a session to comply.
- **Hooks are deterministic.** Anything that must hold without exception
  needs one behind the skill. The skill makes violations rare; the hook
  makes them close to impossible.

Shipped hooks:

| Hook | Fires on | Effect |
|---|---|---|
| `format-on-edit.sh` | after every edit | runs `just fmt` on the changed file |
| `protect-tests.sh` | before every edit | blocks test-file edits while `SDLC_FIX_TASK=1` |
| `production-gate.sh` | before every shell command | blocks production deploys without `RELEASE_APPROVAL` |

Agent PRs target `develop`. The agent may act up to the
production gate and cannot pass it.

## Measurement

The playbook names a leading and a lagging indicator for every play, and
most of them are already in git. `just sdlc-measure` reads out:

- time from intent commit to spec commit, per change;
- time from spec commit to plan commit;
- intent survival rate — the share of intents that reached a spec;
- specs reworked after planning started, which is requirements churn.

The stage whose elapsed time has not fallen is where the bottleneck now
sits.

## Source of truth

The repo is authoritative. Markdown artifacts hold the record; any other
system carries a link to the commit rather than a copy that drifts.

## Keeping it honest

When Claude makes the same mistake twice, the correction goes into
`CLAUDE.md`. When a policy changes, the skill changes and the policy
owner signs it off. When a production incident is fixed, it becomes an
eval. Anything else is documentation that will drift.

## Updating

This repository was generated from a Copier template. Pull template
changes with:

```bash
copier update
```
