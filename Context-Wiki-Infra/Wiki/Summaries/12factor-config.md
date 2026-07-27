---
type: Summary
title: "Twelve-Factor III: Config — store config in the environment"
description: "An app’s config is everything that is likely to vary between deploys (staging, production, developer environments, etc)."
resource: "https://12factor.net/config"
source_file: "Raw/01_foundations/12factor-config.md"
tags: [foundations, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Twelve-Factor III: Config — store config in the environment

Extractive digest of the immutable capture in
`Raw/01_foundations/12factor-config.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://12factor.net/config>

## Opening

> An app’s _config_ is everything that is likely to vary between [deploys](https://12factor.net/codebase) (staging, production, developer environments, etc). This includes:
> Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires **strict separation of config from code**. Config varies substantially across deploys, code does not.
> A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials.
> Note that this definition of “config” does **not** include internal application config, such as `config/routes.rb` in Rails, or how [code modules are connected](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/beans.html) in [Spring](http://spring.io/). This type of config ...

## Contents of the source document

  - III. Config
    - Store config in the environment

## Related pages

[[Amazon S3]] · [[HTTP]] · [[Twelve-Factor App]]
