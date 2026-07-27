---
type: Service
title: "Web3Forms"
description: "A form endpoint for static sites - a public access key and no backend."
tags: [product-patterns]
timestamp: "2026-07-27T00:00:00Z"
---

# Web3Forms

Accepts HTML form submissions and emails them to you. No
account key on the server, no backend, no database.

## How it works

```html
<form action="https://api.web3forms.com/submit"
      method="POST">
  <input type="hidden" name="access_key"
         value="YOUR-PUBLIC-KEY">
  <input type="email" name="email" required>
  <textarea name="message"></textarea>
  <button>Send</button>
</form>
```

The access key is **public by design** — it identifies the
destination inbox, not the sender. Keeping it in a
`access_key.js` file in the repository is fine.

## The features worth using

- **Honeypot** field for spam, with captcha available when
  it is not enough.
- **Redirect** to a thank-you page, or `fetch()` it for an
  in-page confirmation.
- **Integrations** to Google Sheets, Slack, Discord and
  webhooks — which is how you stop losing submissions in
  an inbox.
- **Autoresponder** on paid plans, to acknowledge the
  sender immediately.

## Watch out for

Anyone can post to your endpoint with that key. Spam
protection is therefore not optional, and you should never
treat a submission as trusted input.

## Related

[[Forms Without a Backend]] · [[Static Site Hosting]] ·
[[Catalog and Inventory Sites]] ·
[[Landing Page Email Capture]]

## Sources

- [[web3forms-docs]] · [[web3forms-getting-started]] ·
  [[web3forms-spam-protection]] ·
  [[web3forms-redirection]] ·
  [[web3forms-ajax-form-example]] ·
  [[web3forms-google-sheets]] · [[web3forms-autoresponder]]
