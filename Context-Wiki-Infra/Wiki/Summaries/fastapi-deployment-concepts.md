---
type: Summary
title: "FastAPI — deployment concepts"
description: "When deploying a FastAPI application, or actually, any type of web API, there are several concepts that you probably care about, and using them you can find the most appropriate way to deplo"
resource: "https://fastapi.tiangolo.com/deployment/concepts/"
source_file: "Raw/07_playbooks/fastapi-deployment-concepts.md"
tags: [playbooks, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# FastAPI — deployment concepts

Extractive digest of the immutable capture in
`Raw/07_playbooks/fastapi-deployment-concepts.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://fastapi.tiangolo.com/deployment/concepts/>

## Opening

> When deploying a **FastAPI** application, or actually, any type of web API, there are several concepts that you probably care about, and using them you can find the **most appropriate** way to **deploy your application**.
> Some of the important concepts are:
> We'll see how they would affect **deployments**.
> In the end, the ultimate objective is to be able to **serve your API clients** in a way that is **secure** , to **avoid disruptions** , and to use the **compute resources** (for example remote servers/virtual machines) as efficiently as possible. 🚀

## Contents of the source document

- Deployments Concepts¶
  - Security - HTTPS¶
    - Example Tools for HTTPS¶
  - Program and Process¶
    - What is a Program¶
    - What is a Process¶
  - Running on Startup¶
    - In a Remote Server¶
    - Run Automatically on Startup¶
    - Separate Program¶
    - Example Tools to Run at Startup¶
  - Restarts¶
    - We Make Mistakes¶
    - Small Errors Automatically Handled¶
    - Bigger Errors - Crashes¶
    - Restart After Crash¶
    - Example Tools to Restart Automatically¶
  - Replication - Processes and Memory¶

## Related pages

[[Caddy]] · [[Certbot]] · [[Container Images]] · [[Docker]] · [[Docker Compose]] · [[FastAPI]] · [[Kubernetes]] · [[Nginx]] · [[systemd]]
