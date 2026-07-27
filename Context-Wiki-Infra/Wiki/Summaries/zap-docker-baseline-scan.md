---
type: Summary
title: "OWASP ZAP — automated baseline scan in Docker / CI"
description: "The ZAP Baseline scan is a script that is available in the ZAP Docker images."
resource: "https://www.zaproxy.org/docs/docker/baseline-scan/"
source_file: "Raw/05_ops_cicd_security/zap-docker-baseline-scan.md"
tags: [ops-and-security, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# OWASP ZAP — automated baseline scan in Docker / CI

Extractive digest of the immutable capture in
`Raw/05_ops_cicd_security/zap-docker-baseline-scan.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.zaproxy.org/docs/docker/baseline-scan/>

## Opening

> The ZAP Baseline scan is a script that is available in the ZAP [Docker](https://www.zaproxy.org/docs/docker/about/) images.
> It runs the ZAP spider against the specified target for (by default) 1 minute and then waits for the passive scanning to complete before reporting the results.
> This means that the script doesn’t perform any actual ‘attacks’ and will run for a relatively short period of time (a few minutes at most).
> By default it reports all alerts as WARNings but you can specify a config file which can change any rules to FAIL or IGNORE.

## Contents of the source document

    - Usage [](https://www.zaproxy.org/docs/docker/baseline-scan/#usage)
    - Example Output [](https://www.zaproxy.org/docs/docker/baseline-scan/#example-output)
    - Exit Value [](https://www.zaproxy.org/docs/docker/baseline-scan/#exit-value)
    - Progress File [](https://www.zaproxy.org/docs/docker/baseline-scan/#progress-file)
    - ZAP Parameters [](https://www.zaproxy.org/docs/docker/baseline-scan/#zap-parameters)
    - Mass Baseline [](https://www.zaproxy.org/docs/docker/baseline-scan/#mass-baseline)
    - Scan Hooks [](https://www.zaproxy.org/docs/docker/baseline-scan/#scan-hooks)
    - Source Code [](https://www.zaproxy.org/docs/docker/baseline-scan/#source-code)

## Related pages

[[Authentication]] · [[Docker]] · [[HTTP]] · [[OWASP]] · [[OWASP ZAP]]
