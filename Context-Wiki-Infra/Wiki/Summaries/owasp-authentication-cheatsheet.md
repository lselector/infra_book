---
type: Summary
title: "OWASP — authentication cheat sheet"
description: "The primary function of a User ID is to uniquely identify a user within a system."
resource: "https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"
source_file: "Raw/05_ops_cicd_security/owasp-authentication-cheatsheet.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP — authentication cheat sheet

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/owasp-authentication-cheatsheet.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>

## Opening

> The primary function of a User ID is to uniquely identify a user within a system. Ideally, User IDs should be randomly generated to prevent the creation of predictable or sequential IDs, which could pose a security risk, especially in systems where User IDs might be exposed or inferred from ...
> Usernames are easy-to-remember identifiers chosen by the user and used for identifying themselves when logging into a system or service. The terms User ID and username might be used interchangeably if the username chosen by the user also serves as their unique identifier within the system.
> Users should be permitted to use their email address as a username, provided the email is verified during sign-up. Additionally, they should have the option to choose a username other than an email address. For information on validating email addresses, please visit the [input validation cheat ...
> A key concern when using passwords for authentication is password strength. A "strong" password policy makes it difficult or even improbable for one to guess the password through either manual or automated means. The following characteristics define a strong password:

## Contents of the source document

- Authentication Cheat Sheet¶
  - Introduction¶
  - Authentication General Guidelines¶
    - User IDs¶
    - Usernames¶
    - Authentication Solution and Sensitive Accounts¶
    - Implement Proper Password Strength Controls¶
    - Implement Secure Password Recovery Mechanism¶
    - Store Passwords in a Secure Fashion¶
    - Compare Password Hashes Using Safe Functions¶
    - Change Password Feature¶
    - Transmit Passwords Only Over TLS or Other Strong Transport¶
    - Require Re-authentication for Sensitive Features¶
    - Re-authentication After Risk Events¶
    - Consider Strong Transaction Authentication¶
    - Authentication and Error Messages¶
    - Protect Against Automated Attacks¶
  - Logging and Monitoring¶

## Related pages

[[Authentication]] · [[Authorization]] · [[HTTP]] · [[Monitoring and Alerting]] · [[Multi-Factor Authentication]] · [[OWASP]]
