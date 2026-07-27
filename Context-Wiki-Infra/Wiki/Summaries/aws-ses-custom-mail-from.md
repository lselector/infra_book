---
type: Summary
title: "Amazon SES — using a custom MAIL FROM domain (SPF alignment, MX record)"
description: "When an email is sent, it has two addresses that indicate its source: a From address that's displayed to the message recipient, and a MAIL FROM address that indicates where the message origi"
resource: "https://docs.aws.amazon.com/ses/latest/dg/mail-from.html"
source_file: "Raw/06_product_patterns/aws-ses-custom-mail-from.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — using a custom MAIL FROM domain (SPF alignment, MX record)

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-custom-mail-from.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/mail-from.html>

## Opening

> When an email is sent, it has two addresses that indicate its source: a From address that's displayed to the message recipient, and a MAIL FROM address that indicates where the message originated. The MAIL FROM address is sometimes called the *envelope sender*, *envelope from*, *bounce address*, or ...
> Amazon SES sets the MAIL FROM domain for the messages that you send to a default value unless you specify your own (custom) domain. This section discusses the benefits of setting up a custom MAIL FROM domain, and includes setup procedures.
> Messages that you send through Amazon SES automatically use a subdomain of `amazonses.com` as the default MAIL FROM domain. Sender Policy Framework (SPF) authentication successfully validates these messages because the default MAIL FROM domain matches the application that sent the email—in this ...
> If you don't want to use the SES default MAIL FROM domain, and would rather use a subdomain of a domain that you own, this is referred to in SES as using a *custom* MAIL FROM domain. To do this, it requires you to publish your own SPF record for your custom MAIL FROM domain. In addition, SES also ...

## Contents of the source document

- Using a custom MAIL FROM domain
  - Why use a custom MAIL FROM domain?
  - Choosing a custom MAIL FROM domain
  - Using SPF with your custom MAIL FROM domain
  - Configuring your custom MAIL FROM domain
    - Setting up a custom MAIL FROM domain for a verified domain
    - Setting up a custom MAIL FROM domain for a verified email address
  - Custom MAIL FROM domain setup states with Amazon SES

## Related pages

[[Amazon SES]] · [[Authentication]] · [[HTTP]]
