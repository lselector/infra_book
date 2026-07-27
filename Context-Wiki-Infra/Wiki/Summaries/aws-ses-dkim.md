---
type: Summary
title: "Amazon SES — DKIM signing (Easy DKIM, BYODKIM)"
description: "DKIM signatures are optional. You might decide to sign your email using a DKIM signature to enhance deliverability with DKIM-compliant email providers."
resource: "https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html"
source_file: "Raw/06_product_patterns/aws-ses-dkim.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — DKIM signing (Easy DKIM, BYODKIM)

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-dkim.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html>

## Opening

> DKIM signatures are optional. You might decide to sign your email using a DKIM signature to enhance deliverability with DKIM-compliant email providers. Amazon SES provides three options for signing your messages using a DKIM signature:
> + **Easy DKIM**: SES generates a public-private key pair and automatically adds a DKIM signature to every message that you send from that identity, see [Easy DKIM in Amazon SES](send-email-authentication-dkim-easy.md).
> + **Deterministic Easy DKIM (DEED)**: Enables you to maintain consistent DKIM signing across multiple AWS Regions by creating replica identities that automatically inherit the DKIM signing attributes as a parent identity that is using Easy DKIM, see [Using Deterministic Easy DKIM (DEED) in Amazon ...
> + **BYODKIM (Bring Your Own DKIM)**: You provide your own public-private key pair and SES adds a DKIM signature to every message that you send from that identity, see [Provide your own DKIM authentication token (BYODKIM) in Amazon SES](send-email-authentication-dkim-bring-your-own.md).

## Contents of the source document

- Authenticating Email with DKIM in Amazon SES
  - DKIM signing key length
  - DKIM considerations
  - Understanding inherited DKIM signing properties

## Related pages

[[Amazon SES]] · [[Authentication]]
