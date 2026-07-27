---
type: Concept
title: "Domain Names and DNS"
description: "How a name becomes an IP address, and what a registrar, nameserver and resolver each do."
tags: [foundations, networking]
timestamp: "2026-07-27T00:00:00Z"
---

# Domain Names and DNS

A domain name is a rented label. DNS is the distributed
directory that turns that label into an address a browser
can connect to.

## The three roles

- **Registrar** — who you rent the name from
  ([[Cloudflare Registrar]]). Handles renewal and
  ownership.
- **Authoritative nameserver** — holds the actual records
  for your zone ([[Cloudflare DNS]]). You point the
  registrar at these.
- **Resolver** — the recursive server your visitor's
  network uses to look the name up and cache the answer.

Registrar and nameserver do not have to be the same
company; pointing an externally registered domain at
Cloudflare's nameservers is a normal, well-trodden setup.

## Why it matters here

- DNS is the first thing you configure on every rung of
  [[The Ladder]] and the last thing you should change
  carelessly.
- TTL governs how long a change takes to propagate. Lower
  it *before* a planned migration, not during one.
- Email depends on DNS too: [[Email Authentication]]
  records live in the same zone.

## Watch out for

- Propagation delay is really cache expiry. A record with
  a 24-hour TTL will be stale for up to 24 hours.
- Registrar lock and the 60-day post-transfer lock will
  block an urgent move. Plan transfers early.

## Related

[[DNS Record Types]] · [[TLS and HTTPS]] ·
[[Content Delivery Network]] · [[Email Authentication]]

## Sources

- [[cloudflare-what-is-dns]] ·
  [[mdn-what-is-a-domain-name]] ·
  [[cloudflare-dns-full-setup]]
