---
type: Service
title: "Cloudflare Turnstile"
description: "An invisible CAPTCHA replacement you can put on any site, including one that does not use Cloudflare."
wikipedia: "https://en.wikipedia.org/wiki/Cloudflare"
tags: [ai-in-saas, ops-and-security, security]
timestamp: "2026-07-28T00:00:00Z"
---

# Cloudflare Turnstile

A widget that decides whether a visitor is a browser
driven by a person, without making them identify
motorcycles. It runs non-interactive checks —
proof-of-work, browser API probing, behavioural signals —
and issues a token your server verifies.

The useful property for this wiki: **it works on any
site**, whether or not the traffic goes through
[[Cloudflare]]'s network. There is a free tier.

## The flow

1. Drop the widget script and a `<div>` with your site
   key into the form or page.
2. It produces a token in a hidden
   `cf-turnstile-response` field.
3. Your backend POSTs that token, plus your secret key,
   to the siteverify endpoint.
4. Verify the response, once, and bind the result to the
   session. Then serve the request.

Step 4 is the one people skip. A token that is never
verified server-side is decoration.

## Where it fits

The obvious use is signup and contact forms
([[Forms Without a Backend]] covers the honeypot version
for static sites). The one that matters for an AI feature
is the **unauthenticated demo**: a public "try it" widget
with no user account behind it, calling an endpoint that
costs money per request. A challenge in front of that,
plus per-token and global caps, is the difference between
a marketing page and a free inference service for
strangers ([[Bot Protection]]).

## Watch out for

- **It is one layer.** Determined abuse buys solved
  tokens. Keep [[Rate Limiting]] and quotas behind it.
- **Verify server-side, once.** Tokens are single-use and
  short-lived; do not accept a replay.
- **Widget modes.** Managed, non-interactive and
  invisible differ in how often a human sees anything —
  prefer the ones that show nothing
  ([[Core Web Vitals]] and accessibility both improve).
- **The secret key is a secret** — server-side only
  ([[Secrets Management]]).
- **Privacy questions.** Enterprise customers will ask
  what the widget collects; the vendor's answer is part
  of your [[SOC 2]] vendor list.

## Related

[[Bot Protection]] · [[Cloudflare]] · [[Rate Limiting]] ·
[[Forms Without a Backend]] · [[Web3Forms]] ·
[[Authentication]] · [[AI Assistant Panel]] ·
[[Landing Page Email Capture]]

## Sources

- [[cloudflare-turnstile]] · [[cloudflare-bots]] ·
  [[web3forms-spam-protection]] ·
  [[cloudflare-rate-limiting-rules]]
