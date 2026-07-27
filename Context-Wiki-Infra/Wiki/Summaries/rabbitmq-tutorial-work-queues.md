---
type: Summary
title: "RabbitMQ — work queues tutorial (Python)"
description: "info This tutorial assumes RabbitMQ is installed and running on localhost on the standard port (5672)."
resource: "https://www.rabbitmq.com/tutorials/tutorial-two-python"
source_file: "Raw/04_network_storage_db/rabbitmq-tutorial-work-queues.md"
tags: [storage-and-databases, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# RabbitMQ — work queues tutorial (Python)

Extractive digest of the immutable capture in
`Raw/04_network_storage_db/rabbitmq-tutorial-work-queues.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.rabbitmq.com/tutorials/tutorial-two-python>

## Opening

> info
> This tutorial assumes RabbitMQ is [installed](https://www.rabbitmq.com/docs/download) and running on `localhost` on the [standard port](https://www.rabbitmq.com/docs/networking#ports) (5672). In case you use a different host, port or credentials, connections settings would require adjusting.
> If you're having trouble going through this tutorial you can contact us through [GitHub Discussions](https://github.com/rabbitmq/rabbitmq-server/discussions) or [RabbitMQ community Discord](https://www.rabbitmq.com/discord).
> As with other Python tutorials, we will use the [Pika](https://pypi.python.org/pypi/pika) RabbitMQ client [version 1.0.0](https://pika.readthedocs.io/en/stable/).

## Contents of the source document

  - Work Queues​
    - (using the Pika Python client)​")
    - Prerequisites​
    - Where to get help​
    - Prerequisites​
    - What This Tutorial Focuses On​
  - Round-robin dispatching​
  - Message acknowledgment​
  - Message durability​
  - Fair dispatch​
  - Putting it all together​

## Related pages

[[HTTP]] · [[RabbitMQ]]
