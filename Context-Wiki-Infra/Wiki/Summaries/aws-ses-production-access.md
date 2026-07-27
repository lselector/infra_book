---
type: Summary
title: "Amazon SES — moving out of the sandbox (request production access)"
description: "To help prevent fraud and abuse, and to help protect your reputation as a sender, we apply certain restrictions to new Amazon SES accounts."
resource: "https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html"
source_file: "Raw/06_product_patterns/aws-ses-production-access.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — moving out of the sandbox (request production access)

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-production-access.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html>

## Opening

> To help prevent fraud and abuse, and to help protect your reputation as a sender, we apply certain restrictions to new Amazon SES accounts.
> We place all new accounts in the Amazon SES *sandbox*. The sandbox status for your account is unique per each AWS Region. While your account is in the sandbox, you can use all of the features of Amazon SES. However, when your account is in the sandbox, we apply the following restrictions to your ...
> + You can only send mail **to** verified email addresses and domains, or to [the Amazon SES mailbox simulator](send-an-email-from-console.md#send-email-simulator).
> + You can send a maximum of 200 messages per 24-hour period.

## Contents of the source document

- Request production access (Moving out of the Amazon SES sandbox)

## Related pages

[[Amazon EC2]] · [[Amazon SES]] · [[Authorization]] · [[Transactional Email]]
