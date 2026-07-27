---
type: Summary
title: "Amazon SES — SPF and custom MAIL FROM domain"
description: "Messages that you send through Amazon SES automatically use a subdomain of amazonses.com as the default MAIL FROM domain."
resource: "https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-spf.html"
source_file: "Raw/06_product_patterns/aws-ses-spf.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — SPF and custom MAIL FROM domain

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-spf.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-spf.html>

## Opening

> Messages that you send through Amazon SES automatically use a subdomain of `amazonses.com` as the default MAIL FROM domain. SPF authentication successfully validates these messages because the default MAIL FROM domain matches the application that sent the email—in this case, SES. Therefore, in SES, ...
> However, if you don't want to use the SES default MAIL FROM domain, and would rather use a subdomain of a domain that you own, this is referred to in SES as using a *custom* MAIL FROM domain. To do this, it requires you to publish your own SPF record for your custom MAIL FROM domain. In addition, ...
> Instructions are given for configuring your domain with SPF and how to publish the MX and SPF (type TXT) records in [Using a custom MAIL FROM domain](mail-from.md).

## Contents of the source document

- Authenticating Email with SPF in Amazon SES

## Related pages

[[Amazon SES]] · [[Authentication]]
