---
type: Concept
title: "Bot Protection"
description: "Keeping scripts, scrapers and free-tier farms off an endpoint that costs you money per call."
wikipedia: "https://en.wikipedia.org/wiki/Internet_bot"
tags: [ai-in-saas, ops-and-security, security]
timestamp: "2026-07-28T00:00:00Z"
---

# Bot Protection

Most endpoints cost a fraction of a cent to serve, so
automated traffic is mostly a nuisance. An AI endpoint is
different: each call spends real money at a provider, so
an unprotected one is a faucet pointed at your bank
account. People will find it — resale of stolen inference
capacity is an established business.

The goal is not to eliminate bots. It is to make abuse
cost more than it yields.

## The layers, cheapest first

| Layer | Stops | Cost to you |
|---|---|---|
| Require a login | drive-by scripts | none — do this first |
| Require a paid plan for AI | signup farms | a product decision |
| Edge bot detection | known bad automation | included in most CDN plans |
| Challenge (Turnstile-style) | headless browsers | a few lines, no user friction |
| Rate limits per user and tenant | credential-sharing, runaway clients | a Redis key |
| Quotas per plan | slow, patient abuse | your metering table |
| Anomaly alerts | everything the above missed | a nightly query |

None of these is sufficient alone, and the first two do
most of the work. An assistant panel behind
[[Authentication]] on a paid plan is already a hard
target.

## The unauthenticated demo

The dangerous case is the public "try our AI" widget on
the marketing site. It has no user, so it has no user
limits — and the request it makes is visible in the
browser's network tab, which means it is a public API
five minutes after launch.

If you must ship one:

- Mint a **short-lived signed token** server-side per
  page view, and require it. Verify it, cap its uses,
  expire it in minutes.
- Put a **challenge** in front — [[Cloudflare Turnstile]]
  and equivalents run invisible checks and hand you a
  token to verify server-side. Far better than a
  picture-of-a-bus CAPTCHA for both fraud and
  accessibility.
- Cap **per IP, per token and globally**. The global cap
  is the one that saves you: a hard daily ceiling on demo
  spend, after which the widget politely says to sign up.
- Use the **cheapest model** and a short `max_tokens`.
  A demo does not need the top tier.
- Never put a provider key in the page. Ever. A key in
  client JavaScript is a key on GitHub by Friday.

## Detection beats blocking

Blunt blocking catches customers. What you actually want
is a signal, from data you already collect for
[[Usage Quotas and Metering]]:

- One account, many IPs, many countries, same hour →
  shared or sold credentials.
- Requests at a perfectly even interval → a script.
- Token usage 50x the median for that plan → either
  abuse or your best customer; both merit a phone call.
- A spike in signups from one domain or IP range, each
  immediately using the free AI allowance.

Alert on these, then act with a targeted limit rather
than a global one.

## Bots you should let in

Legitimate automation exists: the customer scripting
against you, the integration partner, your own uptime
checks, search engines on the marketing pages. Give
them the front door — an API key with its own quota and
its own rate limit — so that tightening the browser path
does not break them. Blocking a paying customer's cron
job is a worse outcome than the abuse you prevented.

## Watch out for

- **Signup abuse is the root cause.** Email verification,
  a challenge on the signup form, and blocking disposable
  domains stop more inference theft than anything at the
  chat endpoint ([[Landing Page Email Capture]] has the
  same problem in a cheaper form).
- **Honeypots still work** on forms — a hidden field that
  humans never fill in ([[Forms Without a Backend]]).
- **A challenge is a token, not a verdict.** Verify it
  server-side, once, and bind it to the session.
- **User-Agent proves nothing.** Neither does a referrer.
- **Accessibility.** Interactive puzzles exclude real
  users; prefer invisible challenges.
- **Your provider is watching too.** Sustained abuse
  through your key is your problem with them.

## Related

[[Rate Limiting]] · [[Usage Quotas and Metering]] ·
[[Cloudflare Turnstile]] · [[Cloudflare]] ·
[[Authentication]] · [[Cost Control]] ·
[[AI Assistant Panel]] · [[Forms Without a Backend]] ·
[[Security Testing]] · [[Fail2Ban]]

## Sources

- [[cloudflare-turnstile]] · [[cloudflare-bots]] ·
  [[cloudflare-rate-limiting-rules]] ·
  [[web3forms-spam-protection]] · [[owasp-llm-top-ten]] ·
  [[mdn-http-429]]
