# Outside Links (Wikipedia, or the project's own site)

Every content page in the wiki — the 109 Concept pages
and the 120 Entity pages — links out to a description of its
subject that this wiki did not write: the English
Wikipedia article where one exists, and the project's own
site where it does not. Both render in the page infobox
and open in a new tab.

The wiki says what a thing is *for this project*: which
rung of the ladder it belongs to, what it costs, what it
breaks. Wikipedia says what it is in general, who makes
it, and when it appeared. One link joins the two without
either having to repeat the other. Where Wikipedia has
nothing — true of twenty-two of the newer products —
the vendor's own site is the next best authority, and
far better than a dead end.

## The pieces

| File | Role |
|------|------|
| `wikipedia_links.json` | The curated maps: `links` (page → article **title**, or `null`) and `websites` (page → full URL) |
| `wikipedia_links.py` | Verifies both, writes the URLs into frontmatter |
| `wiki_server.py` | Renders `wikipedia:` and `website:` as infobox links |

## Usage

```bash
python wikipedia_links.py status   # offline coverage
python wikipedia_links.py check    # verify vs the API
python wikipedia_links.py apply    # write frontmatter
```

`apply` is idempotent: it replaces an existing
`wikipedia:` or `website:` line, inserts one (after
`description:` and after `wikipedia:` respectively) if
absent, and removes one when the map no longer has a
value. Pages are otherwise untouched.

## Curated, not guessed

The map stores titles chosen by hand, because automatic
matching on a page name is wrong often enough to matter,
and a confidently wrong link is worse than no link:

- **Trivy** — the security scanner has no article;
  `Trivy` is a commune in Saône-et-Loire.
- **Resend** — the email API has no article; `Resend`
  redirects to *Retransmission (data networks)*.
- **Railway**, **Render**, **Postmark**, **Clerk** — all
  real English words, none of them about these products.
- **Axum** — the Rust web framework has no article;
  `Axum` is a town in the Tigray Region of Ethiopia.
- **Actix** — redirects to *Actix Systems*, a graphics
  adapter manufacturer that closed in 1998.
- **OSS-Fuzz** — Google's fuzzing service has no article
  at all, despite the tens of thousands of bugs it has
  filed.
- **AFL++**, **MITRE ATT&CK** — both exist but not under
  the obvious title: *American Fuzzy Lop (software)* and
  *ATT&CK*. A redirect today is a broken assumption
  tomorrow, so the map stores the real one.

`check` is what makes the map trustworthy. For every
title it asks the MediaWiki API whether the page exists,
whether it is a redirect, and whether it is a
disambiguation page, and prints the article's first
sentence so a wrong target is obvious on sight:

```text
ok  Caddy                    -> Caddy (web server)
    Caddy is an extensible, cross-platform, open-source web server written in Go.
```

It exits non-zero if any title is missing, ambiguous, or
has become a redirect — worth re-running occasionally,
since Wikipedia titles move.

The same command then fetches all twenty-two website URLs
and prints their status. A `403` is reported as `WAF`
rather than counted as a failure: some vendor sites
(Drata's, on one run) sit behind a bot challenge that an
automated client cannot pass, which says nothing about
whether the URL is right. Anything else non-200 is a real
failure and fails the run.

## The two rules behind the map

1. **Link the article about *this* thing when it exists.**
   `Zed` → *Zed (text editor)*, not *Z*.
2. **Otherwise link the vendor or family article, never a
   generic concept.** The AWS services without articles of
   their own point at *Amazon Web Services*; the six
   Cloudflare product pages point at *Cloudflare*. The
   concept articles are already linked from the Concept
   pages that own them, so pointing a product page at one
   would say something untrue about the product.

Because the infobox is labelled with the **target
article's title**, a broader link is visible as such:
`AWS CloudTrail` shows "Amazon Web Services", so nobody
mistakes it for an article about CloudTrail.

## Coverage

| | |
|---|---|
| Content pages | 229 |
| Wikipedia article | 204 |
| Project website | 22 |
| No outside link | 3 |

The 22 on their own site are the products Wikipedia has
no article for:

| Page | Site |
|---|---|
| Actix Web | <https://actix.rs/> |
| AWeber | <https://www.aweber.com/> |
| Axum | <https://github.com/tokio-rs/axum> |
| Clerk | <https://clerk.com/> |
| Drata | <https://drata.com/> |
| Fly.io | <https://fly.io/> |
| Gitleaks | <https://gitleaks.io/> |
| Invoke | <https://www.pyinvoke.org/> |
| just | <https://just.systems/> |
| Leptos | <https://leptos.dev/> |
| OSS-Fuzz | <https://google.github.io/oss-fuzz/> |
| Postmark | <https://postmarkapp.com/> |
| Railway | <https://railway.com/> |
| Render | <https://render.com/> |
| Resend | <https://resend.com/> |
| SOPS | <https://getsops.io/> |
| Supabase Auth | <https://supabase.com/auth> |
| Trivy | <https://trivy.dev/> |
| Uptime Kuma | <https://uptimekuma.org/> |
| uv | <https://docs.astral.sh/uv/> |
| Web3Forms | <https://web3forms.com/> |
| wasm-bindgen | <https://rustwasm.github.io/docs/wasm-bindgen/> |

If an article appears for one of them later, add the
title to `links` and drop the `websites` entry — a page
carries whichever it has, and Wikipedia takes precedence
because it is the neutral description.

The 3 with no outside link at all are `Cost Control`,
`The Ladder` and `DataFrames`: the first two are this
wiki's own framing, and the third has no encyclopedia
article — Wikipedia's `Data frame` is about network
frames, and its `DataFrame` does not exist. The three
tools it names carry the links instead.

Summaries carry no `wikipedia` field by design — a
summary is *about a specific captured document*, not
about a subject, and its infobox already links the
capture in `Raw/`.

## Rendering

`wiki_server.py` renders each field as an infobox row,
labelled with the article title or the site's host:

```html
<a class="ext" href="https://en.wikipedia.org/wiki/Caddy_(web_server)"
   target="_blank" rel="noopener noreferrer">Caddy (web server)</a>

<a class="ext" href="https://trivy.dev/"
   target="_blank" rel="noopener noreferrer">trivy.dev</a>
```

- `target="_blank"` — opens in a new tab, so you never
  lose your place in the wiki.
- `rel="noopener noreferrer"` — the standard companion to
  `target="_blank"`; without it the opened page gets a
  handle on this one via `window.opener`.
- `a.ext::after` adds a small ↗ so a link that leaves the
  site looks different from one that does not.

## Adding a page later

1. Write the page in `Wiki/Concepts/` or `Wiki/Entities/`.
2. Add its name to `links` in `wikipedia_links.json` — a
   title, or `null` if Wikipedia has nothing suitable.
3. If `null` and the subject is a real product, add its
   site to `websites`.
4. `python wikipedia_links.py check` — read the first
   sentence it prints and confirm it is the right subject,
   and that any new URL answers.
5. `python wikipedia_links.py apply`.

`status` fails loudly if a content page is missing from
the map, or either map names a page that no longer
exists, so the two cannot drift apart unnoticed. It also
prints the pages with no outside link at all, which
should stay a very short list.

## See also

- [d1_okf.md](d1_okf.md) — the `wikipedia` and `website`
  frontmatter fields among the other OKF fields.
- [d5_wiki_server.md](d5_wiki_server.md) — the infobox
  that renders it.
- [d7_wiki_build.md](d7_wiki_build.md) — the rest of the
  frontmatter, and how pages are generated.
