---
type: Concept
title: "OAuth 2.0 and OpenID Connect"
description: "Delegated authorisation, and the identity layer built on top of it."
wikipedia: "https://en.wikipedia.org/wiki/OAuth"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# OAuth 2.0 and OpenID Connect

**OAuth 2.0** lets a user grant an application access to a
resource without sharing their password. **OpenID
Connect** adds an identity layer on top, returning an ID
token that says who the user is.

The practical distinction: OAuth alone answers "may this
app act on your behalf"; OIDC answers "who are you". Sign
in with Google is OIDC.

## What you actually implement

Very little, if you use a provider. [[Firebase Authentication]] and its peers run the flow and hand you a
verified ID token — a [[JSON Web Token]] you validate on
the backend.

## The parts worth understanding anyway

- **Authorization code flow with PKCE** is the current
  correct flow for web and mobile apps. Implicit flow is
  deprecated.
- **Scopes** limit what the token permits — an application
  of [[Least Privilege]].
- **The redirect URI must be registered exactly.** Most
  integration failures are this.

## Related

[[Authentication]] · [[JSON Web Token]] ·
[[Firebase Authentication]] · [[Auth0]] ·
[[Least Privilege]]

## Sources

- [[firebase-auth-google-signin]] · [[auth0-get-started]] ·
  [[owasp-authentication-cheatsheet]]
