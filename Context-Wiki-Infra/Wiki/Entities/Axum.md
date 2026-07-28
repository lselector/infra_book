---
type: Tool
title: "Axum"
description: "The default Rust web framework - Tokio's own, built on Tower middleware."
website: "https://github.com/tokio-rs/axum"
tags: [architectures, deployments, rust]
timestamp: "2026-07-28T00:00:00Z"
---

# Axum

A web framework from the [[Tokio]] team. Handlers are
plain async functions, arguments are *extractors*, and
middleware comes from the Tower ecosystem shared with
the rest of the Rust server world.

```rust
use axum::{routing::get, Json, Router};

async fn health() -> &'static str { "ok" }

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/healthz", get(health))
        .route("/api/items", get(list_items));
    let listener = tokio::net::TcpListener::bind(
        "127.0.0.1:8000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

Behind [[Caddy]], supervised by [[systemd]], that is the
[[Rust]] version of the rung-5 one-box stack in
[[Stacks]] — same shape as [[FastAPI]], with a static
binary instead of an interpreter.

## What you get from the ecosystem

- **Tower middleware**: timeouts, concurrency limits,
  retries, tracing, compression — composable layers that
  also work with other Rust servers.
- **`sqlx`** for compile-time-checked SQL against
  [[PostgreSQL]] or [[SQLite]], with pooling
  ([[Connection Pooling]]).
- **`tracing`** for structured logs and spans, which is
  what makes [[Monitoring and Alerting]] tolerable in an
  async system.
- **WebSockets** built in — the realtime tier discussed
  in [[Sticky Sessions]].

## Watch out for

- **Extractor order matters**: the body-consuming
  extractor must be last, and the compiler error when it
  is not is famously opaque.
- **Blocking calls in async handlers** stall the
  executor thread — use `spawn_blocking` for CPU work
  or synchronous libraries.
- **Set limits explicitly**: body size, request timeout,
  concurrency. Defaults are permissive.
- **Version churn** with `tower-http` and `hyper`
  releases; pin them in `Cargo.lock` (commit it).

## Related

[[Rust]] · [[Tokio]] · [[Actix Web]] · [[FastAPI]] ·
[[Caddy]] · [[systemd]] · [[PostgreSQL]] ·
[[Connection Pooling]] · [[One-Box Deployment]]

## Sources

- Upstream documentation:
  <https://github.com/tokio-rs/axum> and
  <https://docs.rs/axum>. Not part of the downloaded
  `Raw/` corpus — no capture to cite yet.
