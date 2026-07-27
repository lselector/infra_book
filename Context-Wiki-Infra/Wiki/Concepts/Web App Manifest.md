---
type: Concept
title: "Web App Manifest"
description: "The JSON file that tells a browser how to install your site as an app."
tags: [architectures, mobile]
timestamp: "2026-07-27T00:00:00Z"
---

# Web App Manifest

A small JSON file, linked from the page head, that
describes how the site should behave when installed.

## The fields that matter

| Field | Purpose |
|---|---|
| `name` / `short_name` | label on the home screen |
| `icons` | at least 192px and 512px, maskable preferred |
| `start_url` | where launching the icon lands |
| `display` | `standalone` removes browser chrome |
| `theme_color` | colours the OS surrounding UI |

## Why it matters here

Together with a [[Service Worker]] over
[[TLS and HTTPS]], it is what makes a site installable —
the whole of [[Progressive Web App]] status rests on these
three pieces.

## Watch out for

- A missing or wrongly sized icon silently blocks the
  install prompt.
- `start_url` must be in scope of the service worker or
  offline launch fails.

## Related

[[Progressive Web App]] · [[Service Worker]] ·
[[Responsive Design]]

## Sources

- [[mdn-web-app-manifest]] ·
  [[mdn-pwa-making-installable]]
