---
type: Concept
title: "Forms Without a Backend"
description: "Accepting contact and quote requests on a static site by posting to somebody else's API."
wikipedia: "https://en.wikipedia.org/wiki/HTML_form"
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Forms Without a Backend

A plain HTML form posts to a third-party endpoint, which
emails you the submission. No server, no database.

## How it works

1. Sign up, get a public access key.
2. Put the key in a hidden input on the form.
3. Post to the provider's endpoint — or `fetch()` it for
   an in-page success message.
4. Submissions arrive by email, and optionally into a
   spreadsheet, Slack or a webhook.

The access key is public by design; it identifies the
destination, not the sender.

## Why it matters here

It is rung 3 of [[The Ladder]] and it is what keeps a
commercial catalog site on free static hosting. Quote
requests, contact forms and applications all work this way.

## The details that matter in practice

- **Spam.** A honeypot field catches most bots; add a
  captcha when it does not.
- **Redirect or AJAX.** Decide whether to send the user to
  a thank-you page or to stay put — both are supported.
- **Where submissions land.** An inbox is fine at low
  volume; route to a spreadsheet or webhook before you
  start losing them.

## Related

[[Web3Forms]] · [[Static Site Hosting]] ·
[[Catalog and Inventory Sites]] ·
[[Landing Page Email Capture]] · [[The Ladder]]

## Sources

- [[web3forms-docs]] · [[web3forms-getting-started]] ·
  [[web3forms-spam-protection]] ·
  [[web3forms-ajax-form-example]] ·
  [[web3forms-google-sheets]]
