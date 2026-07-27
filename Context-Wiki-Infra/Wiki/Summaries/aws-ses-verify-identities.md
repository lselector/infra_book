---
type: Summary
title: "Amazon SES — creating and verifying sender identities (domain, email)"
description: "In Amazon SES, you can create an identity at the domain level or you can create an email address identity."
resource: "https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html"
source_file: "Raw/06_product_patterns/aws-ses-verify-identities.md"
tags: [product-patterns, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Amazon SES — creating and verifying sender identities (domain, email)

Extractive digest of the immutable capture in
`Raw/06_product_patterns/aws-ses-verify-identities.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html>

## Opening

> In Amazon SES, you can create an identity at the domain level or you can create an email address identity. These identity types aren’t mutually exclusive. In most cases, creating a domain identity eliminates the need for creating and verifying individual email address identities, unless you want to ...
> Creating and verifying an email address identity is the fastest way to get started in SES, but there are benefits to verifying an identity at the domain level. When you verify an email address identity, only that email address can be used to send mail, but when you verify a domain identity, you can ...
> However, keep in mind that an email address identity that's using the inherited verification from its domain is limited to straightforward email sending. If you want to do more advanced sending, you'll have to also explicitly verify it as an email address identity. Advanced sending includes using ...
> To help clarify the verification inheritance and email sending capabilities discussed above, the following table categorizes each combination of domain/email address verification and lists the inheritance, sending level, and display status for each:

## Contents of the source document

- Creating and verifying identities in Amazon SES
  - Creating a domain identity
  - Verifying a DKIM domain identity with your DNS provider
    - Troubleshooting domain verification
  - Creating an email address identity
  - Verifying an email address identity
    - Troubleshooting email address verification
  - Create and verify an identity and assign a default configuration set at the same time
  - Using custom verification email templates
    - Creating a custom verification email template
    - Editing a custom verification email template
    - Sending verification emails using custom templates
    - Custom verification email frequently asked questions

## Related pages

[[Amazon SES]] · [[Authentication]] · [[Cloudflare]] · [[Email Authentication]] · [[HTTP]] · [[Resend]]
