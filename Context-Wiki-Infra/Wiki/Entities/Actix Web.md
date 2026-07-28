---
type: Tool
title: "Actix Web"
description: "The other mature Rust web framework - a multi-threaded actor runtime with a long benchmark pedigree."
website: "https://actix.rs/"
tags: [architectures, deployments, rust]
timestamp: "2026-07-28T00:00:00Z"
---

# Actix Web

A mature, fast web framework for [[Rust]], older than
[[Axum]] and consistently near the top of the public
throughput benchmarks.

```rust
use actix_web::{get, App, HttpServer, Responder};

#[get("/healthz")]
async fn health() -> impl Responder { "ok" }

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(health))
        .bind(("127.0.0.1", 8000))?
        .run()
        .await
}
```

## Actix Web or Axum?

Both are production-grade; neither choice is a mistake.

- **Axum** shares the Tower middleware ecosystem with
  the rest of the [[Tokio]] world, and is where new
  Rust web work has been converging.
- **Actix Web** has a longer track record, its own actor
  model underneath, and a worker-per-core `HttpServer`
  that some workloads like.

Pick Axum if you have no reason not to; pick Actix Web
if you want its runtime or its ergonomics.

## Watch out for

- **App state is per worker.** `HttpServer::new` runs
  your factory once per worker thread; shared state must
  be built outside and cloned in (`web::Data`), or you
  get one cache per core without noticing.
- **Blocking work** in a handler blocks that worker —
  `web::block` for synchronous calls.
- **Its own runtime.** Mostly Tokio-compatible, but not
  every Tokio-shaped crate drops straight in.
- The project's early governance controversy is long
  settled; it is actively maintained.

## Related

[[Rust]] · [[Axum]] · [[Tokio]] · [[Caddy]] ·
[[systemd]] · [[One-Box Deployment]] · [[FastAPI]]

## Sources

- Upstream documentation: <https://actix.rs>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
