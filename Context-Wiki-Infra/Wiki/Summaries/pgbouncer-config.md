---
type: Summary
title: "PgBouncer — connection pooling configuration"
description: "The configuration file is in “ini” format."
resource: "https://www.pgbouncer.org/config.html"
source_file: "Raw/08_scaling_maturity/pgbouncer-config.md"
tags: [scaling, summary]
timestamp: "2026-07-27T00:00:00Z"
---

# PgBouncer — connection pooling configuration

Extractive digest of the immutable capture in
`Raw/08_scaling_maturity/pgbouncer-config.md`
(retrieved 2026-07-27).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://www.pgbouncer.org/config.html>

## Opening

> The configuration file is in “ini” format. Section names are between “[” and “]”. Lines starting with “;” or “#” are taken as comments and ignored. The characters “;” and “#” are not recognized as special when they appear later in the line.
> Specifies the log file. For daemonization (`-d`), either this or `syslog` need to be set.
> The log file is kept open, so after rotation, `kill -HUP` or on console `RELOAD;` should be done. On Windows, the service must be stopped and started.
> Note that setting `logfile` does not by itself turn off logging to stderr. Use the command-line option `-q` or `-d` for that.

## Contents of the source document

- pgbouncer.ini
  - Description
  - Generic settings
    - logfile
    - pidfile
    - listen_addr
    - listen_port
    - unix_socket_dir
    - unix_socket_mode
    - unix_socket_group
    - user
    - pool_mode
    - max_client_conn
    - default_pool_size
    - min_pool_size
    - reserve_pool_size
    - reserve_pool_timeout
    - max_db_connections

## Related pages

[[Authentication]] · [[Connection Pooling]] · [[Load Balancing]] · [[PgBouncer]] · [[PostgreSQL]]
