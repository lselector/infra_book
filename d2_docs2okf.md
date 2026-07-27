# Tutorial: Converting a Document into OKF Format

This short guide shows how to take any existing document and turn it into an OKF-compliant Markdown concept that an AI agent can read and navigate. [web:10][web:12]

---

## 1. Understand the OKF building block

In OKF, **each file = one concept** (dataset, API, playbook, metric, procedure, etc.).  
Concept files are plain Markdown with a YAML front matter header at the top. [web:4][web:8]

Key ideas:

- Directory of `.md` files, each representing a single concept. [web:12]
- YAML front matter describes the concept (metadata). [web:4]
- Normal Markdown body holds the human-readable content. [web:8]

---

## 2. Choose the concept and filename

1. Read your source document and decide what single “thing” it describes best:
   - Example: “Customer events BigQuery table” → one concept.
   - Example: “On-call playbook” → one concept. [web:4]

2. Pick a stable filename that matches the concept:
   - `customer_events_table.md`
   - `oncall_playbook.md`  
   Place it inside your OKF bundle folder (e.g. `okf/` or `knowledge/`). [web:11]

---

## 3. Add required YAML front matter

At the very top of the file, add a YAML block between `---` lines.  
The **only required field** in OKF v0.1 is `type`. [web:8][web:12]

Minimal example:

```yaml
***
type: dataset
title: Customer events table
description: Event-level tracking table used for product analytics.
resource: bigquery://projects/acme-prod/datasets/analytics/tables/customer_events
tags:
  - analytics
  - events
  - product
***
```

Guidelines:

- `type`: required; broad category like `dataset`, `metric`, `api`, `playbook`, `runbook`, `system`, etc. [web:4][web:8]
- `title`: short human name for the concept.
- `description`: 1–3 sentence summary of what this concept is and why it matters.
- `resource`: pointer to the “real thing” (URL, DB path, repo path, etc.).
- `tags`: optional list to help agents and humans filter and group concepts. [web:11]

You can add more optional fields later if the spec introduces them; keep the header small and descriptive.

---

## 4. Convert the body into structured Markdown

Take the original document contents and rewrite them into **concise, scannable sections** in Markdown. [web:4]

Example structure for a dataset concept:

```markdown
## Purpose

Explain why this dataset exists and what questions it helps answer.

## Schema

- user_id: Unique user identifier.
- event_name: Name of the event.
- event_time: Timestamp in UTC.

## Usage notes

- Backfilled daily at 03:00 UTC.
- Only includes events from web and mobile apps.

## Related concepts

- [User profile table](../data/user_profile_table.md)
- [Analytics dashboard](../dashboards/product_analytics.md)
```

Tips:

- Prefer headings like `## Purpose`, `## Schema`, `## Usage notes`, `## Related concepts`.  
- Turn long prose into bullets, tables, or short paragraphs.  
- Use **relative Markdown links** to other OKF files to capture relationships. [web:4][web:8]

---

## 5. Add cross-links for navigation

OKF relies on normal Markdown links to create a graph of concepts. [web:4][web:8]

1. Identify other concepts your document mentions (tables, APIs, systems).
2. Link to them with relative paths:

```markdown
See also: [Events ingestion API](../apis/events_ingestion_api.md)
```

3. When you create those other concept files, link back where useful to form bidirectional navigation.

This makes it easy for agents to traverse from high-level overviews to specific entities on demand. [web:11]

---

## 6. Optional: create an index file

For a folder with many related concepts, add a simple index Markdown file that summarizes and links them. [web:5][web:11]

Example: `data/index.md`

```yaml
***
type: index
title: Analytics data assets
description: Overview of core analytics datasets and how they relate.
tags:
  - analytics
  - data
***
```

```markdown
## Core datasets

- [Customer events table](customer_events_table.md)
- [User profile table](user_profile_table.md)

## Metrics

- [Daily active users](../metrics/daily_active_users.md)
```

Indexes help agents start broad and drill down selectively, reducing token usage. [web:5][web:14]

---

## 7. Quick checklist for each converted document

Before you call a document “OKF-ready”:

- One file per concept (no giant multi-concept docs). [web:4][web:12]
- YAML front matter at top with at least `type`. [web:8][web:12]
- Clear `title`, short `description`, and a useful `resource`.
- Body structured into headings, bullets, and/or tables.
- Links to related concepts using relative Markdown links.
- Placed in an OKF bundle directory under version control (e.g. Git). [web:4][web:11]

---

## 8. Example end-to-end conversion pattern

**Input:**  
A 5-page internal doc called “Customer Events Table” with prose, screenshots, and random notes.

**Output OKF concept file (`customer_events_table.md`):**

1. Add YAML front matter with `type: dataset`, `title`, `description`, `resource`, `tags`. [web:8]
2. Convert narrative sections into `## Purpose`, `## Schema`, `## Data freshness`, `## Known issues`, `## Related concepts`.
3. Strip images/screenshots or replace them with text descriptions if needed.
4. Link to other tables, metrics, and dashboards with relative Markdown links.
5. Commit this file into your `okf/` or `knowledge/` directory. [web:11]

---
