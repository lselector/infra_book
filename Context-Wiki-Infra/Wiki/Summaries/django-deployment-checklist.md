---
type: Summary
title: "Django — deployment checklist"
description: "The internet is a hostile environment. Before deploying your Django project, you should take some time to review your settings, with security, performance, and operations in mind."
resource: "https://docs.djangoproject.com/en/stable/howto/deployment/checklist/"
source_file: "Raw/07_playbooks/django-deployment-checklist.md"
tags: [playbooks, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# Django — deployment checklist

Extractive digest of the immutable capture in
`Raw/07_playbooks/django-deployment-checklist.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://docs.djangoproject.com/en/stable/howto/deployment/checklist/>

## Opening

> The internet is a hostile environment. Before deploying your Django project, you should take some time to review your settings, with security, performance, and operations in mind.
> Django includes many [security features](https://docs.djangoproject.com/en/stable/topics/security/). Some are built-in and always enabled. Others are optional because they aren’t always appropriate, or because they’re inconvenient for development. For example, forcing HTTPS may not be suitable for ...
> Performance optimizations are another category of trade-offs with convenience. For instance, caching is useful in production, less so for local development. Error reporting needs are also widely different.
> The following checklist includes settings that:

## Contents of the source document

- Deployment checklist¶
  - Run manage.py check --deploy¶
  - Switch away from manage.py runserver¶
  - Critical settings¶
    - SECRET_KEY¶
    - DEBUG¶
  - Environment-specific settings¶
    - ALLOWED_HOSTS¶
    - CACHES¶
    - DATABASES¶
    - EMAIL_BACKEND and related settings¶
    - STATIC_ROOT and STATIC_URL¶
    - MEDIA_ROOT and MEDIA_URL¶
  - HTTPS¶
    - CSRF_COOKIE_SECURE¶
    - SESSION_COOKIE_SECURE¶
  - Performance optimizations¶
    - Sessions¶

## Related pages

[[Authentication]] · [[Django]] · [[HTTP]] · [[Nginx]]
