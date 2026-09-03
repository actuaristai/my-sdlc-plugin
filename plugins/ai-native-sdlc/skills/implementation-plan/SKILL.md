---
name: implementation-plan
description: Write and commit a plan.md before any code is generated, naming the files that change, the order of work, the risks and the tests that prove it. Use this at the start of every implementation session, whenever the user says "build it", "implement this", "let's code", hands you an accepted spec, or asks for a change of more than one file. Nothing gets implemented in this repository without an accepted plan — start in plan mode and iterate the plan before touching anything.
---

# Implementation plan

Start the session in plan mode. Claude cannot edit files until the
engineer accepts the plan, which is the point: design review happens
while changing course is still a matter of editing a document.

## Steps

1. **Read `spec.md` and the intent behind it.** Then read the code you
   are about to change. A plan written without reading the code is a
   guess.
2. **Produce a plan that names:**
   - every file that changes, with exact paths, marked (new) where
     applicable;
   - the order of work, in independently verifiable steps;
   - the risks — what this could break, and which step is riskiest;
   - the options you considered and rejected, with the reason;
   - the proof — the tests that demonstrate the change works.
3. **Invite interrogation.** Ask the engineer: what could this break,
   which step worries you, what did I not consider. Answer honestly,
   including where you are uncertain.
4. **Iterate to the handover test.** An engineer who has never seen this
   conversation should be able to implement the change from the plan
   alone. If they could not, keep going.
5. **Commit the approved plan** as `docs/sdlc/<slug>/plan.md` before
   implementing.
6. **Implement.** With a solid plan this is usually a single pass.
7. **Keep the plan honest.** When implementation departs from the plan,
   update `plan.md` in the same commit as the departure. The review stage
   checks the diff against this file, so a stale plan produces false
   findings.

## Splitting work

If the plan reveals independent streams that touch different files, say
so and name them. Each can run in its own git worktree as a separate
session. Tasks that share files run sequentially in one session — do not
parallelise work that collides.

## When to push back

Say so plainly if the spec cannot be implemented as written, if the
change is larger than the spec suggests, or if a cheaper approach exists
that the spec did not consider. Raising it at plan time costs a
conversation; raising it after implementation costs the implementation.
