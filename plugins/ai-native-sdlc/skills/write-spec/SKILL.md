---
name: write-spec
description: Produce a requirements-and-design spec from an accepted intent.md, applying this organisation's policy skills and flagging every concern the policies cannot cleanly satisfy. Use whenever an intent has been accepted, when the user says "spec this out", "how would we build this", "design this", or hands you an intent file. Requirements and design happen in one session here — do not split them, and do not begin implementation planning until the spec is accepted.
---

# Write the spec

Requirements and design collapse into one session. Policy is applied
while the spec is written, not discovered in a review weeks later.

## Steps

1. **Read the intent.** Everything you write traces back to it. If the
   intent is missing or vague, stop and use `capture-intent` instead.
2. **Load the policy skills.** Whatever this repository has for security,
   data handling, brand and UX. Name them in the spec so the reader knows
   what constrained the design.
3. **Read the codebase before designing.** The spec must be
   implementable *here*, not in the abstract. Name real files and real
   interfaces.
4. **Write requirements as numbered, independently testable statements.**
   If a requirement cannot be tested, it is a preference — say so and
   move it.
5. **Flag every concern.** This is the highest-value part of the
   artifact. Flag anything where:
   - two policies contradict each other;
   - the intent asks for something the constraints forbid;
   - the design needs a decision you are not entitled to make;
   - a dependency is outside this repository's control.

   Each concern names the policy owner it should go to. Do not resolve a
   policy conflict by picking one — that is the product owner's call.
6. **Carry forward the open questions** from the intent. Answered ones
   get their answer; unanswered ones stay visible.
7. **Write `docs/sdlc/<slug>/spec.md`** using
   `docs/sdlc/spec-template.md`. Commit it alongside the intent.

## The review that follows

The product owner reviews the spec but does not write it. They check that
it solves the stated problem and that the flagged concerns are resolved
with their policy owners before engineering sees it.

Anything the organisation classes as higher risk goes to a technical lead
as well. A human makes that call. Accepting the spec is what starts the
planning stage.

## Failure mode to avoid

A spec with no flagged concerns is usually a spec that did not look hard
enough. If you genuinely found none, say that explicitly and name the
policies you checked against — an empty section reads as an oversight.
