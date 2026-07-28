---
type: Tool
title: "Rust"
description: "A compiled language with no runtime and no garbage collector - small containers, flat memory, and a slower first week."
wikipedia: "https://en.wikipedia.org/wiki/Rust_(programming_language)"
tags: [architectures, deployments, rust]
timestamp: "2026-07-28T00:00:00Z"
---

# Rust

A systems language with memory safety enforced at
compile time rather than by a garbage collector. For the
infrastructure in this wiki, three consequences matter
more than the language itself.

## What it changes operationally

1. **One static binary.** No interpreter, no
   `node_modules`, no virtualenv. Deployment is `scp` a
   file and restart a [[systemd]] unit; a container
   image built `FROM scratch` or distroless is 5–20 MB
   rather than several hundred
   ([[Containers in Production]]).
2. **Flat, predictable memory.** No GC pauses and no
   heap that grows until the OOM killer arrives. A
   service that fits in 64 MB *keeps* fitting, which
   makes the smallest VM tiers genuinely usable.
3. **Concurrency without a thread-per-request budget.**
   Async tasks on [[Tokio]] handle tens of thousands of
   connections per process — the same profile as
   [[Node.js]], with every core in use.

Together: fewer machines for the same load, and boring
long-running processes. That is the whole argument.

## What it costs

- **Time to first version.** The borrow checker is a
  real learning curve, and idiomatic async Rust is
  another.
- **Compile times** measured in minutes, which changes
  how CI feels ([[GitHub Actions]] caching matters).
- **Ecosystem depth** for niche vendor SDKs is thinner
  than Python's or JavaScript's.

**Use it when** the service is long-lived, hot, or
resource-constrained — a proxy, an ingest endpoint, an
image pipeline, a WebSocket fan-out, anything on the
critical path. **Don't** rewrite a CRUD app that
[[FastAPI]] serves fine.

## Where it shows up in this stack

- Server: [[Axum]] or [[Actix Web]] on [[Tokio]].
- Browser: compiled to [[WebAssembly]] via
  [[wasm-bindgen]], or a whole UI in [[Leptos]].
- Tools you already run: [[uv]], [[Polars]] and
  `ripgrep` are Rust; so is much of Cloudflare's edge.

## Related

[[Axum]] · [[Actix Web]] · [[Tokio]] ·
[[WebAssembly]] · [[wasm-bindgen]] · [[Leptos]] ·
[[Polars]] · [[Containers in Production]] ·
[[One-Box Deployment]] · [[FastAPI]]

## Sources

- Upstream documentation: <https://doc.rust-lang.org/book/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
