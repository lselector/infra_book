---
type: Concept
title: "JSON Web Token"
description: "A signed, self-describing token - convenient, and awkward to revoke."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# JSON Web Token

A base64url-encoded header, payload and signature. Anyone
can read it; only the holder of the key can produce a
valid one.

## Verifying one properly

- Check the **signature** against the issuer's public key.
- Check **`exp`** — is it expired.
- Check **`iss`** and **`aud`** — issued by who you expect,
  for your application.
- **Reject `alg: none`**, and do not let the token choose
  its own algorithm.

Use a maintained library. Hand-rolled verification is
where the historic vulnerabilities live.

## The trade-off to understand

A JWT is stateless: your server needs no session store,
which is why it suits
[[Single Page Application and API]]. The cost is that it
remains valid until it expires — you cannot easily revoke
one. Mitigate with short lifetimes plus a refresh token,
and a deny-list for the rare forced logout.

## Watch out for

Putting anything secret in the payload. It is signed, not
encrypted, and trivially readable.

## Related

[[Authentication]] · [[OAuth 2.0 and OpenID Connect]] ·
[[Single Page Application and API]] · [[Key Rotation]]

## Sources

- [[firebase-auth-web-start]] ·
  [[owasp-authentication-cheatsheet]]
