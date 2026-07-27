---
type: Summary
title: "Twelve-Factor XI: Logs as event streams"
description: "Logs provide visibility into the behavior of a running app."
resource: "https://12factor.net/logs"
source_file: "Raw/01_foundations/12factor-logs.md"
tags: [foundations, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Twelve-Factor XI: Logs as event streams

Extractive digest of the immutable capture in
`Raw/01_foundations/12factor-logs.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://12factor.net/logs>

## Opening

> _Logs_ provide visibility into the behavior of a running app. In server-based environments they are commonly written to a file on disk (a “logfile”); but this is only an output format.
> Logs are the [stream](https://adam.herokuapp.com/past/2011/4/1/logs_are_streams_not_files/) of aggregated, time-ordered events collected from the output streams of all running processes and backing services. Logs in their raw form are typically a text format with one event per line (though ...
> In staging or production deploys, each process’ stream will be captured by the execution environment, collated together with all other streams from the app, and routed to one or more final destinations for viewing and long-term archival. These archival destinations are not visible to or ...
> The event stream for an app can be routed to a file, or watched via realtime tail in a terminal. Most significantly, the stream can be sent to a log indexing and analysis system such as [Splunk](http://www.splunk.com/), or a general-purpose data warehousing system such as ...

## Contents of the source document

  - XI. Logs
    - Treat logs as event streams

## Related pages

[[HTTP]] · [[Twelve-Factor App]]
