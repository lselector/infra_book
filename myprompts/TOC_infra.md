Here’s a concise, opinionated Table of Contents for a “cheap and simple cloud infrastructure for web/SaaS” book aimed at practitioners.

## Part I – Foundations: Thinking About Infrastructure

1. Why This Book: Simple, Cheap, Pragmatic Infrastructure  
2. What “Infrastructure” Means for Web & SaaS  
3. Cloud Service Models: IaaS vs PaaS vs Serverless vs SaaS [cloud.google](https://cloud.google.com/learn/paas-vs-iaas-vs-saas)
4. Core Building Blocks: DNS, SSL, HTTP, Domains, Load Balancers  
5. Design Principles for Small Teams: 12‑Factor‑Style Apps, Automation, Keep It Boring [reddit](https://www.reddit.com/r/devops/comments/4z41bs/any_favorite_best_practices_resources_for/)

## Part II – Typical Architectures, From Static to SaaS

6. The Ladder: Ten Stacks in Increasing Order of Complexity — a worked example at each rung (static site on Cloudflare → Caddy + FastAPI → add a database → add email → add auth and payments → …), what each one costs, and the single signal that tells you to climb (see `Dashboards/Stacks.md`)  
7. Static Website Hosting (Marketing Sites, Docs, Blogs)  
8. Content as Files: A Directory of JSON + Images as a Tiny CMS (no database, no admin panel)  
9. Interactivity Without a Backend: Vanilla JS, Generated Data Files, and localStorage  
10. Simple Monolithic Web App (CRUD SaaS, Admin Panels)  
11. API‑First Backend + Separate Frontend (SPA + API)  
12. One App, All Screens: Making the Web App Work on Smartphones (responsive layout, PWA, mobile performance) [developer.mozilla](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
13. Multi‑Tenant SaaS Patterns (shared DB vs per‑tenant DB, isolation) [dev.bitolog](https://dev.bitolog.com/design-build-and-code-a-saas-product-from-scratch/)
14. Picking the Right Architecture for Your Stage and Budget [towardsaws](https://towardsaws.com/the-best-way-to-build-a-saas-web-app-for-free-427afeb43b20)

## Part III – Cheap and Simple Deployments on Common Clouds

15. Cloudflare as a Cheap Front Door: Registrar, DNS, CDN, and Pages in One Place [cloudflare](https://www.cloudflare.com)
16. Cloudflare Pages for Static Sites: Direct Upload vs GitHub‑Connected Builds [developers.cloudflare](https://developers.cloudflare.com/pages/)
17. Deploying with the Wrangler CLI: `wrangler pages deploy`, Preview vs Production, Cache Purge [developers.cloudflare](https://developers.cloudflare.com/workers/wrangler/)
18. The Static Build Pipeline: Validate → Optimize Images → Build → Cache‑Bust → Deploy (numbered scripts you can run in order)  
19. One‑Box Deployments (Cheap VPS: Hetzner, DigitalOcean, EC2‑light) [community.spiceworks](https://community.spiceworks.com/t/fastest-way-to-build-a-cloud-infrastructure-on-premise/367983)
20. Setting Up a Simple Linux Server in the Cloud (Ubuntu: sudo user, SSH keys, firewall, systemd, unattended upgrades)  
21. Reverse Proxy and Automatic HTTPS: Caddy vs Nginx — automatic certificate issuance and renewal, a much simpler config [caddyserver](https://caddyserver.com/docs/)
22. Managed PaaS (Render, Fly.io, Railway, Heroku‑style)  
23. Serverless Full‑Stack (Static frontend + Lambda/API Gateway backend on AWS) [towardsaws](https://towardsaws.com/the-best-way-to-build-a-saas-web-app-for-free-427afeb43b20)
24. Containers Without the Pain (Docker Compose in Production, ECS/Fargate Lite)  
25. When You Actually Need Kubernetes (and When You Really Don’t)  

## Part IV – Core Infrastructure: Networking, Storage, and Databases

26. VPCs, Subnets, Security Groups, and Firewalls – Minimal Mental Model [youtube](https://www.youtube.com/watch?v=TPKQup_b0yk)
27. Object Storage (S3, GCS, Azure Blob) for Assets and Static Sites [youtube](https://www.youtube.com/watch?v=TPKQup_b0yk)
28. SQLite for Very Simple Apps: One File, No Database Server, No Ops [sqlite](https://www.sqlite.org/whentouse.html)
29. Relational Databases (PostgreSQL, MySQL) – Single Node to Managed Service  
30. PostgreSQL on the Same Server: Install, Secure, Connect, and Back Up [postgresql](https://www.postgresql.org/docs/)
31. Caching and Queues (Redis, RabbitMQ) for Simple Scale [usersnap](https://usersnap.com/blog/cloud-based-saas-architecture-fundamentals/)
32. Multi‑Region and Backups: Cheap Resilience Before Fancy HA [youtube](https://www.youtube.com/watch?v=TPKQup_b0yk)

## Part V – Operational Basics: CI/CD, Monitoring, and Security

33. Git‑Driven Deployment: From “SSH & Git Pull” to CI/CD Pipelines [reddit](https://www.reddit.com/r/devops/comments/4z41bs/any_favorite_best_practices_resources_for/)
34. Minimal CI/CD Setup (GitHub Actions / GitLab CI)  
35. Logging, Metrics, and Alerts: What to Monitor First  
36. Basic Security Hygiene (HTTPS, secrets management, least privilege) [reddit](https://www.reddit.com/r/devops/comments/4z41bs/any_favorite_best_practices_resources_for/)
37. Storing Secrets Safely: Environment Variables, `.env` Files, and Secret Managers (never in Git; AWS Secrets Manager / Parameter Store, Google Secret Manager, Vault, platform-native secrets) [owasp](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
38. Key Management: KMS and HSMs — Envelope Encryption, Key Rotation, and What an HSM Actually Buys You (AWS KMS, Google Cloud KMS, CloudHSM) [aws](https://aws.amazon.com/kms/)
39. Authentication Without Rolling Your Own (Firebase Authentication; when Auth0 / Clerk / Supabase Auth fit better) [firebase](https://firebase.google.com/docs/auth)
40. Testing the Security of Your Website or App: Scanners, Dependency Audits, and Manual Checks (OWASP ZAP, Dependabot, `npm audit` / `pip-audit`, TLS and header tests, when to hire a pentester) [owasp](https://owasp.org/www-project-web-security-testing-guide/)
41. Making Your App SOC 2 Compliant: The Trust Services Criteria in Plain English — Encryption in Transit and at Rest, Access Control and Access Reviews, Audit Logging, Change Management, Backups, and Vendor Management (what the controls mean for a one‑box or serverless app, and which ones your cloud provider already covers) [aicpa](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)
42. Cost Control and Budget Guardrails  

## Part VI – Patterns for Different Product Types

43. Infrastructure for Simple Web Sites (Portfolio, Content, Marketing)  
44. Catalog and Inventory Sites: Products, Categories, Detail Pages, and Photo Galleries Without a Database  
45. Forms Without a Backend: Web3Forms for Contact and Quote Requests (public access key, spam protection, where submissions land) [web3forms](https://web3forms.com)
46. Landing Pages: Capturing Name + Email and Starting an Autoresponder Sequence [aweber](https://www.aweber.com)
47. Sending Email from Your App: Transactional Email with Amazon SES — Verify a Domain, DKIM/SPF/DMARC, Leave the Sandbox, Send via SMTP or SDK, and Handle Bounces and Complaints (and when Postmark or Resend is worth the higher per‑email price) [aws](https://aws.amazon.com/ses/)
48. Infrastructure for Small SaaS with Auth, Billing, and Admin [freecodecamp](https://www.freecodecamp.org/news/how-to-build-your-first-saas/)
49. Infrastructure for API Products and Developer Tools  
50. Infrastructure for Internal Line‑of‑Business Apps  
51. Migrating from “Prototype Infra” to “Real Infra” Without Rewriting Everything [dev](https://dev.to/thebitforge/building-scalable-saas-products-a-developers-guide-48a7)

## Part VII – Playbooks and Recipes

52. Recipe: Deploy a Static Site in 30 Minutes (Domain + DNS + SSL + CDN)  
53. Recipe: Static Site on Cloudflare Pages — Register or Point a Domain, Deploy by Upload or GitHub [developers.cloudflare](https://developers.cloudflare.com/pages/)
54. Recipe: A Folder of JSON + Photos → a Deployed Site, in Four Commands (validate, clean images, build, deploy)  
55. Recipe: Preview Locally Before You Ship (a 40‑line Python dev server with no‑cache headers)  
56. Recipe: Add a Contact / Quote Form to a Static Site with Web3Forms  
57. Recipe: Provision and Harden an Ubuntu Server in One Hour  
58. Recipe: HTTPS in Five Lines — Put Caddy in Front of Your App (certs issued and renewed automatically)  
59. Recipe: Deploy a Monolithic SaaS on a Single VPS Safely  
60. Recipe: Ship a Tiny App on SQLite — and Migrate to PostgreSQL Later Without Panic  
61. Recipe: App + PostgreSQL on One Box, with Nightly Backups  
62. Recipe: Landing Page → Email Capture → Autoresponder Sequence (double opt‑in, welcome drip) [aweber](https://www.aweber.com)
63. Recipe: Send Your First Transactional Email with Amazon SES (verify the domain, publish DKIM and SPF records in Cloudflare DNS, request production access, send from Python, and route bounces to SNS) [aws](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
64. Recipe: Add Firebase Authentication to a SPA (Email/Password + Google Sign‑In)  
65. Recipe: Get Secrets Out of Your Repository (move keys to env vars and a secret store, scan history with Gitleaks, turn on push protection, rotate what leaked) [gitleaks](https://github.com/gitleaks/gitleaks)
66. Recipe: Encrypt Application Data with Envelope Encryption — AWS KMS or Google Cloud KMS in About 30 Lines [aws](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
67. Recipe: Encrypt Everything, Then Prove It — TLS 1.2+ and HSTS in Transit, Encrypted Volumes, Database and Backups at Rest, and the Screenshots an Auditor Will Ask For  
68. Recipe: Make an Existing Web App Mobile‑Friendly (viewport, responsive CSS, touch targets, installable PWA)  
69. Recipe: Deploy a SPA + API Using PaaS Only  
70. Recipe: Deploy a Serverless Full‑Stack SaaS (Auth + Payments) on a Budget [towardsaws](https://towardsaws.com/the-best-way-to-build-a-saas-web-app-for-free-427afeb43b20)
71. Recipe: Run a Security Test Pass Before Launch (TLS and header check, ZAP baseline scan, dependency audit, server audit with Lynis, fix‑and‑retest loop) [zaproxy](https://www.zaproxy.org/docs/docker/baseline-scan/)
72. Recipe: A SOC 2 Readiness Sprint for a Tiny Team (pick the criteria, write the six policies you actually need, turn on CloudTrail / audit logs and alerting, run an access review, collect evidence automatically, then start the observation window) [vanta](https://www.vanta.com/collection/soc-2/soc-2-compliance-checklist)
73. Checklist: Production‑Readiness for a Tiny Team  

## Part VIII – Growing Up Without Overcomplicating

74. When to Add More Environments (staging, preview, etc.) [reddit](https://www.reddit.com/r/devops/comments/4z41bs/any_favorite_best_practices_resources_for/)
75. When to Introduce IaC (Terraform / Pulumi / Serverless Framework) [invensislearning](https://www.invensislearning.com/blog/infrastructure-as-a-code-tutorial/)
76. Gradual Hardening: Policies, SSO, Compliance‑Lite  
77. Getting Audited: SOC 2 Type I vs Type II, Choosing an Auditor, the Observation Window, and Whether a Compliance‑Automation Platform Is Worth It (and how SOC 2 compares to ISO 27001) [drata](https://drata.com/grc-central/soc-2)
78. Handling Scale: Simple Sharding, Read Replicas, and Horizontal Scale  
79. Common Anti‑Patterns and “Overkill” to Avoid  

## Part IX – Appendices

A. Suggested “Starter Stacks” by Use Case and Cloud  
B. Infra Diagrams: Reference Architectures for Small Web & SaaS [usersnap](https://usersnap.com/blog/cloud-based-saas-architecture-fundamentals/)
C. Further Reading and Courses (DevOps, SRE, Cloud Architecture) [freecodecamp](https://www.freecodecamp.org/news/how-to-build-your-first-saas/)
D. Case Study — A Catalog Inventory Site: JSON Inventory → Python Build Scripts → Cloudflare Pages (Web3Forms quote requests, brand filter, cache busting, ~4 inventory types and 8 categories)  
E. Security Toolbox — Secret Stores, KMS/HSM Options, and Testing Tools Side by Side (AWS vs Google Cloud vs Azure vs self‑hosted; free vs paid scanners) [aws](https://aws.amazon.com/kms/)
F. SOC 2 Control Map — Each Trust Services Criterion Matched to the Concrete Thing You Configure in This Book (Caddy/TLS, KMS, IAM, CloudTrail, backups, CI/CD change management), Plus What You Inherit from Your Cloud Provider's Own Report [aicpa](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)
