---
type: Concept
title: "Rate Limiting"
description: "Capping how much one caller can ask for - the algorithms, where to enforce them, and why AI endpoints need three limits, not one."
wikipedia: "https://en.wikipedia.org/wiki/Rate_limiting"
tags: [ai-in-saas, ops-and-security, reliability]
timestamp: "2026-07-28T00:00:00Z"
---

# Rate Limiting

A cap on how much one caller may consume in a window.
It protects capacity from a stampede, protects the bill
from abuse, and protects every other tenant from the one
having a bad day.

Every endpoint that costs real money per call needs one.
An AI endpoint costs real money per call.

## The algorithms

| Algorithm | How | Trade-off |
|---|---|---|
| Fixed window | count per minute, reset on the minute | trivial; allows a 2x burst across the boundary |
| Sliding window | count over the trailing N seconds | smooth, slightly more state |
| Token bucket | refill R per second, capacity B | allows bursts, then throttles — the usual choice |
| Concurrency cap | at most N in flight per caller | the right shape for long streaming calls |

For a chat panel you want a token bucket **and** a
concurrency cap: the bucket stops a hundred questions a
minute, the cap stops one user holding twenty
simultaneous generations open.

## Where to enforce it

**At the edge, for cheap volumetric protection.** A
[[Content Delivery Network|CDN]] or WAF can rate limit by
IP, path or header before the request reaches your
server, which is the only layer that helps during a flood
([[Bot Protection]]).

**In the application, for anything that knows who the
user is.** Only your code knows the tenant, the plan and
the remaining quota. This is where per-tenant limits
live.

A shared counter in [[Redis]] is the standard
implementation — `INCR` the key, set the expiry on first
touch, reject above the limit:

```python
n = r.incr(key)             # key: "rl:tenant:12:202607281530"
if n == 1:
    r.expire(key, 60)
if n > limit:
    raise TooManyRequests(retry_after=60)
```

Two operations, no lock, and correct under concurrency
because `INCR` is atomic. In-process counters are fine
only while you run exactly one process — which is not a
state you should design around.

## What to key on

- **Authenticated traffic: the tenant, then the user.**
  The tenant limit protects your bill; the per-user limit
  stops one employee starving their colleagues.
- **Unauthenticated traffic: IP, plus a challenge.** IP
  alone is weak — offices share one, mobile carriers
  share thousands, and a residential proxy pool defeats
  it entirely. Treat it as friction, not a control.
- **Never the API key alone** if keys are self-service:
  the abuser just makes more.

## Return a useful rejection

`429 Too Many Requests`, with `Retry-After` in seconds,
and a body that says which limit was hit. Clients that
can see the limit back off politely; clients that get an
opaque error retry immediately and make it worse
([[Retry Storm]]).

Surface it in the UI as a fact, not a failure: "You have
used your 200 messages for today; the limit resets at
midnight." A 429 the user cannot interpret becomes a
support ticket.

## AI endpoints need three limits, not one

1. **Requests per minute** — the classic one.
2. **Tokens per minute or per day** — a single request
   with a 200,000-token document costs more than a
   thousand one-line questions. Requests are a poor
   proxy for cost.
3. **Concurrent generations** — long-lived streams tie up
   connections and provider capacity.

Your provider applies the same three to you: request,
input-token and output-token limits per minute, with
`429` and rate-limit headers when you exceed them. Your
own limits should be tighter than theirs, so that a busy
tenant hits *your* friendly limit rather than a provider
429 that lands on everyone at once.

## Watch out for

- **Limiting after the expensive part.** Check the budget
  before you call the provider, not after.
- **A limit that is per-process.** Ten workers with a
  local counter is a limit ten times higher than the one
  you documented.
- **Clock alignment.** Fixed windows keyed to the minute
  synchronise every client onto the same boundary.
- **Retries counting against the limit** while the client
  hammers, guaranteeing it never recovers. Reject
  cheaply, and early.
- **No exemptions.** Your own health checks, migrations
  and support tooling should have a separate key.
- **Untracked limits.** Alert when rejections spike; it
  is either abuse or a broken client, and both are
  worth knowing about tonight.

## Related

[[Usage Quotas and Metering]] · [[Bot Protection]] ·
[[Retry Storm]] · [[Cascading Failure]] ·
[[Queue Backlog]] · [[Cost Control]] · [[Redis]] ·
[[Cloudflare]] · [[LLM API Integration]] ·
[[AI Assistant Panel]] · [[Monitoring and Alerting]]

## Sources

- [[mdn-http-429]] · [[mdn-retry-after]] ·
  [[cloudflare-rate-limiting-rules]] · [[redis-incr]] ·
  [[anthropic-rate-limits]] · [[anthropic-errors]] ·
  [[cloudflare-ai-gateway]]
