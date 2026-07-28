# Raw Sources Registry

Source URL for every file in `Raw/`. Files
in `Raw/` are immutable — never edit them;
re-download from the URL if needed.

Format: `filename | title | source URL`

## 01_foundations — thinking about infrastructure

- `12factor-backing-services.md` |
  Twelve-Factor IV: Backing services as attached resources |
  https://12factor.net/backing-services
- `12factor-config.md` |
  Twelve-Factor III: Config — store config in the environment |
  https://12factor.net/config
- `12factor-dev-prod-parity.md` |
  Twelve-Factor X: Dev/prod parity |
  https://12factor.net/dev-prod-parity
- `12factor-intro.md` |
  The Twelve-Factor App — introduction |
  https://12factor.net/
- `12factor-logs.md` |
  Twelve-Factor XI: Logs as event streams |
  https://12factor.net/logs
- `aws-what-is-cloud-computing.md` |
  What is cloud computing? (AWS) |
  https://aws.amazon.com/what-is-cloud-computing/
- `aws-what-is-serverless.md` |
  What is serverless computing? (AWS) |
  https://aws.amazon.com/what-is/serverless-computing/
- `cloudflare-dns-records.md` |
  DNS record types explained (Cloudflare) |
  https://www.cloudflare.com/learning/dns/dns-records/
- `cloudflare-what-is-a-cdn.md` |
  What is a CDN? (Cloudflare) |
  https://www.cloudflare.com/learning/cdn/what-is-a-cdn/
- `cloudflare-what-is-dns.md` |
  What is DNS? (Cloudflare Learning Center) |
  https://www.cloudflare.com/learning/dns/what-is-dns/
- `cloudflare-what-is-load-balancing.md` |
  What is load balancing? (Cloudflare) |
  https://www.cloudflare.com/learning/performance/what-is-load-balancing/
- `cloudflare-what-is-ssl.md` |
  What is SSL / TLS? (Cloudflare) |
  https://www.cloudflare.com/learning/ssl/what-is-ssl/
- `gcp-iaas-paas-saas.md` |
  PaaS vs IaaS vs SaaS — cloud service models (Google Cloud) |
  https://cloud.google.com/learn/paas-vs-iaas-vs-saas
