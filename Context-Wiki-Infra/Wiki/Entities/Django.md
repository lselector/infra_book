---
type: Tool
title: "Django"
description: "Batteries-included Python framework - admin, ORM and auth out of the box."
tags: [deployments, application]
timestamp: "2026-07-27T00:00:00Z"
---

# Django

A full-stack Python framework that ships with an ORM,
migrations, an authentication system and an automatic
admin interface.

## Why it appears here

The admin site alone is often the reason. For an internal
tool or a catalog with a back office, Django gives you a
usable CRUD interface over your models on day one — work
that would otherwise take weeks.

## The deployment checklist matters

Django publishes an explicit production checklist, and it
exists because the development defaults are deliberately
unsafe:

- `DEBUG = False` — leaving it on exposes tracebacks,
  settings and often secrets.
- `SECRET_KEY` from the environment, never committed —
  [[Secrets Management]].
- `ALLOWED_HOSTS` set.
- `SECURE_HSTS_SECONDS`, secure cookies, HTTPS redirect —
  [[Security Headers]].

Run `manage.py check --deploy` before launch and again in
[[Continuous Integration and Delivery]].

## Related

[[Monolithic Web App]] · [[FastAPI]] · [[PostgreSQL]] ·
[[Security Headers]] · [[Secrets Management]]

## Sources

- [[django-deployment-checklist]] ·
  [[fastapi-run-server-manually]]
