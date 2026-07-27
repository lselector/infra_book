---
type: Summary
title: "Twelve-Factor IV: Backing services as attached resources"
description: "A backing service is any service the app consumes over the network as part of its normal operation."
resource: "https://12factor.net/backing-services"
source_file: "Raw/01_foundations/12factor-backing-services.md"
tags: [foundations, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Twelve-Factor IV: Backing services as attached resources

Extractive digest of the immutable capture in
`Raw/01_foundations/12factor-backing-services.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://12factor.net/backing-services>

## Opening

> A _backing service_ is any service the app consumes over the network as part of its normal operation. Examples include datastores (such as [MySQL](http://dev.mysql.com/) or [CouchDB](http://couchdb.apache.org/)), messaging/queueing systems (such as [RabbitMQ](http://www.rabbitmq.com/) or ...
> Backing services like the database are traditionally managed by the same systems administrators who deploy the app’s runtime. In addition to these locally-managed services, the app may also have services provided and managed by third parties. Examples include SMTP services (such as ...
> Each distinct backing service is a _resource_. For example, a MySQL database is a resource; two MySQL databases (used for sharding at the application layer) qualify as two distinct resources. The twelve-factor app treats these databases as _attached resources_ , which indicates their loose coupling ...
> Resources can be attached to and detached from deploys at will. For example, if the app’s database is misbehaving due to a hardware issue, the app’s administrator might spin up a new database server restored from a recent backup. The current production database could be detached, and the new ...

## Contents of the source document

  - IV. Backing services
    - Treat backing services as attached resources

## Related pages

[[Amazon RDS]] · [[Amazon S3]] · [[HTTP]] · [[Postmark]] · [[RabbitMQ]] · [[Twelve-Factor App]]
