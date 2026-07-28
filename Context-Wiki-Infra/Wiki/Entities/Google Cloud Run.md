---
type: Tool
title: "Google Cloud Run"
description: "Give it a container image, get an autoscaling HTTPS service that scales to zero - the least-effort container host."
wikipedia: "https://en.wikipedia.org/wiki/Google_Cloud_Platform"
tags: [deployments, serverless, tooling]
timestamp: "2026-07-28T00:00:00Z"
---

# Google Cloud Run

A managed platform that runs a container image as an
HTTPS service, scaling from zero to many instances on
request volume and back down again. You supply an image
that listens on `$PORT`; Google supplies the URL, the
certificate, the load balancing and the autoscaling.

## Why it is worth knowing about

It sits in a useful gap. [[AWS Lambda]] wants your code
in its packaging model; [[Kubernetes]] wants you to
operate a cluster. Cloud Run takes the artifact you
already build for [[Docker]] and runs it with no cluster
to manage — the shortest path from a `Dockerfile` to a
production URL that still scales to zero.

```bash
gcloud run deploy myapp --source .    # builds and deploys
```

## What you get

- **Scale to zero**, so an idle service costs nothing but
  storage for the image.
- **Concurrency > 1 per instance** — unlike function
  platforms, one instance handles many simultaneous
  requests, which is far kinder to database connections
  ([[Connection Pooling]]).
- **`--min-instances 1`** to remove [[Cold Starts]]
  entirely for a few dollars a month.
- Request-based or instance-based billing, jobs for
  batch work, and direct integration with Cloud SQL and
  [[Google Secret Manager]].

## Where it fits on the ladder

Rung 11 in [[Stacks]] — the "containers and a scheduler"
rung — for teams already on Google Cloud, alongside
[[AWS Fargate]] on AWS and [[Fly.io]] as the
independent option. For a single small app, a VPS with
[[Docker Compose]] behind [[Caddy]] is still cheaper and
simpler ([[One-Box Deployment]]); Cloud Run earns its
place when traffic is spiky or you want no machines at
all.

## Watch out for

- **Stateless containers only.** The filesystem is
  ephemeral; persistent state goes to Cloud SQL,
  [[Object Storage]] or a volume mount.
- **Request timeout** caps long operations — push those
  to Cloud Run jobs or a queue
  ([[Message Queues]]).
- **Egress and image storage are billed separately** from
  compute, which is where surprise costs live
  ([[Cost Control]]).
- **Vendor coupling is low** — it is a container image
  with a `PORT` — which is a real argument in its favour
  compared with function-shaped platforms.

## Related

[[Serverless Architecture]] · [[Micro-VMs]] ·
[[Cold Starts]] · [[Docker]] · [[Container Images]] ·
[[AWS Fargate]] · [[AWS Lambda]] · [[Fly.io]] ·
[[Managed PaaS]] · [[Kubernetes]] ·
[[Container Orchestration]] · [[Google Secret Manager]]

## Sources

- [[gcp-iaas-paas-saas]] ·
  [[gcp-architecture-framework]] · [[aws-ecs-fargate]] ·
  [[aws-what-is-serverless]]. Upstream documentation
  (<https://cloud.google.com/run/docs>) is not part of
  the downloaded `Raw/` corpus.
