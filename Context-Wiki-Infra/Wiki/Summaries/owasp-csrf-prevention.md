---
type: Summary
title: "OWASP — cross-site request forgery prevention cheat sheet"
description: "A Cross-Site Request Forgery (CSRF) attack occurs when a malicious web site, email, blog, instant message, or program tricks an authenticated user's web browser into performing an unwanted a"
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-csrf-prevention.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — cross-site request forgery prevention cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-csrf-prevention.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html>

## Opening

> A [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) attack occurs when a malicious web site, email, blog, instant message, or program tricks an authenticated user's web browser into performing an unwanted action on a trusted site. If a target user is authenticated to ...
> Since browser requests automatically include all cookies including session cookies, this attack works unless proper authorization is used, which means that the target site's challenge-response mechanism does not verify the identity and authority of the requester. In effect, CSRF attacks make a ...
> However, successful CSRF attacks can only exploit the capabilities exposed by the vulnerable application and the user's privileges. Depending on the user's credentials, the attacker can transfer funds, change a password, make an unauthorized purchase, elevate privileges for a target account, or ...
> In short, the following principles should be followed to defend against CSRF:

## Contents of the source document

- Cross-Site Request Forgery Prevention Cheat Sheet¶
  - Introduction¶
    - Built-In Or Existing CSRF Implementations¶
  - Token-Based Mitigation¶
    - Synchronizer Token Pattern¶
    - ALTERNATIVE: Using A Double-Submit Cookie Pattern¶
    - Naive Double-Submit Cookie Pattern (DISCOURAGED)¶
  - Fetch Metadata headers¶
    - Ease of use¶
    - Browser compatibility¶
    - How to treat Fetch Metadata headers on the server-side¶
    - Requirements¶
    - Concerns¶
    - Rollout & testing recommendations¶
  - Disallowing simple requests¶
    - Disallowing simple content types¶
    - Employing Custom Request Headers for AJAX/API¶
  - Dealing with Client-Side CSRF Attacks (IMPORTANT)¶

## Related pages

[[Authentication]] · [[Authorization]] · [[CORS]] · [[Django]] · [[HTTP]] · [[Multi-Tenant SaaS]] · [[OWASP]]
