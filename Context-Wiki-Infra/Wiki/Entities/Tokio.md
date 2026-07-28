---
type: Tool
title: "Tokio"
description: "The async runtime under almost every Rust network service - the scheduler your handlers actually run on."
wikipedia: "https://en.wikipedia.org/wiki/Tokio_(software)"
tags: [architectures, rust, foundations]
timestamp: "2026-07-28T00:00:00Z"
---

# Tokio

The asynchronous runtime for [[Rust]]: a multi-threaded,
work-stealing scheduler plus async networking, timers,
synchronisation primitives and channels. [[Axum]] runs
on it; so do `hyper`, `reqwest`, `sqlx` and most of the
crates a service depends on.

## Why it belongs in an infrastructure wiki

It is the thing that decides how your service behaves
under load. Tasks are cheap — hundreds of thousands per
process — and the scheduler spreads them across every
core. That is how one small VM serves connection counts
that would need a fleet of thread-per-request workers,
which is the practical argument for Rust on the rungs of
[[Stacks]] where efficiency starts to cost money.

## The rule that causes every incident

**Never block a worker thread.** A synchronous file
read, a `std::thread::sleep`, a CPU-heavy loop, or a
blocking database driver inside an `async fn` stops one
of your (few) executor threads. Enough of those and the
whole service stalls while the CPU looks idle.

```rust
// CPU-bound or blocking work goes here:
let out = tokio::task::spawn_blocking(move || {
    resize_image(bytes)          // sync, expensive
}).await?;
```

The same failure mode as blocking the [[Node.js]] event
loop, with more threads to hide it slightly longer.

## Worth knowing

- **`tracing`** — structured, span-based logging built
  for async, and the only sane way to follow a request
  across tasks ([[Monitoring and Alerting]]).
- **Graceful shutdown** — `tokio::signal` plus a
  cancellation token, so `SIGTERM` drains connections
  rather than cutting them.
- **Channels** — `mpsc` for a worker queue in-process,
  before you reach for [[Message Queues]].
- **Feature flags** — depend on the features you use;
  `full` is convenient and slows compiles.

## Related

[[Rust]] · [[Axum]] · [[Actix Web]] · [[Node.js]] ·
[[Message Queues]] · [[Monitoring and Alerting]] ·
[[Sticky Sessions]]

## Sources

- Upstream documentation: <https://tokio.rs>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
