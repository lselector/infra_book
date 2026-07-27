---
type: Summary
title: "Amazon SES — sending via the SMTP interface"
description: "To send production email through Amazon SES, you can use the Simple Mail Transfer Protocol (SMTP) interface or the Amazon SES API."
resource: "https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html"
source_file: "Raw/06_product_patterns/aws-ses-smtp.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — sending via the SMTP interface

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-smtp.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html>

## Opening

> To send production email through Amazon SES, you can use the Simple Mail Transfer Protocol (SMTP) interface or the Amazon SES API. For more information about the Amazon SES API, see [Using the Amazon SES API to send email](send-email-api.md). This section describes the SMTP interface.
> Amazon SES sends email using SMTP, which is the most common email protocol on the internet. You can send email through Amazon SES by using a variety of SMTP-enabled programming languages and software to connect to the Amazon SES SMTP interface. This section explains how to get your Amazon SES SMTP ...
> For solutions to common problems that you might encounter when you use Amazon SES through its SMTP interface, see [Amazon SES SMTP issues](troubleshoot-smtp.md).
> To send email using the Amazon SES SMTP interface, you need the following:

## Contents of the source document

- Using the Amazon SES SMTP interface to send email
  - Requirements to send email over SMTP
  - Methods to send email over SMTP
  - Email information to provide

## Related pages

[[Amazon SES]]
