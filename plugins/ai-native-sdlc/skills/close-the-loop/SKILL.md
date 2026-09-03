---
name: close-the-loop
description: Diagnose a production signal — an alert, a breached control band, an incident, a failing pipeline, a support escalation — and write the finding back as a new intent.md so it re-enters the loop. Use whenever something has gone wrong in a running system, when the user pastes an alert, log or stack trace, when a metric has moved unexpectedly, or after an incident is resolved and the lesson needs recording. Diagnosis is yours; the fix goes through the same gates as any other change.
---

# Close the loop

Maintenance is where the loop restarts. A signal arrives, you diagnose
it, and what you find becomes the next `intent.md` rather than a message
that scrolls away.

## Steps

1. **Establish what actually happened** before proposing why. Pull the
   evidence: the metric and its baseline, the logs, the deployment
   window, the recent commits. Quote the evidence rather than
   summarising it.
2. **Separate the symptom from the cause.** Do not propose a fix until
   you can state the causal chain from change to symptom. If you cannot,
   say the cause is unknown and name what evidence would settle it.
3. **Act only through gated routes.** Read-only diagnosis is always
   allowed. Anything that changes state goes through a pull request into
   review, or a runbook that was approved in advance. Never both improvise
   and act.
4. **Size the finding:**
   - Fits in one PR → open it, targeting `develop`, with the
     evidence in the description.
   - Larger than one PR → write `intent/YYYY-MM-DD-slug.md` in the Stage 1
     format and start at Plan. Architectural weaknesses and patterns
     repeated across services always land here.
5. **Add the regression.** When the fix ships, add a case to the eval
   suite for this class of failure so the configuration is tested against
   it from now on.

## Writing the finding as intent

Use the same template as any other intent. The anomaly and its evidence
are the problem section; the proposed outcome is what "not happening
again" looks like; the affected systems come from the diagnosis.

Include what you ruled out and why. The next person to see this class of
incident should not repeat your dead ends.

## Triage is not yours

The service owner decides fix now, schedule, or dismiss. Dismissals are
useful — they tune the detection bands and cut noise. Record the
dismissal reason rather than deleting the finding.

## Escalate rather than guess

If the signal suggests active data loss, a security incident, or customer
harm, say so immediately and plainly at the top of your response. Do not
bury it under the diagnosis, and do not wait until you are confident.
