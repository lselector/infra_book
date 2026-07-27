---
type: Summary
title: "Amazon SES — event publishing (bounces, complaints, deliveries)"
description: "To enable you to track your email sending at a granular level, you can set up Amazon SES to publish email sending events to Amazon CloudWatch, Amazon Data Firehose, Amazon Pinpoint, Amazon S"
resource: "https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html"
source_file: "Raw/06_product_patterns/aws-ses-event-publishing.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — event publishing (bounces, complaints, deliveries)

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-event-publishing.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html>

## Opening

> To enable you to track your email sending at a granular level, you can set up Amazon SES to publish *email sending events* to Amazon CloudWatch, Amazon Data Firehose, Amazon Pinpoint, Amazon Simple Notification Service, or Amazon EventBridge based on characteristics that you define.
> You can track several types of email sending events, including sends, deliveries, opens, clicks, bounces, complaints, rejections, rendering failures, and delivery delays. This information can be useful for operational and analytical purposes. For example, you can publish your email sending data to ...
> To use event publishing, you first set up one or more *configuration sets*. A configuration set specifies where to publish your events and which events to publish. Then, each time you send an email, you provide the name of the configuration set and one or more *message tags*, in the form of ...
> Depending on which email sending interface you use, you either provide the message tag as a parameter to the ...

## Contents of the source document

- Monitor email sending using Amazon SES event publishing
  - How event publishing works with configuration sets and message tags
  - Fine-grained feedback for email campaigns
  - How to use event publishing
  - Event publishing terminology

## Related pages

[[Amazon SES]]
