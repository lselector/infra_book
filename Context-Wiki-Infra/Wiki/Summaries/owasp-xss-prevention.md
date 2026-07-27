---
type: Summary
title: "OWASP — cross-site scripting prevention cheat sheet"
description: "This cheat sheet helps developers prevent XSS vulnerabilities."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-xss-prevention.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — cross-site scripting prevention cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-xss-prevention.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html>

## Opening

> This cheat sheet helps developers prevent XSS vulnerabilities.
> Cross-Site Scripting (XSS) is a misnomer. Originally this term was derived from early versions of the attack that were primarily focused on stealing data cross-site. Since then, the term has widened to include injection of basically any content. XSS attacks are serious and can lead to account ...
> Fortunately, applications built with modern web frameworks have fewer XSS bugs, because these frameworks steer developers towards good security practices and help mitigate XSS by using templating, auto-escaping, and more. However, developers need to know that problems can occur if frameworks are ...
> When you use a modern web framework, you need to know how your framework prevents XSS and where it has gaps. There will be times where you need to do something outside the protection provided by your framework, which means that Output Encoding and HTML Sanitization can be critical. OWASP will be ...

## Contents of the source document

- Cross Site Scripting Prevention Cheat Sheet¶
  - Introduction¶
  - Framework Security¶
  - XSS Defense Philosophy¶
  - Output Encoding¶
    - Output Encoding for “HTML Contexts”¶
    - Output Encoding for “HTML Attribute Contexts”¶
    - Output Encoding for “JavaScript Contexts”¶
    - Output Encoding for “CSS Contexts”¶
    - Output Encoding for “URL Contexts”¶
    - Dangerous Contexts¶
  - HTML Sanitization¶
  - Safe Sinks¶
  - Other Controls¶
    - XSS Prevention Rules Summary¶
    - Output Encoding Rules Summary¶
  - Common Anti-patterns: Ineffective Approaches to Avoid¶
    - Sole Reliance on Content-Security-Policy (CSP) Headers¶

## Related pages

[[Anti-Patterns]] · [[HTTP]] · [[OWASP]] · [[Render]]
