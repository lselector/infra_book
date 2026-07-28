---
type: Concept
title: "Authentication"
description: "Proving who a user is - and the strong argument for never building it yourself."
wikipedia: "https://en.wikipedia.org/wiki/Authentication"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Authentication

Establishing that a request comes from a particular user.
Distinct from [[Authorization]], which is what that user
may then do.

## Why not to build it

The surface is much larger than "hash the password":
reset flows, email verification, rate limiting,
credential-stuffing defence, session invalidation,
[[Multi-Factor Authentication]], social login, account
recovery. Each is a well-documented way to get breached.

## The options here

| Option | Fits |
|---|---|
| [[Firebase Authentication]] | free tier, email + Google sign-in, minimal setup |
| [[Supabase Auth]] | if you already use Supabase Postgres |
| [[Auth0]] | enterprise SSO, SAML, complex rules |
| [[Clerk]] | polished pre-built UI components |

## The pattern regardless of provider

1. The provider authenticates and issues a token.
2. Your backend **verifies the token on every request** —
   signature, expiry, audience and issuer.
3. You keep your own `users` row keyed by the provider's
   stable user ID, holding your application's data.

Step 3 is what keeps you portable.

## Related

[[Authorization]] · [[JSON Web Token]] ·
[[OAuth 2.0 and OpenID Connect]] ·
[[Multi-Factor Authentication]] ·
[[Firebase Authentication]] ·
[[Bot Protection]]

## Sources

- [[firebase-auth-overview]] · [[firebase-auth-web-start]]
  · [[owasp-authentication-cheatsheet]] ·
  [[supabase-auth-overview]]
