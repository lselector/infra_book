---
type: Concept
title: "Security Headers"
description: "A handful of response headers that shut down whole classes of browser attack."
wikipedia: "https://en.wikipedia.org/wiki/List_of_HTTP_header_fields"
tags: [ops-and-security, security]
timestamp: "2026-07-27T00:00:00Z"
---

# Security Headers

Response headers that instruct the browser to enforce
restrictions on your behalf.

## The set worth having

| Header | Effect |
|---|---|
| `Strict-Transport-Security` | browser refuses plaintext HTTP |
| `Content-Security-Policy` | restricts where scripts may load from |
| `X-Content-Type-Options: nosniff` | stops MIME sniffing |
| `Referrer-Policy` | limits URL leakage to third parties |
| `Permissions-Policy` | turns off camera, mic, geolocation |

## Content Security Policy

The most powerful and the most work. A strict CSP is the
main structural defence against cross-site scripting, but
it will break inline scripts and styles — which is why it
is best adopted on a new project, or via report-only mode
first.

## Why it matters here

They are set in one place — the [[Reverse Proxy]], or a
`_headers` file on [[Cloudflare Pages]] — and apply to the
whole site. Minutes of work, and they show up immediately
in any [[Security Testing]] scan.

## Related

[[TLS and HTTPS]] · [[Encryption in Transit]] ·
[[Security Testing]] · [[Reverse Proxy]] · [[CORS]] ·
[[Prompt Injection]]

## Sources

- [[mdn-content-security-policy]] ·
  [[mdn-security-practical-guides]] ·
  [[mdn-strict-transport-security]] ·
  [[cloudflare-pages-headers]]
