---
type: Summary
title: "Amazon SES — sending quotas and rate limits"
description: "Your Amazon SES account has a set of sending quotas that regulate the number of email messages that you can send and the rate at which you can send them."
resource: "https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html"
source_file: "Raw/06_product_patterns/aws-ses-sending-quotas.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — sending quotas and rate limits

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-sending-quotas.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html>

## Opening

> Your Amazon SES account has a set of sending quotas that regulate the number of email messages that you can send and the rate at which you can send them. Sending quotas benefit all Amazon SES customers because they help to maintain the trusted relationship between Amazon SES and email providers. ...
> The following quotas apply to sending email through Amazon SES:
> + [**Sending quota**](quotas.md)—The maximum number of emails that you can send in a 24-hour period. This quota is calculated on a rolling time period. Every time you try to send an email, Amazon SES determines the number of emails that you sent in the previous 24 hours. As long as the total number ...
> If sending a message would exceed the daily maximum for your account, your call to Amazon SES is rejected.

## Contents of the source document

- Managing your Amazon SES sending limits

## Related pages

[[Amazon SES]]
