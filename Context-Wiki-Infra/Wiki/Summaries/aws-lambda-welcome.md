---
type: Summary
title: "AWS Lambda — developer guide introduction"
description: "AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers."
resource: "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"
source_file: "Raw/03_deployments/aws-lambda-welcome.md"
tags: [deployments, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# AWS Lambda — developer guide introduction

Extractive digest of the immutable capture in
`Raw/03_deployments/aws-lambda-welcome.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>

## Opening

> AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. Lambda automatically manages the underlying infrastructure – including server maintenance, capacity provisioning, scaling, and patching – so you can focus on your application logic.
> Lambda provides two compute primitives, each designed for different workload patterns:
> + **[Lambda Functions](lambda-functions-chapter.md)** – Run code in response to events or API calls without managing servers. You write a handler function, connect it to a trigger (API Gateway, Amazon S3, Amazon SQS, EventBridge, and 200\+ other AWS services), and Lambda executes it. Each ...
> + **[Lambda MicroVMs](lambda-microvms-guide.md)** – Isolated compute environments with near-instant startup and state retention for up to 8 hours. Designed for workloads needing a dedicated compute environment for each individual user or job. Lambda manages isolation, capacity, and networking. Your ...

## Contents of the source document

- What is AWS Lambda?
  - How Lambda Functions and Lambda MicroVMs compare

## Related pages

[[AWS Lambda]] · [[Amazon S3]]
