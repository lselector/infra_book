---
type: Summary
title: "Ubuntu Server — automatic (unattended) security updates"
description: "Ubuntu will apply security updates automatically, without user interaction."
resource: "https://documentation.ubuntu.com/server/how-to/software/automatic-updates/"
source_file: "Raw/03_deployments/ubuntu-automatic-updates.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Ubuntu Server — automatic (unattended) security updates

Extractive digest of the immutable capture in
`Raw/03_deployments/ubuntu-automatic-updates.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://documentation.ubuntu.com/server/how-to/software/automatic-updates/>

## Opening

> Ubuntu will apply security updates automatically, without user interaction. This is done via the `unattended-upgrades` package, which is installed by default.
> But as the name suggests, it can apply other types of updates, and with interesting options alongside. For example:
> And more. Let’s explore some of these options.
> Important

## Contents of the source document

- Automatic updates¶
  - Configuration layout¶
  - Enabling and disabling unattended upgrades¶
  - Where to pick updates from¶
    - Automatic upgrades from a PPA¶
  - How to block certain packages¶
  - Notifications¶
    - Notification examples¶
  - Reboots¶
  - Service restarts¶
  - When to consider disabling automatic updates¶
    - Systems which just get recreated¶
    - Manual steps required¶
    - Too much of a risk¶
    - Fleet management¶
  - Postponable updates¶
    - Prompt duration¶
    - Who can postpone¶

## Related pages

[[Authorization]] · [[HTTP]] · [[Ubuntu Server]] · [[Unattended Upgrades]] · [[systemd]]
