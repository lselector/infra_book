---
type: Concept
title: "WebAssembly"
description: "Compiled code running in the browser at near-native speed - what it is genuinely good for, and what it is not."
wikipedia: "https://en.wikipedia.org/wiki/WebAssembly"
tags: [frontend, architectures, rust]
timestamp: "2026-07-28T00:00:00Z"
---

# WebAssembly

A portable binary instruction format that browsers
execute in a sandbox, alongside JavaScript. Compile
[[Rust]], C, C++, Go or Zig to `.wasm`, ship it like any
other asset, and it runs at a large fraction of native
speed on every modern browser.

## What it is actually good at

- **CPU-bound work in the page**: image and video
  processing, audio, compression, cryptography,
  simulation, physics, CAD, spreadsheets.
- **Reusing an existing library** rather than porting
  it. FFmpeg, SQLite and image codecs all run this way.
- **Data work in the browser**: parsing large files,
  running queries over Parquet client-side, charting
  millions of points.
- **Sharing one implementation** between server and
  browser — the same [[Rust]] validation crate compiled
  both ways cannot drift.

## What it is not

**Not a replacement for JavaScript, and not automatically
faster.** DOM manipulation still goes through JS
bindings, and every call across the boundary costs. A
CRUD form rewritten in Wasm is slower to load and no
faster to use.

**Not smaller.** A "hello world" Rust/Wasm bundle starts
in the hundreds of kilobytes before you optimise. Against
[[Core Web Vitals]], that is a real cost you must earn
back with real computation.

## What it means for infrastructure — the good part

The work happens **on the user's CPU**, which is free to
you. Resizing images in the browser before upload,
filtering a dataset client-side, running a search index
locally — each is a server you do not rent, a queue you
do not run, and data that never leaves the machine.
For a rung-1 or rung-2 stack in [[Stacks]], Wasm buys
capability that would otherwise force a backend.

## Getting it into a page

For [[Rust]]: [[wasm-bindgen]] generates the JS glue,
`wasm-pack` builds an npm-consumable package, and
[[Leptos]] (or Yew, or Dioxus) goes further and lets you
write the whole UI in Rust. Serve `.wasm` with
`Content-Type: application/wasm`, `Cache-Control:
immutable`, and a hashed filename
([[Cache Busting]]) — it is a static asset like any
other, so it lives happily on [[Cloudflare Pages]].

Beyond the browser, the same binaries run on edge
runtimes (Cloudflare Workers) — the reason a Worker can
start in under a millisecond.

## Related

[[Rust]] · [[wasm-bindgen]] · [[Leptos]] ·
[[Core Web Vitals]] · [[Backend-Free Interactivity]] ·
[[Service Worker]] · [[Progressive Web App]] ·
[[Cloudflare Pages]] · [[Cache Busting]]

## Sources

- Upstream documentation: the WebAssembly specification
  site and the Rust and WebAssembly book. Not part of
  the downloaded `Raw/` corpus — no capture to cite yet.
