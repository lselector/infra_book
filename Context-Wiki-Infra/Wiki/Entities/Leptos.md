---
type: Tool
title: "Leptos"
description: "A full web UI framework in Rust - fine-grained reactivity, compiled to WebAssembly, with optional SSR."
website: "https://leptos.dev/"
tags: [frontend, rust, javascript]
timestamp: "2026-07-28T00:00:00Z"
---

# Leptos

A [[Rust]] framework for building web UIs. Components
are functions, reactivity is fine-grained (signals
update exactly the DOM nodes that depend on them, with
no virtual DOM diff), and the whole thing compiles to
[[WebAssembly]].

```rust
#[component]
fn Counter() -> impl IntoView {
    let (count, set_count) = signal(0);
    view! {
        <button on:click=move |_| *set_count.write() += 1>
            "Clicked " {count} " times"
        </button>
    }
}
```

## Why it is interesting for infrastructure

- **One language across the stack.** Types, validation
  and domain logic are shared between the [[Axum]]
  server and the browser, so they cannot drift.
- **Server functions.** Write an `async fn`, annotate
  it, and call it from the client; the framework
  generates the endpoint. No hand-written API layer for
  internal calls.
- **SSR with hydration** when you want it — the same
  trade-offs as [[Server-Side Rendering]], including
  the [[Node.js]]-shaped one it avoids: the server here
  is your existing Rust binary, not a second runtime.
- **CSR-only builds are static files** — Trunk emits a
  `dist/` you can put on [[Cloudflare Pages]] with
  nothing to operate.

## Honest limitations

- **Small ecosystem.** No equivalent of React's
  component libraries; you will write more UI yourself.
- **Bundle size** starts higher than a JS framework's,
  even after `wasm-opt` ([[Core Web Vitals]]).
- **Hiring and handover.** Far fewer people can pick it
  up than [[React]].
- **Moving target.** Signal APIs changed meaningfully
  across recent major versions; pin the version.

Yew and Dioxus occupy the same space with different
trade-offs; the infrastructure story is identical.

**Use it when** the team is already writing Rust and the
UI is an app. Otherwise [[React]] is the boring,
correct answer.

## Related

[[Rust]] · [[WebAssembly]] · [[wasm-bindgen]] ·
[[Axum]] · [[React]] · [[Server-Side Rendering]] ·
[[Cloudflare Pages]] · [[Core Web Vitals]]

## Sources

- Upstream documentation: <https://leptos.dev> and
  <https://book.leptos.dev>. Not part of the downloaded
  `Raw/` corpus — no capture to cite yet.
