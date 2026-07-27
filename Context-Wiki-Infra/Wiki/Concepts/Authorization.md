---
type: Concept
title: "Authorization"
description: "What an authenticated user may do - enforced on the server, in one place, failing closed."
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Authorization

Deciding whether this user may perform this action on this
object.

## The rules that prevent the common bugs

1. **Enforce on the server.** Hiding a button is UI, not
   security.
2. **Check object ownership, not just role.** "Is this
   user an editor" is not the same as "does this user own
   record 4711". Missing the second is the most common
   real-world vulnerability class.
3. **Deny by default.** New endpoints should be
   inaccessible until explicitly opened.
4. **Centralise the check.** One decision function, not a
   condition scattered through every handler.

## Why it matters here

In [[Multi-Tenant SaaS]] this is the control that stops
one customer reading another's data. Enforce the tenant
filter in a single query layer that fails closed, and test
it deliberately.

## Related

[[Authentication]] · [[Least Privilege]] ·
[[Multi-Tenant SaaS]] · [[Security Testing]] ·
[[Access Review]]

## Sources

- [[owasp-authorization-cheatsheet]] · [[owasp-top-ten]] ·
  [[owasp-asvs]]
