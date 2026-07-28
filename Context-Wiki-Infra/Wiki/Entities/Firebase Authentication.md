---
type: Service
title: "Firebase Authentication"
description: "Google's hosted authentication - email, Google sign-in and MFA without building any of it."
wikipedia: "https://en.wikipedia.org/wiki/Firebase"
tags: [ops-and-security, auth]
timestamp: "2026-07-27T00:00:00Z"
---

# Firebase Authentication

A hosted identity service: email/password, Google, Apple
and other providers, with a client SDK and a server SDK
for token verification.

## Why it is the default recommendation here

- A generous free tier that covers most small projects.
- Email/password and Google sign-in working in an
  afternoon.
- Password reset, email verification and MFA are provided,
  not implemented by you.
- No user database of your own to breach.

## The integration pattern

1. Client SDK signs the user in and receives an ID token.
2. Client sends the token with each API request.
3. **Your backend verifies it on every request** with the
   Admin SDK — signature, expiry, audience, issuer.
4. You keep your own `users` row keyed by the Firebase
   UID.

Step 4 is what keeps you portable if you later move to
another provider.

## Watch out for

- Verify server-side, always. A client claiming to be
  logged in proves nothing.
- Firebase Security Rules matter only if you also use
  Firestore; with your own backend, your
  [[Authorization]] code is the control.
- It ties you to a Google project — factor that into
  vendor concentration.

## Related

[[Authentication]] · [[JSON Web Token]] ·
[[OAuth 2.0 and OpenID Connect]] · [[Supabase Auth]] ·
[[Auth0]] · [[Clerk]]

## Sources

- [[firebase-auth-overview]] · [[firebase-auth-web-start]]
  · [[firebase-auth-google-signin]] ·
  [[firebase-auth-password-auth]] ·
  [[firebase-auth-manage-users]] ·
  [[firebase-security-rules-get-started]]
