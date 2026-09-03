---
name: capture-intent
description: Turn a half-formed idea, ticket, complaint or incident into a committed intent.md that the design stage can act on. Use this whenever someone describes a problem, a frustration, something they wish the system did, or hands over a ticket or alert — even if they did not ask for a document. Also use when the user says "I have an idea", "we should build", "can we make it so that", or when a monitoring signal needs writing up. Do not start designing or coding until an intent exists and has been accepted.
---

# Capture intent

The originator describes a problem in their own words. You turn it into a
version-controlled artifact without stripping out what they meant.

You are not writing a ticket. You are writing the thing that makes a
ticket unnecessary.

## Steps

1. **Listen first.** Let the originator describe what they cannot do
   today, who is affected, and what better would look like. No formal
   language required. Do not correct their vocabulary.
2. **Brainstorm until the idea is concrete.** Ask what an analyst would
   ask: scope, users, constraints, what success looks like, what is
   explicitly out of scope. Ask one question at a time. Stop when the
   answers stop changing the shape of the problem.
3. **Separate problem from solution.** Originators usually arrive with a
   solution. Ask what problem it solves and write that down as the
   problem. Keep their proposed solution in the outcome section, marked
   as their suggestion.
4. **Write the file** using `intent/TEMPLATE.md`, named
   `intent/YYYY-MM-DD-short-slug.md`.
5. **Read it back.** Ask the originator to correct anything you
   misunderstood. Their correction is the point of this step — do not
   skip it because the draft looks good.
6. **Commit** to `intent/`. Author and timestamp join the record.

## What a good intent looks like

- The problem is stated as an observation, not a feature request.
- Someone who was not in the conversation can tell who is affected.
- Constraints are hard limits, not preferences.
- Open questions are genuinely open — do not invent answers to look
  complete.

## What to refuse

Do not write an intent for work that is already specified elsewhere, and
do not merge several unrelated problems into one file. One problem, one
intent. If the originator has three problems, write three files and say
so.

## Handover

An accepted intent starts the design pass. Do not write the spec in the
same breath — acceptance by the product owner is a real gate, and the
artifact has to survive it before anything downstream is worth doing.
