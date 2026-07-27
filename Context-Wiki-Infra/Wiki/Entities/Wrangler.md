---
type: Tool
title: "Wrangler"
description: "Cloudflare's CLI - the command that deploys a folder to Pages."
tags: [deployments, cli]
timestamp: "2026-07-27T00:00:00Z"
---

# Wrangler

The command-line tool for Cloudflare Workers and Pages.

## The command that matters

```bash
npx wrangler pages deploy ./website \
  --project-name=my-site \
  --commit-dirty=true
```

That single line is the deploy step of a
[[Static Build Pipeline]]. `npx` avoids a global install;
`--commit-dirty` suppresses the prompt when deploying a
working tree that has uncommitted changes.

## Other useful commands

- `wrangler pages deployment list` — history, and the IDs
  you roll back to.
- `wrangler pages project list` — projects in the account.
- `wrangler secret put` — set a secret for a Worker
  without it entering the repository.

## Authentication

`wrangler login` for interactive use; a scoped API token
in `CLOUDFLARE_API_TOKEN` for CI. Scope the token to the
one project — see [[Least Privilege]].

## Watch out for

Wrangler changes quickly across major versions; pin it in
CI so a deploy does not break because of an upstream
release.

## Related

[[Cloudflare Pages]] · [[Static Build Pipeline]] ·
[[Continuous Integration and Delivery]] ·
[[Secrets Management]]

## Sources

- [[cloudflare-wrangler-pages-commands]] ·
  [[cloudflare-wrangler-install]] ·
  [[cloudflare-wrangler-workers-commands]]
