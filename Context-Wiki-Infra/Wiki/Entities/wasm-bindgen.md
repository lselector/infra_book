---
type: Tool
title: "wasm-bindgen"
description: "The bridge between Rust and JavaScript - what makes Rust in the browser practical rather than theoretical."
website: "https://rustwasm.github.io/docs/wasm-bindgen/"
tags: [frontend, rust, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# wasm-bindgen

[[WebAssembly]] on its own can only pass numbers between
Rust and JavaScript. wasm-bindgen generates the glue
that makes strings, structs, closures, `Promise`s and
DOM objects cross the boundary, in both directions.

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn thumbnail(bytes: &[u8], width: u32) -> Vec<u8> {
    resize(bytes, width)      // heavy work, user's CPU
}
```

```javascript
import init, { thumbnail } from "./pkg/imgtools.js"
await init()
const small = thumbnail(new Uint8Array(buf), 640)
```

## The toolchain around it

- **`wasm-pack`** — builds the crate, runs wasm-bindgen,
  and emits an npm-ready package with the `.wasm`, the
  JS shim and TypeScript types.
- **`web-sys` / `js-sys`** — generated bindings to the
  browser APIs and JavaScript built-ins.
- **`wasm-opt`** (binaryen) — the size pass that turns
  an unacceptable bundle into an acceptable one; run it
  in release builds.

## Shipping it

The output is static assets, so it deploys like the rest
of a rung-1 site: hashed filenames
([[Cache Busting]]), `Cache-Control: immutable`, and
`Content-Type: application/wasm` so the browser can
stream-compile. [[Cloudflare Pages]] serves it as-is.

## Watch out for

- **Size.** Build with `--release`, `opt-level = "z"`,
  `lto = true`, `panic = "abort"`, then `wasm-opt -Oz`.
  Measure against [[Core Web Vitals]] and load it lazily
  — only when the feature is used.
- **Boundary crossings are not free.** Pass one big
  buffer, not a thousand small calls.
- **No threads by default.** `SharedArrayBuffer` needs
  cross-origin isolation headers
  ([[Security Headers]]) — a deployment decision, not a
  code one.
- **Debugging.** Keep `console_error_panic_hook` in
  development or a Rust panic surfaces as `unreachable`.

## Related

[[WebAssembly]] · [[Rust]] · [[Leptos]] ·
[[Cache Busting]] · [[Core Web Vitals]] ·
[[Cloudflare Pages]] · [[Backend-Free Interactivity]]

## Sources

- Upstream documentation:
  <https://rustwasm.github.io/docs/wasm-bindgen/>.
  Not part of the downloaded `Raw/` corpus — no capture
  to cite yet.
