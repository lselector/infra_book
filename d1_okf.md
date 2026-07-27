# Open Knowledge Format (OKF)

## What is OKF?

**Open Knowledge Format (OKF)** is an open, vendor-neutral
specification from Google Cloud (launched June 12, 2026)
for representing knowledge — the metadata, context, and
curated insight that surrounds data and systems — in a form
that both humans and AI agents can directly read, navigate,
and update.

OKF is an open standard for the "LLM wiki" pattern
popularized by Andrej Karpathy: a curated, cross-linked
wiki handbook stored as plain files under version control.

In one sentence:

> **OKF v0.1 = a directory of Markdown files with YAML
> frontmatter, plus a small set of shared conventions.**

- Spec and tools: [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- Announcement: [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)

## Core ideas

1. **One file = one concept.** Each `.md` file describes a
   single "thing": a dataset, table, API, metric, playbook,
   system, procedure, etc.
2. **A bundle = a directory tree** of such files, organized
   however the producer likes, versioned in Git.
3. **YAML frontmatter** at the top of each file carries
   machine-readable metadata; the Markdown body carries the
   human-readable content.
4. **Plain Markdown links** between files form a navigable
   knowledge graph. Broken links are tolerated.
5. **No central schema registry, no special tooling** —
   any text editor, any agent, any Git host works.

## Frontmatter fields

Required:

| Field  | Meaning                                        |
|--------|------------------------------------------------|
| `type` | Short string naming the concept kind, e.g. `BigQuery Table`, `Playbook`. Not centrally registered; consumers must tolerate unknown types. |

Recommended (optional):

| Field         | Meaning                                  |
|---------------|------------------------------------------|
| `title`       | Display name (defaults to filename)      |
| `description` | Single-sentence summary                  |
| `resource`    | URI of the underlying real asset         |
| `tags`        | YAML list for filtering / grouping       |
| `timestamp`   | ISO 8601 datetime of last modification   |

Producers may add custom fields; consumers must preserve
unknown keys.

## Reserved filenames

| File       | Purpose                                       |
|------------|-----------------------------------------------|
| `index.md` | Directory listing for progressive disclosure — lets an agent start broad and drill down. **No frontmatter**; body is grouped Markdown lists of links. |
| `log.md`   | Chronological update history for the bundle.  |

All other `.md` files are concept documents.

## Body conventions

Standard Markdown, with optional conventional headings:

- `# Schema` — structured description of fields / columns
- `# Examples` — usage examples
- `# Citations` — external sources

## Linking

- **Bundle-absolute** (recommended): starts with `/`,
  resolved from the bundle root, e.g.
  `[customers](/tables/customers.md)`
- **Relative**: normal Markdown relative paths, e.g.
  `[customers](../tables/customers.md)`

Links assert untyped relationships between concepts.

## Example 1: a concept file

`tables/orders.md`

```markdown
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders]
timestamp: 2026-05-28T00:00:00Z
---

# Schema

| Column        | Type    | Description                              |
|---------------|---------|------------------------------------------|
| `order_id`    | STRING  | Unique identifier.                       |
| `customer_id` | STRING  | FK to [customers](/tables/customers.md). |
| `total_usd`   | NUMERIC | Order total in USD.                      |

# Examples

    SELECT COUNT(*) FROM sales.orders
    WHERE DATE(created_at) = CURRENT_DATE()
```

## Example 2: a playbook concept

`playbooks/oncall.md`

```markdown
---
type: Playbook
title: On-call playbook
description: Steps for handling production incidents.
tags: [ops, incidents]
---

# Steps

1. Acknowledge the page in [PagerDuty](/systems/pagerduty.md).
2. Check the [service dashboard](/dashboards/service_health.md).
3. Escalate per the [escalation policy](/playbooks/escalation.md).
```

## Example 3: an index file

`index.md` (bundle root — note: **no frontmatter**)

```markdown
# Tables

* [Orders](/tables/orders.md) - One row per completed order.
* [Customers](/tables/customers.md) - Customer master data.

# Playbooks

* [On-call](/playbooks/oncall.md) - Incident handling steps.
```

## Conformance

A bundle conforms to OKF v0.1 if every non-reserved `.md`
file has parseable YAML frontmatter with a non-empty
`type`. Everything else is soft guidance: consumers must
tolerate missing optional fields, unknown types, and
broken links.

## See also

- [d2_docs2okf.md](d2_docs2okf.md) — tutorial on converting
  an existing document into an OKF concept file.
