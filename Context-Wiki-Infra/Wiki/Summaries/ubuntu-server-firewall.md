---
type: Summary
title: "Ubuntu Server — firewall (ufw / iptables)"
description: "The Linux kernel includes the netfilter subsystem, which is used to manipulate or decide the fate of network traffic headed into or through your server."
resource: "https://documentation.ubuntu.com/server/how-to/security/firewalls/"
source_file: "Raw/03_deployments/ubuntu-server-firewall.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Ubuntu Server — firewall (ufw / iptables)

Extractive digest of the immutable capture in
`Raw/03_deployments/ubuntu-server-firewall.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://documentation.ubuntu.com/server/how-to/security/firewalls/>

## Opening

> The Linux kernel includes the **[netfilter](https://netfilter.org/)** subsystem, which is used to manipulate or decide the fate of network traffic headed into or through your server. All modern Linux firewall solutions use this system for packet filtering.
> The kernel’s packet filtering system would be of little use to administrators without a userspace interface to manage it. This is the purpose of the **`iptables`** utility: when a packet reaches your server, it will be handed off to the netfilter subsystem for acceptance, manipulation, or rejection ...
> The default firewall configuration tool for Ubuntu is `ufw`. Developed to ease `iptables` firewall configuration, `ufw` provides a user-friendly way to create an IPv4 or IPv6 host-based firewall.
> `ufw` by default is initially disabled. From the _[ufw(8)](https://manpages.ubuntu.com/manpages/resolute/man8/ufw.8.html)_ manual page:

## Contents of the source document

- Firewall¶
  - ufw - Uncomplicated Firewall¶
    - Enable or disable ufw¶
    - Open or close a port¶
    - Add or remove a rule¶
    - Allow access from specific hosts¶
    - The --dry-run option¶
    - Check the status¶
    - ufw application integration¶
  - IP masquerading¶
    - IP masquerading with ufw¶
    - IP masquerading with iptables¶
  - Logs¶
  - Other tools¶
  - Further reading¶

## Related pages

[[HTTP]] · [[PostgreSQL]] · [[Ubuntu Server]]
