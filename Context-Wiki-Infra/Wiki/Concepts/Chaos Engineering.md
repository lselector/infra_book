---
type: Concept
title: "Chaos Engineering"
description: "Breaking your own system on purpose, during office hours - and the two-hour version a small team can actually run."
wikipedia: "https://en.wikipedia.org/wiki/Chaos_engineering"
tags: [ops-and-security, reliability, scaling]
timestamp: "2026-07-28T00:00:00Z"
---

# Chaos Engineering

Deliberately injecting failure into a system to find out
what actually happens, rather than trusting what the
architecture diagram implies. It is the experimental
counterpart to [[Failure Modes]]: every item on that list
is a hypothesis until you have caused it once.

## The method

1. **State the steady state** in a metric —
   "checkout completes in under 2s for 99% of requests."
2. **Form a hypothesis**: "if the recommendations service
   is down, checkout is unaffected."
3. **Inject the failure** in the smallest scope that can
   disprove it.
4. **Compare.** If the steady state held, you have
   evidence. If not, you have a bug found on a Tuesday
   afternoon rather than at 3am.
5. **Fix, then re-run the same experiment.** The re-run
   is the step people skip.

Always with a **blast radius** you have chosen in advance
and an abort button you have tested.

## Not for production first

The industry stories are about running this in
production. For a small product, that is the last step,
not the first. Staging finds most of it, and finding it
in staging costs nothing ([[Deployment Environments]]).

## The two-hour version, no tools required

You do not need a chaos platform. In a rung 5–9 stack
([[Stacks]]), block out an afternoon and do these by
hand:

| Experiment | What it tests |
|---|---|
| `sudo systemctl stop postgresql` | Do you return 503 or hang? Does the alert fire? |
| Fill the disk with a big file | Logs, uploads, and the database all die of this — usually first |
| `docker compose stop redis` | [[Cache Stampede]] — can the origin take it? |
| Add 2s latency to an outbound API (`tc netem`) | Timeouts and [[Cascading Failure]] |
| Kill a worker mid-job | [[Duplicate Processing]]: does the job run twice cleanly? |
| Post a malformed message | [[Poison Message]]: does the DLQ catch it? |
| Revoke an API key | Does it fail loudly, or silently stop sending email? |
| **Restore last night's backup to a scratch box** | The only test that matters ([[Database Backups]]) |
| Let a certificate expire in staging | [[Automatic HTTPS]] renewal actually working |

Most teams that try this find the same three things: an
unbounded timeout, an alert that never fires, and a
backup that has never been restored.

## The related practice: game days

Same idea, aimed at people rather than code. Someone
plays the incident, everyone else responds using only the
runbook. It tests whether the on-call person can find the
dashboard, has the credentials, and knows who to call —
which is the part of [[Incident Response]] that fails at
3am.

## Watch out for

**Do not start here.** Chaos engineering on a system with
no [[Monitoring and Alerting]] just breaks things: you
cannot observe the steady state, so the experiment has no
result. Metrics first, then experiments.

## Related

[[Failure Modes]] · [[Incident Response]] ·
[[Monitoring and Alerting]] ·
[[Service Level Objectives]] · [[Database Backups]] ·
[[Deployment Environments]] · [[Automated Testing]] ·
[[Cascading Failure]] · [[Cache Stampede]] ·
[[Single Point of Failure]]

## Sources

- [[sre-book-index]] · [[sre-book-monitoring]] ·
  [[aws-well-architected-reliability]] ·
  [[nist-incident-handling-guide]]