- `mdn-http-overview.md` |
  An overview of HTTP (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview
- `mdn-what-is-a-domain-name.md` |
  What is a domain name? (MDN) |
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name
- `mdn-what-is-a-web-server.md` |
  What is a web server? (MDN) |
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server

## 02_architectures — static sites to multi-tenant SaaS (incl. mobile / PWA)

- `azure-multitenant-overview.md` |
  Architecting multitenant solutions — overview (Microsoft Learn) |
  https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview
- `azure-multitenant-storage-data.md` |
  Architectural approaches for storage and data in multitenant solutions |
  https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data
- `azure-multitenant-tenancy-models.md` |
  Tenancy models for a multitenant solution (Microsoft Learn) |
  https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models
- `mdn-cors.md` |
  Cross-Origin Resource Sharing (CORS) (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- `mdn-fetch-api-using.md` |
  Using the Fetch API (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- `mdn-media-queries-using.md` |
  Using media queries (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries
- `mdn-progressive-web-apps.md` |
  Progressive web apps — overview (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
- `mdn-pwa-making-installable.md` |
  Making PWAs installable (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable
- `mdn-responsive-design.md` |
  Responsive design (MDN) |
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
- `mdn-viewport-meta-element.md` |
  Viewport meta element (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Viewport_meta_element
- `mdn-web-app-manifest.md` |
  Web app manifest reference (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest
- `mdn-web-storage-api.md` |
  Web Storage API — localStorage and sessionStorage (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API
- `web-dev-rendering-on-the-web.md` |
  Rendering on the web: SSR, SSG, CSR (web.dev) |
  https://web.dev/articles/rendering-on-the-web
- `web-dev-vitals.md` |
  Web Vitals — user-centric performance metrics (web.dev) |
  https://web.dev/articles/vitals

## 03_deployments — Cloudflare, VPS/Linux setup, Caddy/Nginx, PaaS, serverless, containers

- `aws-apigateway-welcome.md` |
  Amazon API Gateway — developer guide introduction |
  https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
- `aws-ec2-get-started.md` |
  AWS — get started with Amazon EC2 |
  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
- `aws-ecs-fargate.md` |
  AWS Fargate for Amazon ECS |
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
- `aws-lambda-welcome.md` |
  AWS Lambda — developer guide introduction |
  https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
- `aws-s3-website-hosting.md` |
  Amazon S3 — hosting a static website |
  https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
- `caddy-automatic-https.md` |
  Caddy — automatic HTTPS (certificate issuance and renewal) |
  https://caddyserver.com/docs/automatic-https
- `caddy-caddyfile-concepts.md` |
  Caddy — Caddyfile concepts |
  https://caddyserver.com/docs/caddyfile/concepts
- `caddy-docs-index.md` |
  Caddy documentation — index |
  https://caddyserver.com/docs/
- `caddy-install.md` |
  Caddy — installation |
  https://caddyserver.com/docs/install
- `caddy-quickstart-https.md` |
  Caddy quick start — HTTPS |
  https://caddyserver.com/docs/quick-starts/https
- `caddy-quickstart-reverse-proxy.md` |
  Caddy quick start — reverse proxy |
  https://caddyserver.com/docs/quick-starts/reverse-proxy
- `caddy-quickstart-static-files.md` |
  Caddy quick start — static file server |
  https://caddyserver.com/docs/quick-starts/static-files
- `caddy-running-service.md` |
  Caddy — running as a systemd service |
  https://caddyserver.com/docs/running
- `certbot-using.md` |
  Certbot — user guide |
  https://eff-certbot.readthedocs.io/en/stable/using.html
- `cloudflare-cache-purge.md` |
  Cloudflare cache — purge cached content |
  https://developers.cloudflare.com/cache/how-to/purge-cache/index.md
- `cloudflare-dns-full-setup.md` |
  Cloudflare DNS — full setup (change nameservers) |
  https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/index.md
- `cloudflare-dns-records-manage.md` |
  Cloudflare DNS — manage DNS records |
  https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/index.md
- `cloudflare-pages-build-config.md` |
  Cloudflare Pages — build configuration |
  https://developers.cloudflare.com/pages/configuration/build-configuration/index.md
- `cloudflare-pages-c3.md` |
  Cloudflare Pages — create-cloudflare CLI (C3) |
  https://developers.cloudflare.com/pages/get-started/c3/index.md
- `cloudflare-pages-custom-domains.md` |
  Cloudflare Pages — custom domains |
  https://developers.cloudflare.com/pages/configuration/custom-domains/index.md
- `cloudflare-pages-direct-upload.md` |
  Cloudflare Pages — deploy by direct upload |
  https://developers.cloudflare.com/pages/get-started/direct-upload/index.md
- `cloudflare-pages-git-integration.md` |
  Cloudflare Pages — Git integration (GitHub/GitLab builds) |
  https://developers.cloudflare.com/pages/get-started/git-integration/index.md
- `cloudflare-pages-headers.md` |
  Cloudflare Pages — custom headers and caching |
  https://developers.cloudflare.com/pages/configuration/headers/index.md
- `cloudflare-pages-overview.md` |
  Cloudflare Pages — overview |
  https://developers.cloudflare.com/pages/index.md
- `cloudflare-pages-preview-deployments.md` |
  Cloudflare Pages — preview deployments |
  https://developers.cloudflare.com/pages/configuration/preview-deployments/index.md
- `cloudflare-pages-redirects.md` |
  Cloudflare Pages — redirects |
  https://developers.cloudflare.com/pages/configuration/redirects/index.md
- `cloudflare-registrar-overview.md` |
  Cloudflare Registrar — register or transfer a domain |
  https://developers.cloudflare.com/registrar/index.md
- `cloudflare-wrangler-install.md` |
  Wrangler CLI — install and update |
  https://developers.cloudflare.com/workers/wrangler/install-and-update/index.md
- `cloudflare-wrangler-pages-commands.md` |
  Wrangler CLI — pages commands (wrangler pages deploy) |
  https://developers.cloudflare.com/workers/wrangler/commands/pages/index.md
- `cloudflare-wrangler-workers-commands.md` |
  Wrangler CLI — Workers commands (dev, deploy, versions) |
  https://developers.cloudflare.com/workers/wrangler/commands/workers/index.md
- `coolify-home.md` |
  Coolify — self-hostable open-source alternative to Heroku, Netlify and Vercel |
  https://coolify.io/
- `coolify-installation.md` |
  Coolify — installation on your own server |
  https://coolify.io/docs/get-started/installation
- `coolify-introduction.md` |
  Coolify — introduction and what it does |
  https://coolify.io/docs/get-started/introduction
- `coolify-readme.md` |
  Coolify — GitHub README (coollabsio) |
  https://raw.githubusercontent.com/coollabsio/coolify/main/README.md
- `digitalocean-droplet-quickstart.md` |
  DigitalOcean — Droplet quickstart |
  https://docs.digitalocean.com/products/droplets/getting-started/quickstart/
- `docker-build-best-practices.md` |
  Docker — building best practices for images |
  https://docs.docker.com/build/building/best-practices/
- `docker-compose-overview.md` |
  Docker Compose — overview |
  https://docs.docker.com/compose/
- `docker-compose-production.md` |
  Docker Compose in production |
  https://docs.docker.com/compose/how-tos/production/
- `docker-compose-services-reference.md` |
  Docker Compose — services top-level element reference |
  https://docs.docker.com/reference/compose-file/services/
- `flyio-getting-started-launch.md` |
  Fly.io — getting started: launch an existing app |
  https://fly.io/docs/getting-started/launch/
- `flyio-launch.md` |
  Fly.io — deploy an app with fly launch |
  https://fly.io/docs/launch/deploy/
- `hetzner-create-a-server.md` |
  Hetzner Cloud — creating a server |
  https://docs.hetzner.com/cloud/servers/getting-started/creating-a-server
- `kamal-configuration.md` |
  Kamal — configuration overview (deploy.yml) |
  https://kamal-deploy.org/docs/configuration/overview/
- `kamal-home.md` |
  Kamal — deploy web apps anywhere, from bare metal to cloud VMs |
  https://kamal-deploy.org/
- `kamal-installation.md` |
  Kamal — installation and first deploy |
  https://kamal-deploy.org/docs/installation/
- `kamal-readme.md` |
  Kamal — GitHub README (Basecamp) |
  https://raw.githubusercontent.com/basecamp/kamal/main/README.md
- `kubernetes-overview.md` |
  Kubernetes — what is Kubernetes? |
  https://kubernetes.io/docs/concepts/overview/
- `letsencrypt-getting-started.md` |
  Let's Encrypt — getting started |
  https://letsencrypt.org/getting-started/
- `letsencrypt-how-it-works.md` |
  Let's Encrypt — how it works (ACME) |
  https://letsencrypt.org/how-it-works/
- `nginx-beginners-guide.md` |
  nginx — beginner's guide |
  https://nginx.org/en/docs/beginners_guide.html
- `nginx-reverse-proxy-guide.md` |
  nginx — reverse proxy guide |
  https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
- `railway-quick-start.md` |
  Railway — quick start |
  https://docs.railway.com/quick-start
- `render-web-services.md` |
  Render — web services |
  https://render.com/docs/web-services
- `systemd-service-unit.md` |
  systemd.service(5) — service unit configuration |
  https://man7.org/linux/man-pages/man5/systemd.service.5.html
- `ubuntu-automatic-updates.md` |
  Ubuntu Server — automatic (unattended) security updates |
  https://documentation.ubuntu.com/server/how-to/software/automatic-updates/
- `ubuntu-community-ufw.md` |
  UFW — Uncomplicated Firewall (Ubuntu community help) |
  https://help.ubuntu.com/community/UFW
- `ubuntu-server-firewall.md` |
  Ubuntu Server — firewall (ufw / iptables) |
  https://documentation.ubuntu.com/server/how-to/security/firewalls/
- `ubuntu-server-openssh.md` |
  Ubuntu Server — OpenSSH server setup and key auth |
  https://documentation.ubuntu.com/server/how-to/security/openssh-server/

## 04_network_storage_db — networking, storage, databases (SQLite, self-hosted PostgreSQL)

- `aws-rds-what-is.md` |
  What is Amazon RDS? (managed relational databases) |
  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
- `aws-s3-welcome.md` |
  Amazon S3 — user guide introduction |
  https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
- `aws-vpc-security-groups.md` |
  Amazon VPC — security groups |
  https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
- `aws-vpc-subnets.md` |
  Amazon VPC — subnets |
  https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html
- `aws-what-is-vpc.md` |
  What is Amazon VPC? |
  https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- `cloudflare-r2-overview.md` |
  Cloudflare R2 — object storage without egress fees |
  https://developers.cloudflare.com/r2/index.md
- `gcp-cloud-storage-overview.md` |
  Google Cloud Storage — product overview |
  https://cloud.google.com/storage/docs/introduction
- `mariadb-vs-mysql.md` |
  MariaDB vs MySQL — compatibility and differences |
  https://mariadb.com/kb/en/mariadb-vs-mysql-compatibility/
- `postgresql-backup-dump.md` |
  PostgreSQL — SQL dump backups (pg_dump) |
  https://www.postgresql.org/docs/current/backup-dump.html
- `postgresql-database-roles.md` |
  PostgreSQL — database roles and privileges |
  https://www.postgresql.org/docs/current/user-manag.html
- `postgresql-pg-hba-conf.md` |
  PostgreSQL — the pg_hba.conf file (client authentication) |
  https://www.postgresql.org/docs/current/auth-pg-hba-conf.html
- `postgresql-runtime-config-connection.md` |
  PostgreSQL — connections and authentication settings |
  https://www.postgresql.org/docs/current/runtime-config-connection.html
- `postgresql-ssl-tcp.md` |
  PostgreSQL — secure TCP/IP connections with SSL |
  https://www.postgresql.org/docs/current/ssl-tcp.html
- `postgresql-tutorial-start.md` |
  PostgreSQL — getting started tutorial |
  https://www.postgresql.org/docs/current/tutorial-start.html
- `postgresql-warm-standby.md` |
  PostgreSQL — log-shipping standby servers and replication |
  https://www.postgresql.org/docs/current/warm-standby.html
- `rabbitmq-tutorial-work-queues.md` |
  RabbitMQ — work queues tutorial (Python) |
  https://www.rabbitmq.com/tutorials/tutorial-two-python
- `redis-data-store-get-started.md` |
  Redis — get started as a data store / cache |
  https://redis.io/docs/latest/develop/get-started/data-store/
- `restic-backup-docs.md` |
  restic — backup basics and repositories |
  https://restic.readthedocs.io/en/stable/040_backup.html
- `sqlite-about.md` |
  SQLite — about |
  https://www.sqlite.org/about.html
- `sqlite-backup.md` |
  SQLite — backup API and safe copies |
  https://www.sqlite.org/backup.html
- `sqlite-quirks.md` |
  SQLite — quirks, caveats and gotchas |
  https://www.sqlite.org/quirks.html
- `sqlite-wal.md` |
  SQLite — write-ahead logging (WAL mode) |
  https://www.sqlite.org/wal.html
- `sqlite-when-to-use.md` |
  SQLite — appropriate uses for SQLite |
  https://www.sqlite.org/whentouse.html

## 05_ops_cicd_security — CI/CD, monitoring, security, authentication, cost

- `aicpa-soc2-overview.md` |
  AICPA — SOC 2 examinations overview (the authority that defines SOC 2) |
  https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
- `auth0-get-started.md` |
  Auth0 — get started / core concepts |
  https://auth0.com/docs/get-started
- `aws-artifact-what-is.md` |
  AWS Artifact — downloading your provider's SOC 2 report |
  https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html
- `aws-backup-what-is.md` |
  AWS Backup — centralized, policy-based backups (availability criterion) |
  https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html
- `aws-budgets-managing-costs.md` |
  AWS Budgets — managing your costs |
  https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html
- `aws-cloudhsm-intro.md` |
  AWS CloudHSM — what is a hardware security module? |
  https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html
- `aws-cloudtrail-user-guide.md` |
  AWS CloudTrail — audit trail of API activity |
  https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
- `aws-config-what-is.md` |
  AWS Config — continuous configuration compliance monitoring |
  https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html
- `aws-ebs-encryption.md` |
  Amazon EBS encryption — encrypting volumes at rest |
  https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html
- `aws-iam-access-analyzer.md` |
  AWS IAM Access Analyzer — finding overly broad access |
  https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
- `aws-iam-best-practices.md` |
  AWS IAM — security best practices (least privilege) |
  https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- `aws-kms-concepts.md` |
  AWS KMS — concepts: KMS keys, data keys, envelope encryption |
  https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html
- `aws-kms-key-policies.md` |
  AWS KMS — key policies and access control |
  https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html
- `aws-kms-overview.md` |
  AWS KMS — developer guide overview |
  https://docs.aws.amazon.com/kms/latest/developerguide/overview.html
- `aws-kms-product-page.md` |
  AWS Key Management Service (KMS) — product overview |
  https://aws.amazon.com/kms/
- `aws-kms-rotate-keys.md` |
  AWS KMS — rotating KMS keys |
  https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html
- `aws-parameter-store.md` |
  AWS Systems Manager Parameter Store — cheap config and secret storage |
  https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
- `aws-penetration-testing-policy.md` |
  AWS — customer support policy for penetration testing (authorization) |
  https://aws.amazon.com/security/penetration-testing/
- `aws-rds-encryption.md` |
  Amazon RDS — encrypting database resources at rest |
  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html
- `aws-s3-sse-kms.md` |
  Amazon S3 — server-side encryption with KMS keys (SSE-KMS) |
  https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html
- `aws-secrets-manager-intro.md` |
  AWS Secrets Manager — what it is and when to use it |
  https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
- `aws-soc-faqs.md` |
  AWS — SOC compliance FAQs (SOC 1/2/3, shared responsibility) |
  https://aws.amazon.com/compliance/soc-faqs/
- `aws-well-architected-security-pillar.md` |
  AWS Well-Architected — security pillar: design principles |
  https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/security.html
- `azure-key-vault-overview.md` |
  Azure Key Vault — overview (keys, secrets, certificates) |
  https://learn.microsoft.com/en-us/azure/key-vault/general/overview
- `cis-controls-list.md` |
  CIS Critical Security Controls — prioritized control list |
  https://www.cisecurity.org/controls/cis-controls-list
- `clerk-overview.md` |
  Clerk — overview and quickstarts |
  https://clerk.com/docs
- `cloudflare-trust-hub-compliance.md` |
  Cloudflare Trust Hub — compliance certifications and reports |
  https://www.cloudflare.com/trust-hub/compliance-resources/
- `cloudflare-workers-secrets.md` |
  Cloudflare Workers / Pages — storing secrets |
  https://developers.cloudflare.com/workers/configuration/secrets/index.md
- `docker-compose-secrets.md` |
  Docker Compose — using secrets in services |
  https://docs.docker.com/compose/how-tos/use-secrets/
- `firebase-auth-google-signin.md` |
  Firebase Authentication — Google sign-in on the web |
  https://firebase.google.com/docs/auth/web/google-signin
- `firebase-auth-manage-users.md` |
  Firebase Authentication — manage users on the web |
  https://firebase.google.com/docs/auth/web/manage-users
- `firebase-auth-overview.md` |
  Firebase Authentication — overview |
  https://firebase.google.com/docs/auth
- `firebase-auth-password-auth.md` |
  Firebase Authentication — email/password auth on the web |
  https://firebase.google.com/docs/auth/web/password-auth
- `firebase-auth-web-start.md` |
  Firebase Authentication — get started on the web |
  https://firebase.google.com/docs/auth/web/start
- `firebase-security-rules-get-started.md` |
  Firebase Security Rules — get started |
  https://firebase.google.com/docs/rules/get-started
- `gcp-billing-budgets.md` |
  Google Cloud — create budgets and budget alerts |
  https://cloud.google.com/billing/docs/how-to/budgets
- `gcp-cloud-audit-logs.md` |
  Google Cloud Audit Logs — who did what, where, and when |
  https://cloud.google.com/logging/docs/audit
- `gcp-cloud-hsm.md` |
  Google Cloud HSM — FIPS 140-2 Level 3 hardware-backed keys |
  https://cloud.google.com/kms/docs/hsm
- `gcp-cmek.md` |
  Google Cloud — customer-managed encryption keys (CMEK) |
  https://cloud.google.com/kms/docs/cmek
- `gcp-encryption-at-rest.md` |
  Google Cloud — default encryption at rest |
  https://cloud.google.com/docs/security/encryption/default-encryption
- `gcp-kms-envelope-encryption.md` |
  Google Cloud KMS — envelope encryption explained |
  https://cloud.google.com/kms/docs/envelope-encryption
- `gcp-kms-key-rotation.md` |
  Google Cloud KMS — key rotation |
  https://cloud.google.com/kms/docs/key-rotation
- `gcp-kms-overview.md` |
  Google Cloud KMS — key management service overview |
  https://cloud.google.com/kms/docs/key-management-service
- `gcp-secret-manager-overview.md` |
  Google Cloud Secret Manager — overview |
  https://cloud.google.com/secret-manager/docs/overview
- `gcp-soc2-compliance.md` |
  Google Cloud — SOC 2 compliance offering |
  https://cloud.google.com/security/compliance/soc-2
- `github-actions-deployment.md` |
  GitHub Actions — continuous deployment concepts |
  https://docs.github.com/en/actions/concepts/overview/continuous-deployment
- `github-actions-secrets.md` |
  GitHub Actions — using secrets in workflows |
  https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- `github-actions-understanding.md` |
  Understanding GitHub Actions |
  https://docs.github.com/en/actions/get-started/understanding-github-actions
- `github-actions-workflow-syntax.md` |
  GitHub Actions — workflow syntax reference |
  https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- `github-code-scanning.md` |
  GitHub — about code scanning (CodeQL static analysis) |
  https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning
- `github-dependabot-alerts.md` |
  GitHub — about Dependabot alerts (vulnerable dependencies) |
  https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
- `github-push-protection.md` |
  GitHub — push protection for secrets |
  https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- `github-secret-scanning.md` |
  GitHub — about secret scanning (finding committed credentials) |
  https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning
- `gitlab-ci-quick-start.md` |
  GitLab CI/CD — get started |
  https://docs.gitlab.com/ci/quick_start/
- `gitleaks-readme.md` |
  Gitleaks — scan git history for hardcoded secrets (README) |
  https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md
- `grafana-loki-get-started.md` |
  Grafana Loki — get started with log aggregation |
  https://grafana.com/docs/loki/latest/get-started/
- `lynis-readme.md` |
  Lynis — Linux server security auditing (README) |
  https://raw.githubusercontent.com/CISOfy/lynis/master/README.md
- `mdn-content-security-policy.md` |
  Content Security Policy (CSP) (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP
- `mdn-security-practical-guides.md` |
  MDN — practical security implementation guides (headers, TLS, cookies) |
  https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides
- `mdn-strict-transport-security.md` |
  HTTP Strict-Transport-Security (HSTS) — enforcing TLS (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security
- `nist-cmvp-fips-140.md` |
  NIST Cryptographic Module Validation Program (FIPS 140-3) |
  https://csrc.nist.gov/projects/cryptographic-module-validation-program
- `nist-incident-handling-guide.md` |
  NIST SP 800-61 — computer security incident handling guide |
  https://csrc.nist.gov/pubs/sp/800/61/r3/final
- `npm-audit.md` |
  npm audit — scanning JavaScript dependencies |
  https://docs.npmjs.com/cli/v10/commands/npm-audit
- `owasp-asvs.md` |
  OWASP Application Security Verification Standard (ASVS) |
  https://owasp.org/www-project-application-security-verification-standard/
- `owasp-authentication-cheatsheet.md` |
  OWASP — authentication cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- `owasp-authorization-cheatsheet.md` |
  OWASP — authorization cheat sheet (least privilege, access reviews) |
  https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- `owasp-cryptographic-storage-cheatsheet.md` |
  OWASP — cryptographic storage cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
- `owasp-csrf-prevention.md` |
  OWASP — cross-site request forgery prevention cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- `owasp-input-validation-cheatsheet.md` |
  OWASP — input validation cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- `owasp-key-management-cheatsheet.md` |
  OWASP — key management cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html
- `owasp-logging-cheatsheet.md` |
  OWASP — logging cheat sheet (what to log, what never to log) |
  https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- `owasp-secrets-management-cheatsheet.md` |
  OWASP — secrets management cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- `owasp-sql-injection-prevention.md` |
  OWASP — SQL injection prevention cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- `owasp-tls-cheatsheet.md` |
  OWASP — transport layer security cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html
- `owasp-top-ten.md` |
  OWASP Top 10 web application security risks |
  https://owasp.org/www-project-top-ten/
- `owasp-vulnerable-dependency-management.md` |
  OWASP — vulnerable dependency management cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html
- `owasp-wstg-stable.md` |
  OWASP Web Security Testing Guide — stable release (test checklist) |
  https://owasp.org/www-project-web-security-testing-guide/stable/
- `owasp-wstg.md` |
  OWASP Web Security Testing Guide (WSTG) |
  https://owasp.org/www-project-web-security-testing-guide/
- `owasp-xss-prevention.md` |
  OWASP — cross-site scripting prevention cheat sheet |
  https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- `pip-audit-readme.md` |
  pip-audit — scanning Python dependencies (README) |
  https://raw.githubusercontent.com/pypa/pip-audit/main/README.md
- `portswigger-web-security-academy.md` |
  PortSwigger Web Security Academy — free hands-on labs |
  https://portswigger.net/web-security
- `postgresql-encryption-options.md` |
  PostgreSQL — encryption options (at rest and in transit) |
  https://www.postgresql.org/docs/current/encryption-options.html
- `prometheus-overview.md` |
  Prometheus — overview |
  https://prometheus.io/docs/introduction/overview/
- `sops-readme.md` |
  SOPS — encrypted secrets files in git (README) |
  https://raw.githubusercontent.com/getsops/sops/main/README.rst
- `sre-book-monitoring.md` |
  Google SRE Book — monitoring distributed systems |
  https://sre.google/sre-book/monitoring-distributed-systems/
- `sre-book-slos.md` |
  Google SRE Book — service level objectives |
  https://sre.google/sre-book/service-level-objectives/
- `supabase-auth-overview.md` |
  Supabase Auth — overview |
  https://supabase.com/docs/guides/auth
- `systemd-credentials.md` |
  systemd — passing credentials to services (LoadCredential) |
  https://systemd.io/CREDENTIALS/
- `trivy-overview.md` |
  Trivy — container, filesystem and IaC vulnerability scanner |
  https://trivy.dev/latest/docs/
- `uptime-kuma-readme.md` |
  Uptime Kuma — self-hosted uptime monitoring (README) |
  https://raw.githubusercontent.com/louislam/uptime-kuma/master/README.md
- `vault-what-is-vault.md` |
  HashiCorp Vault — what is Vault? |
  https://developer.hashicorp.com/vault/docs/what-is-vault
- `zap-desktop-getting-started.md` |
  OWASP ZAP — desktop UI: running your first scan |
  https://www.zaproxy.org/docs/desktop/start/
- `zap-docker-baseline-scan.md` |
  OWASP ZAP — automated baseline scan in Docker / CI |
  https://www.zaproxy.org/docs/docker/baseline-scan/
- `zap-getting-started.md` |
  OWASP ZAP — getting started with the web app scanner |
  https://www.zaproxy.org/getting-started/

## 06_product_patterns — infra by product type (incl. landing pages / email capture)

- `aweber-email-automation.md` |
  AWeber — email automation and autoresponder campaigns |
  https://www.aweber.com/email-automation.htm
- `aweber-home.md` |
  AWeber — email marketing and autoresponders (home) |
  https://www.aweber.com
- `aweber-pricing.md` |
  AWeber — plans and pricing (free tier limits) |
  https://www.aweber.com/pricing.htm
- `aws-ses-bounce-complaint-handling.md` |
  Amazon SES — deliverability: handling bounces and complaints |
  https://docs.aws.amazon.com/ses/latest/dg/send-email-concepts-deliverability.html
- `aws-ses-custom-mail-from.md` |
  Amazon SES — using a custom MAIL FROM domain (SPF alignment, MX record) |
  https://docs.aws.amazon.com/ses/latest/dg/mail-from.html
- `aws-ses-dkim.md` |
  Amazon SES — DKIM signing (Easy DKIM, BYODKIM) |
  https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html
- `aws-ses-dmarc.md` |
  Amazon SES — complying with DMARC |
  https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dmarc.html
- `aws-ses-event-publishing.md` |
  Amazon SES — event publishing (bounces, complaints, deliveries) |
  https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html
- `aws-ses-pricing.md` |
  Amazon SES — pricing (per-1,000-email cost, EC2 free tier) |
  https://aws.amazon.com/ses/pricing/
- `aws-ses-product-page.md` |
  Amazon SES — product overview and use cases |
  https://aws.amazon.com/ses/
- `aws-ses-production-access.md` |
  Amazon SES — moving out of the sandbox (request production access) |
  https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html
- `aws-ses-send-email-sdk.md` |
  Amazon SES — sending email programmatically with the AWS SDK |
  https://docs.aws.amazon.com/ses/latest/dg/send-an-email-using-sdk-programmatically.html
- `aws-ses-sending-quotas.md` |
  Amazon SES — sending quotas and rate limits |
  https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html
- `aws-ses-smtp.md` |
  Amazon SES — sending via the SMTP interface |
  https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html
- `aws-ses-spf.md` |
  Amazon SES — SPF and custom MAIL FROM domain |
  https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-spf.html
- `aws-ses-verify-identities.md` |
  Amazon SES — creating and verifying sender identities (domain, email) |
  https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html
- `aws-ses-welcome.md` |
  Amazon SES — developer guide introduction |
  https://docs.aws.amazon.com/ses/latest/dg/Welcome.html
- `cloudflare-dns-email-records.md` |
  Cloudflare DNS — email records (SPF, DKIM, DMARC, MX) |
  https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/index.md
- `google-bulk-sender-guidelines.md` |
  Google — email sender guidelines (authentication, spam rate, unsubscribe) |
  https://support.google.com/a/answer/81126
- `google-search-central-structured-data.md` |
  Google Search Central — intro to structured data markup |
  https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- `mailchimp-double-opt-in.md` |
  About double opt-in for email lists (Mailchimp) |
  https://mailchimp.com/help/about-double-opt-in/
- `mailchimp-landing-pages.md` |
  Mailchimp — about landing pages |
  https://mailchimp.com/help/about-landing-pages/
- `mailchimp-signup-forms.md` |
  Mailchimp — add a signup form to your website |
  https://mailchimp.com/help/add-a-signup-form-to-your-website/
- `mdn-responsive-images.md` |
  Responsive images — srcset and sizes (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- `postmark-developer-docs.md` |
  Postmark — transactional email developer documentation |
  https://postmarkapp.com/developer
- `resend-introduction.md` |
  Resend — developer-first transactional email (introduction) |
  https://resend.com/docs/introduction
- `schema-org-product.md` |
  schema.org Product — structured data for catalog items |
  https://schema.org/Product
- `stripe-how-checkout-works.md` |
  Stripe Checkout — how Checkout works |
  https://docs.stripe.com/payments/checkout/how-checkout-works
- `stripe-subscriptions-overview.md` |
  Stripe Billing — subscriptions overview |
  https://docs.stripe.com/billing/subscriptions/overview
- `web-dev-image-formats.md` |
  web.dev — choose the right image format |
  https://web.dev/articles/choose-the-right-image-format
- `web3forms-ajax-form-example.md` |
  Web3Forms — AJAX contact form with JavaScript (example) |
  https://docs.web3forms.com/getting-started/examples/ajax-contact-form-using-javascript
- `web3forms-autoresponder.md` |
  Web3Forms — autoresponder (automatic reply to the submitter) |
  https://docs.web3forms.com/getting-started/pro-features/autoresponder
- `web3forms-docs.md` |
  Web3Forms — documentation |
  https://docs.web3forms.com/
- `web3forms-getting-started.md` |
  Web3Forms — installation and first form (access key) |
  https://docs.web3forms.com/getting-started/installation
- `web3forms-google-sheets.md` |
  Web3Forms — send submissions to Google Sheets |
  https://docs.web3forms.com/getting-started/integrations/google-sheets
- `web3forms-home.md` |
  Web3Forms — contact forms for static sites (home) |
  https://web3forms.com
- `web3forms-redirection.md` |
  Web3Forms — redirect to a thank-you page after submit |
  https://docs.web3forms.com/getting-started/customizations/redirection
- `web3forms-spam-protection.md` |
  Web3Forms — spam protection (honeypot, captcha) |
  https://docs.web3forms.com/getting-started/customizations/spam-protection/spam-protection

## 07_playbooks — recipes and checklists

- `cloudflare-pages-deploy-anything.md` |
  Cloudflare Pages — deploy any static site (framework guide) |
  https://developers.cloudflare.com/pages/framework-guides/deploy-anything/index.md
- `crontab-5-man-page.md` |
  crontab(5) — cron table format for scheduled backups |
  https://man7.org/linux/man-pages/man5/crontab.5.html
- `django-deployment-checklist.md` |
  Django — deployment checklist |
  https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- `fail2ban-readme.md` |
  Fail2Ban — README (SSH brute-force protection) |
  https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md
- `fastapi-deployment-concepts.md` |
  FastAPI — deployment concepts |
  https://fastapi.tiangolo.com/deployment/concepts/
- `fastapi-run-server-manually.md` |
  FastAPI — run a server manually (Uvicorn/Gunicorn behind a proxy) |
  https://fastapi.tiangolo.com/deployment/manually/
- `mdn-lazy-loading.md` |
  Lazy loading images and iframes (MDN) |
  https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading
- `pg-dump-man.md` |
  PostgreSQL — pg_dump reference |
  https://www.postgresql.org/docs/current/app-pgdump.html
- `python-http-server-docs.md` |
  Python http.server — simple local dev server |
  https://docs.python.org/3/library/http.server.html
- `rsync-man-page.md` |
  rsync(1) — file transfer and backup |
  https://man7.org/linux/man-pages/man1/rsync.1.html
- `ssh-keygen-man-page.md` |
  ssh-keygen(1) — generating SSH keys |
  https://man7.org/linux/man-pages/man1/ssh-keygen.1.html
- `web-dev-service-worker-caching.md` |
  Service workers and caching strategies (web.dev) |
  https://web.dev/learn/pwa/service-workers

## 08_scaling_maturity — environments, IaC, scaling

- `aws-well-architected-reliability.md` |
  AWS Well-Architected — reliability pillar |
  https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
- `drata-soc2-compliance.md` |
  SOC 2 compliance guide — scoping, evidence, audit (Drata) |
  https://drata.com/grc-central/soc-2
- `github-environments.md` |
  GitHub Actions — managing deployment environments |
  https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
- `iso-27001-offering.md` |
  ISO/IEC 27001 — what the standard covers (Microsoft Learn compliance offering) |
  https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001
- `martinfowler-feature-toggles.md` |
  Feature toggles (feature flags) — Martin Fowler |
  https://martinfowler.com/articles/feature-toggles.html
- `martinfowler-microservice-premium.md` |
  MicroservicePremium — don't start with microservices |
  https://martinfowler.com/bliki/MicroservicePremium.html
- `martinfowler-monolith-first.md` |
  MonolithFirst — Martin Fowler |
  https://martinfowler.com/bliki/MonolithFirst.html
- `pgbouncer-config.md` |
  PgBouncer — connection pooling configuration |
  https://www.pgbouncer.org/config.html
- `postgresql-partitioning.md` |
  PostgreSQL — table partitioning |
  https://www.postgresql.org/docs/current/ddl-partitioning.html
- `pulumi-iac-concepts.md` |
  Pulumi — infrastructure as code concepts |
  https://www.pulumi.com/docs/iac/concepts/
- `terraform-iac-tutorial.md` |
  Terraform — what is infrastructure as code (tutorial) |
  https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code
- `terraform-intro.md` |
  Terraform — what is Terraform / intro to IaC |
  https://developer.hashicorp.com/terraform/intro
- `terraform-language.md` |
  Terraform — configuration language overview |
  https://developer.hashicorp.com/terraform/language
- `vanta-soc2-checklist.md` |
  SOC 2 compliance checklist — controls, evidence and timeline (Vanta) |
  https://www.vanta.com/collection/soc-2/soc-2-compliance-checklist
- `vanta-what-is-soc2.md` |
  What is SOC 2? Type I vs Type II, criteria and timeline (Vanta) |
  https://www.vanta.com/collection/soc-2/what-is-soc-2

## 09_appendices — starter stacks, diagrams, further reading, case study

- `aws-well-architected-framework.md` |
  AWS Well-Architected Framework — overview |
  https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- `azure-web-app-reference-architecture.md` |
  Azure — basic web application reference architecture |
  https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/basic-web-app
- `cloudflare-pages-functions.md` |
  Cloudflare Pages Functions — get started |
  https://developers.cloudflare.com/pages/functions/get-started/index.md
- `cloudflare-pages-limits.md` |
  Cloudflare Pages — platform limits and pricing tiers |
  https://developers.cloudflare.com/pages/platform/limits/index.md
- `freecodecamp-build-first-saas.md` |
  How to build your first SaaS (freeCodeCamp) |
  https://www.freecodecamp.org/news/how-to-build-your-first-saas/
- `gcp-architecture-framework.md` |
  Google Cloud Architecture Framework |
  https://cloud.google.com/architecture/framework
- `roadmap-sh-devops.md` |
  roadmap.sh — DevOps learning roadmap |
  https://roadmap.sh/devops
- `sre-book-index.md` |
  Google SRE Book — table of contents (free online) |
  https://sre.google/sre-book/table-of-contents/
- `usersnap-saas-architecture.md` |
  Cloud-based SaaS architecture fundamentals (Usersnap) |
  https://usersnap.com/blog/cloud-based-saas-architecture-fundamentals/

## Local reference implementations (not downloads)

Some of the static-site material in this wiki is drawn
from a working private project rather than from a
downloaded document: a catalog site built as a directory
of JSON plus images, rendered to static pages by a short
chain of numbered Python scripts and deployed to
Cloudflare Pages, with Web3Forms handling quote requests.

The patterns are written up in the wiki pages
`File-Based CMS`, `Static Build Pipeline`,
`Catalog and Inventory Sites` and
`Backend-Free Interactivity`. The project itself is not
public and its details are deliberately not recorded
here.

## Known gaps

Sources that could not be downloaded on 2026-07-27,
and what was used instead. Re-check periodically —
some are transient.

- **MySQL Reference Manual** (`dev.mysql.com`) —
  HTTP 403, bot-blocked. Substituted
  `mariadb-vs-mysql.md` (MariaDB KB) plus
  `aws-rds-what-is.md` for the managed-MySQL angle.
- **AWeber knowledge base** (`help.aweber.com`,
  Zendesk) — HTTP 403 on every article, so the
  sign-up-form, confirmed-opt-in and campaign
  how-tos could not be captured. Substituted
  `aweber-home.md`, `aweber-email-automation.md`,
  `aweber-pricing.md` for the vendor side, and
  `mailchimp-double-opt-in.md` +
  `mailchimp-signup-forms.md` for the mechanics
  (they apply to any autoresponder).
- **Debian wiki — UnattendedUpgrades**
  (`wiki.debian.org`) — the whole wiki served a
  "Technical Difficulties" page. Substituted
  `ubuntu-automatic-updates.md` (official Ubuntu
  Server docs), which covers the same package.
- **Gunicorn deployment guide**
  (`docs.gunicorn.org/en/stable/deploy.html`) —
  redirects to a 404; the docs site has been
  restructured. Substituted
  `fastapi-run-server-manually.md` and
  `django-deployment-checklist.md`.
- **Terraform Registry provider docs**
  (`registry.terraform.io`) — client-rendered, the
  HTML response carries no content. Substituted
  `terraform-language.md` and
  `terraform-iac-tutorial.md`.
- **Stripe interactive quickstarts**
  (`docs.stripe.com/*/quickstart`) — client-rendered
  wizards with no server-side prose. Substituted
  `stripe-how-checkout-works.md` and
  `stripe-subscriptions-overview.md`.
- **Kit / ConvertKit help centre** — the sequences
  article served unrelated content (Teachable
  integration) behind an Intercom redirect. Dropped;
  the Mailchimp pages above cover the same ground.
- **AICPA Trust Services Criteria (the TSC
  document)** — the AICPA publishes the criteria as
  a gated PDF, not at a fetchable URL. Only the SOC 2
  overview page was captured
  (`aicpa-soc2-overview.md`). Criterion-level detail
  in `Raw/` therefore comes from vendor guides
  (Vanta, Drata) and provider compliance pages;
  treat it as orientation, not authority, and check
  the official TSC PDF before stating what a
  specific criterion requires.
- **ISO** (`iso.org`) — HTTP 403, bot-blocked.
  Substituted `iso-27001-offering.md` (Microsoft
  Learn) for the SOC 2 vs ISO 27001 comparison.
- **Secureframe SOC 2 checklist** — HTTP 500.
  Substituted `vanta-soc2-checklist.md`.

Section index pages that are navigation-only
(`.../pages/functions/`, `.../wrangler/commands/`,
`fly.io/docs/speedrun/`, `docs.web3forms.com/`) were
replaced with the concrete content pages beneath
them, which is why some filenames differ slightly
from the URLs listed in `myprompts/TOC_infra.md`.
