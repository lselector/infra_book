---
type: Concept
title: "Poison Message"
description: "One message the consumer can never process - and the infinite retry loop that stops the whole queue."
wikipedia: "https://en.wikipedia.org/wiki/Poison_message"
tags: [ops-and-security, reliability, architectures]
timestamp: "2026-07-28T00:00:00Z"
---

# Poison Message

A message that fails every time it is processed. The
consumer crashes or throws, the broker redelivers it, and
the loop repeats — burning capacity, filling logs, and on
an ordered queue blocking everything behind it. Failure
mode 9 of [[Failure Modes]].

## What poisons a message

- A field that is null, or a type that changed
  (`"1"` where `1` was expected).
- A referenced row that has since been deleted.
- A payload from a newer producer version that the
  consumer does not understand.
- Something huge — an oversized attachment that OOMs the
  worker.
- A malicious or malformed payload from an untrusted
  producer.

It is rarely a broker problem. It is a **contract
problem** between producer and consumer.

## The fix: a dead-letter queue

Count delivery attempts, and after N (3 is a good
default) move the message to a **dead-letter queue**
instead of retrying forever. The main queue keeps
flowing; the bad message waits somewhere you can inspect
it.

```text
main queue --(3 failures)--> DLQ --> a human, or a
                                     fixed consumer
```

Three rules make a DLQ useful rather than a landfill:

1. **Alert on it.** A DLQ nobody looks at is a silent
   data-loss channel. Alert on depth > 0.
2. **Keep the failure reason** — the exception, the
   attempt count, the consumer version — with the
   message. Without it, triage means guessing.
3. **Be able to replay.** Once the bug is fixed, you
   need one command to put messages back on the main
   queue. Write it before you need it, at 3am.

## Distinguish "poison" from "transient"

Retrying is correct for a network blip and pointless for
a schema mismatch. If you can tell them apart in code, do
— fail fast and dead-letter on a parse or validation
error, retry with backoff on a timeout or a 503. Treating
everything as transient is what produces the infinite
loop; treating everything as poison discards work that
would have succeeded.

## Prevention

- **Validate at the producer.** A message that never
  enters the queue cannot poison it.
- **Version the payload schema** and make consumers
  tolerant of unknown fields.
- **Cap message size**, and put large bodies in
  [[Object Storage]] with only a reference in the queue.
- **Make handlers idempotent** ([[Idempotency]]) — a
  replayed DLQ message will be processed again, possibly
  after a partial success.

## Watch out for

**A poison message can look like a [[Queue Backlog]].**
The queue grows, consumers are busy, throughput is zero —
because all of it is being spent on one message being
redelivered. Check the redelivery count before adding
consumers.

## Related

[[Failure Modes]] · [[Queue Backlog]] ·
[[Duplicate Processing]] · [[Idempotency]] ·
[[Message Queues]] · [[RabbitMQ]] ·
[[Event-Driven Architecture]] · [[Object Storage]] ·
[[Monitoring and Alerting]] · [[Incident Response]]

## Sources

- [[rabbitmq-tutorial-work-queues]] ·
  [[aws-well-architected-reliability]] ·
  [[owasp-input-validation-cheatsheet]]
