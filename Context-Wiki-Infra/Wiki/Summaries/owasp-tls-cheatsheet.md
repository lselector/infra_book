---
type: Summary
title: "OWASP — transport layer security cheat sheet"
description: "This cheat sheet provides guidance on implementing transport layer protection for applications using Transport Layer Security (TLS)."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-tls-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — transport layer security cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-tls-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>

## Opening

> This cheat sheet provides guidance on implementing transport layer protection for applications using Transport Layer Security (TLS). It primarily focuses on how to use TLS to protect clients connecting to a web application over HTTPS, though much of this guidance is also applicable to other uses of ...
> Secure Socket Layer (SSL) was the original protocol that was used to provide encryption for HTTP traffic, in the form of HTTPS. There were two publicly released versions of SSL - versions 2 and 3. Both of these have serious cryptographic weaknesses and should no longer be used.
> For [various reasons](https://tim.dierks.org/2014/05/security-standards-and-name-changes-in.html) the next version of the protocol (effectively SSL 3.1) was named Transport Layer Security (TLS) version 1.0. Subsequently TLS versions 1.1, 1.2 and 1.3 have been released.
> The terms "SSL", "SSL/TLS" and "TLS" are frequently used interchangeably, and in many cases "SSL" is used when referring to the more modern TLS protocol. This cheat sheet will use the term "TLS" except where referring to the legacy protocols.

## Contents of the source document

- Transport Layer Security Cheat Sheet¶
  - Introduction¶
    - SSL vs TLS¶
  - Server Configuration¶
    - Only Support Strong Protocols¶
    - Only Support Strong Ciphers¶
    - Set the appropriate Diffie-Hellman groups¶
    - Disable Compression¶
    - Patch Cryptographic Libraries¶
    - Test the Server Configuration¶
  - Certificates¶
    - Use Strong Keys and Protect Them¶
    - Use Strong Cryptographic Hashing Algorithms¶
    - Use Correct Domain Names¶
    - Carefully Consider the use of Wildcard Certificates¶
    - Use an Appropriate Certification Authority for the Application's User Base¶
    - Use CAA Records to Restrict Which CAs can Issue Certificates¶
    - Consider the Certificate’s Validation Type¶

## Related pages

[[Authentication]] · [[Authorization]] · [[HTTP]] · [[Least Privilege]] · [[Nginx]] · [[OWASP]] · [[Reverse Proxy]]
