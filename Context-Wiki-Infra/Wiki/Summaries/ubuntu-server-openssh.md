---
type: Summary
title: "Ubuntu Server — OpenSSH server setup and key auth"
description: "OpenSSH is a powerful collection of tools for remotely controlling networked computers and transferring data between them."
resource: "https://documentation.ubuntu.com/server/how-to/security/openssh-server/"
source_file: "Raw/03_deployments/ubuntu-server-openssh.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Ubuntu Server — OpenSSH server setup and key auth

Extractive digest of the immutable capture in
`Raw/03_deployments/ubuntu-server-openssh.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>

## Opening

> OpenSSH is a powerful collection of tools for remotely controlling networked computers and transferring data between them. Here we’ll describe some of the configuration settings possible with the OpenSSH server application and how to change them on your Ubuntu system.
> OpenSSH is a freely available version of the Secure Shell (SSH) protocol family of tools. Traditional tools, such as `telnet` or `rcp`, are insecure and transmit the user’s password in cleartext when used. OpenSSH provides a server daemon and client tools to facilitate secure, encrypted, remote ...
> The OpenSSH server component, `sshd`, listens continuously for client connections from any of the client tools. When a connection request occurs, `sshd` sets up the correct connection depending on the type of client tool connecting. For example, if the remote computer is connecting with the SSH ...
> OpenSSH can use many authentication methods, including plain password, public key cryptography, and Kerberos tickets.

## Contents of the source document

- OpenSSH server¶
  - Install OpenSSH¶
  - Configure OpenSSH¶
    - Example configuration directive¶
    - Disable OS information disclosure through service banner¶
  - SSH keys¶
  - Connection multiplexing¶
  - Import keys from public keyservers¶
  - Two factor authentication¶
  - Handling unstable connections¶
  - Further reading¶

## Related pages

[[Authentication]] · [[HTTP]] · [[Ubuntu Server]]
