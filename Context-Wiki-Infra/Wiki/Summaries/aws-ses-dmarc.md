---
type: Summary
title: "Amazon SES — complying with DMARC"
description: "Domain-based Message Authentication, Reporting and Conformance (DMARC) is an email authentication protocol that uses Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) to de"
resource: "https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dmarc.html"
source_file: "Raw/06_product_patterns/aws-ses-dmarc.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — complying with DMARC

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-dmarc.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dmarc.html>

## Opening

> Domain-based Message Authentication, Reporting and Conformance (DMARC) is an email authentication protocol that uses Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) to detect email spoofing and phishing. In order to comply with DMARC, messages must be authenticated through ...
> Let's briefly review which each does and how DMARC ties them all together:
> +  **SPF** – Identifies which mail servers are allowed to send mail on behalf of your custom MAIL FROM domain through a DNS TXT record that is used by DNS. Recipient mail systems refer to the SPF TXT record to determine whether a message from your custom domain comes from an authorized messaging ...
> +  **DKIM** – Adds a digital signature to your outbound messages in the email header. Receiving email systems can use this digital signature to help verify whether incoming email is signed by a key owned by the domain. However, when a receiving email system forwards a message, the message's ...

## Contents of the source document

- Complying with DMARC authentication protocol in Amazon SES
  - Setting up the DMARC policy on your domain
  - Best practices for implementing DMARC
  - Complying with DMARC through SPF
  - Complying with DMARC through DKIM

## Related pages

[[Amazon SES]] · [[Authentication]] · [[Email Authentication]]
