<div align="center">

# Awesome Craft DevOps [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source, self-hostable alternatives to popular DevOps and hosting SaaS tools.

<img src="assets/craft-devops.svg" alt="Pixel-art DevOps scene with server racks, a dashboard and a deploy rocket" width="100%">

![Tools](https://img.shields.io/badge/tools-40-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-12-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-1.48M-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-DevOps?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-DevOps/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-DevOps?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-DevOps/commits/main)

</div>

Paid PaaS, observability and CI bills add up fast. Every project here can be self-hosted, and each entry names the paid tool it replaces. Check each project's licence before you host or resell it for clients.

Related list: [Awesome Craft](https://github.com/EdisonTKPcom/Awesome-Craft), open-source alternatives to popular SaaS tools.

## Contents

- [Dashboard](#dashboard)
- [PaaS and App Hosting](#paas-and-app-hosting)
- [Observability](#observability)
- [Error Tracking](#error-tracking)
- [Uptime and Status Pages](#uptime-and-status-pages)
- [CI, CD and Git](#ci-cd-and-git)
- [Container Registries](#container-registries)
- [Auth and Identity](#auth-and-identity)
- [Backend as a Service](#backend-as-a-service)
- [Secrets Management](#secrets-management)
- [Feature Flags](#feature-flags)
- [Tunnels and Networking](#tunnels-and-networking)
- [Workflow Orchestration](#workflow-orchestration)

## Dashboard

<table>
<tr>
<td align="center"><h2>40</h2>open-source tools</td>
<td align="center"><h2>50</h2>SaaS products replaced</td>
<td align="center"><h2>1.48M</h2>combined GitHub stars</td>
<td align="center"><h2>193.7k</h2>combined forks</td>
<td align="center"><h2>40/40</h2>pushed in the last 30 days</td>
<td align="center"><h2>8</h2>languages</td>
</tr>
</table>

Stats snapshot taken on 2026-11-15 from the GitHub API. Star badges next to each entry update live.

### 🏆 Leaderboard

<table>
<tr><th>Rank</th><th>Project</th><th>Replaces</th><th align="right">Stars</th><th></th></tr>
<tr><td align="center">🥇</td><td><b>Supabase</b></td><td>Firebase</td><td align="right">115.1k</td><td><code>████████████████████</code></td></tr>
<tr><td align="center">🥈</td><td><b>frp</b></td><td>Cloudflare Tunnel, ngrok</td><td align="right">110.6k</td><td><code>███████████████████</code></td></tr>
<tr><td align="center">🥉</td><td><b>Uptime Kuma</b></td><td>Pingdom, UptimeRobot, Statuspage</td><td align="right">94.3k</td><td><code>████████████████</code></td></tr>
<tr><td align="center">4</td><td><b>Netdata</b></td><td>Datadog, New Relic</td><td align="right">81.4k</td><td><code>██████████████</code></td></tr>
<tr><td align="center">5</td><td><b>Grafana</b></td><td>Datadog, New Relic</td><td align="right">77.9k</td><td><code>██████████████</code></td></tr>
<tr><td align="center">6</td><td><b>Prometheus</b></td><td>Datadog, CloudWatch</td><td align="right">67.6k</td><td><code>████████████</code></td></tr>
<tr><td align="center">7</td><td><b>Coolify</b></td><td>Vercel, Netlify, Heroku, Railway</td><td align="right">66.1k</td><td><code>███████████</code></td></tr>
<tr><td align="center">8</td><td><b>Gitea</b></td><td>GitHub, GitLab</td><td align="right">59.1k</td><td><code>██████████</code></td></tr>
<tr><td align="center">9</td><td><b>Appwrite</b></td><td>Firebase</td><td align="right">58.1k</td><td><code>██████████</code></td></tr>
<tr><td align="center">10</td><td><b>Apache Airflow</b></td><td>Astronomer, Amazon MWAA</td><td align="right">47.5k</td><td><code>████████</code></td></tr>
</table>


### Stars by category

```mermaid
pie showData
    title Combined GitHub stars by category
    "PaaS and App Hosting" : 166780
    "Observability" : 363380
    "Error Tracking" : 55171
    "Uptime and Status Pages" : 117651
    "CI, CD and Git" : 118677
    "Container Registries" : 47719
    "Auth and Identity" : 109470
    "Backend as a Service" : 173163
    "Secrets Management" : 67037
    "Feature Flags" : 30197
    "Tunnels and Networking" : 156300
    "Workflow Orchestration" : 77716
```

### Licences

![Apache-2.0](https://img.shields.io/badge/Apache--2.0-14-64748b?style=flat-square) ![Custom](https://img.shields.io/badge/Custom-9-64748b?style=flat-square) ![MIT](https://img.shields.io/badge/MIT-7-64748b?style=flat-square) ![AGPL-3.0](https://img.shields.io/badge/AGPL--3.0-5-64748b?style=flat-square) ![BSD-3-Clause](https://img.shields.io/badge/BSD--3--Clause-4-64748b?style=flat-square) ![GPL-3.0](https://img.shields.io/badge/GPL--3.0-1-64748b?style=flat-square)

"Custom" means GitHub couldn't match the licence to a standard one, often because of open-core or extra terms. Read it before you use the project commercially.

## PaaS and App Hosting

- [CapRover](https://github.com/caprover/caprover) - Heroku-style PaaS built on Docker, with one-click apps and SSL, an alternative to Heroku and DigitalOcean App Platform. ![Stars](https://img.shields.io/github/stars/caprover/caprover?style=flat-square&label=%E2%AD%90)
- [Coolify](https://github.com/coollabsio/coolify) - PaaS for deploying apps, databases and services from a single dashboard, an alternative to Vercel, Netlify, Heroku and Railway. ![Stars](https://img.shields.io/github/stars/coollabsio/coolify?style=flat-square&label=%E2%AD%90)
- [Dokku](https://github.com/dokku/dokku) - Small Docker-based PaaS that deploys from Git like Heroku, an alternative to Heroku. ![Stars](https://img.shields.io/github/stars/dokku/dokku?style=flat-square&label=%E2%AD%90)
- [Dokploy](https://github.com/Dokploy/dokploy) - Docker-based PaaS with Compose, databases and preview deploys, an alternative to Vercel, Heroku and Railway. ![Stars](https://img.shields.io/github/stars/Dokploy/dokploy?style=flat-square&label=%E2%AD%90)
- [Kamal](https://github.com/basecamp/kamal) - Deploy web apps to your own servers with Docker and zero-downtime rollouts, an alternative to Heroku, Render and Railway. ![Stars](https://img.shields.io/github/stars/basecamp/kamal?style=flat-square&label=%E2%AD%90)

## Observability

- [ClickStack](https://github.com/ClickHouse/ClickStack) - Observability platform, formerly HyperDX, that unifies session replay, logs, metrics, traces and errors, an alternative to Datadog and New Relic. ![Stars](https://img.shields.io/github/stars/ClickHouse/ClickStack?style=flat-square&label=%E2%AD%90)
- [Grafana](https://github.com/grafana/grafana) - Dashboards and visualization for metrics, logs and traces, an alternative to Datadog and New Relic. ![Stars](https://img.shields.io/github/stars/grafana/grafana?style=flat-square&label=%E2%AD%90)
- [Jaeger](https://github.com/jaegertracing/jaeger) - Distributed tracing for microservices, an alternative to Datadog and New Relic. ![Stars](https://img.shields.io/github/stars/jaegertracing/jaeger?style=flat-square&label=%E2%AD%90)
- [Loki](https://github.com/grafana/loki) - Log aggregation designed to be cost-effective and easy to operate, an alternative to Datadog, Logtail and Loggly. ![Stars](https://img.shields.io/github/stars/grafana/loki?style=flat-square&label=%E2%AD%90)
- [Netdata](https://github.com/netdata/netdata) - Real-time infrastructure monitoring with per-second metrics, an alternative to Datadog and New Relic. ![Stars](https://img.shields.io/github/stars/netdata/netdata?style=flat-square&label=%E2%AD%90)
- [OpenObserve](https://github.com/openobserve/openobserve) - Logs, metrics and traces with a focus on lower storage cost, an alternative to Datadog and Splunk. ![Stars](https://img.shields.io/github/stars/openobserve/openobserve?style=flat-square&label=%E2%AD%90)
- [Prometheus](https://github.com/prometheus/prometheus) - Metrics collection and alerting, the standard for Kubernetes monitoring, an alternative to Datadog and CloudWatch. ![Stars](https://img.shields.io/github/stars/prometheus/prometheus?style=flat-square&label=%E2%AD%90)
- [SigNoz](https://github.com/SigNoz/signoz) - APM, metrics, logs and traces in one OpenTelemetry-native platform, an alternative to Datadog and New Relic. ![Stars](https://img.shields.io/github/stars/SigNoz/signoz?style=flat-square&label=%E2%AD%90)
- [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) - Fast, cost-efficient time series database and long-term Prometheus storage, an alternative to Datadog and Grafana Cloud. ![Stars](https://img.shields.io/github/stars/VictoriaMetrics/VictoriaMetrics?style=flat-square&label=%E2%AD%90)

## Error Tracking

- [Highlight](https://github.com/highlight/highlight) - Error monitoring, session replay, logging and tracing in one platform, an alternative to Sentry, LogRocket and Datadog. ![Stars](https://img.shields.io/github/stars/highlight/highlight?style=flat-square&label=%E2%AD%90)
- [Sentry](https://github.com/getsentry/sentry) - Error tracking and performance monitoring you can self-host. Recent versions use the Functional Source Licence, so read it before you use it commercially, an alternative to Sentry Cloud, Bugsnag and Rollbar. ![Stars](https://img.shields.io/github/stars/getsentry/sentry?style=flat-square&label=%E2%AD%90)

## Uptime and Status Pages

- [Gatus](https://github.com/TwiN/gatus) - Automated health checks and status pages, configured as code, an alternative to Pingdom and Statuspage. ![Stars](https://img.shields.io/github/stars/TwiN/gatus?style=flat-square&label=%E2%AD%90)
- [Healthchecks](https://github.com/healthchecks/healthchecks) - Cron job and heartbeat monitoring, with alerts when jobs fail to check in, an alternative to Cronitor and Dead Man's Snitch. ![Stars](https://img.shields.io/github/stars/healthchecks/healthchecks?style=flat-square&label=%E2%AD%90)
- [Uptime Kuma](https://github.com/louislam/uptime-kuma) - Self-hosted monitoring with a polished UI, alerts and status pages, an alternative to Pingdom, UptimeRobot and Statuspage. ![Stars](https://img.shields.io/github/stars/louislam/uptime-kuma?style=flat-square&label=%E2%AD%90)

## CI, CD and Git

- [Argo CD](https://github.com/argoproj/argo-cd) - GitOps continuous delivery for Kubernetes, an alternative to GitHub Actions and Harness. ![Stars](https://img.shields.io/github/stars/argoproj/argo-cd?style=flat-square&label=%E2%AD%90)
- [Gitea](https://github.com/go-gitea/gitea) - Lightweight forge for Git hosting, issues, pull requests and packages, an alternative to GitHub and GitLab. ![Stars](https://img.shields.io/github/stars/go-gitea/gitea?style=flat-square&label=%E2%AD%90)
- [Jenkins](https://github.com/jenkinsci/jenkins) - Extensible automation server for building and deploying projects, an alternative to GitHub Actions and CircleCI. ![Stars](https://img.shields.io/github/stars/jenkinsci/jenkins?style=flat-square&label=%E2%AD%90)
- [Woodpecker CI](https://github.com/woodpecker-ci/woodpecker) - Lightweight CI engine that runs pipelines in containers, a community fork of Drone, an alternative to GitHub Actions and CircleCI. ![Stars](https://img.shields.io/github/stars/woodpecker-ci/woodpecker?style=flat-square&label=%E2%AD%90)

## Container Registries

- [Harbor](https://github.com/goharbor/harbor) - Container registry with vulnerability scanning, replication and access control, an alternative to Docker Hub and Amazon ECR. ![Stars](https://img.shields.io/github/stars/goharbor/harbor?style=flat-square&label=%E2%AD%90)
- [Verdaccio](https://github.com/verdaccio/verdaccio) - Lightweight private npm registry and proxy, an alternative to npm and GitHub Packages. ![Stars](https://img.shields.io/github/stars/verdaccio/verdaccio?style=flat-square&label=%E2%AD%90)

## Auth and Identity

- [Authelia](https://github.com/authelia/authelia) - Authentication portal for self-hosted apps, with SSO and two-factor auth, an alternative to Cloudflare Access and Auth0. ![Stars](https://img.shields.io/github/stars/authelia/authelia?style=flat-square&label=%E2%AD%90)
- [Authentik](https://github.com/goauthentik/authentik) - Flexible identity provider with SSO, MFA and application proxying, an alternative to Auth0 and Okta. ![Stars](https://img.shields.io/github/stars/goauthentik/authentik?style=flat-square&label=%E2%AD%90)
- [Keycloak](https://github.com/keycloak/keycloak) - Identity and access management with SSO, social login and user federation, an alternative to Auth0, Okta and Cognito. ![Stars](https://img.shields.io/github/stars/keycloak/keycloak?style=flat-square&label=%E2%AD%90)
- [Zitadel](https://github.com/zitadel/zitadel) - Cloud-native identity platform with a built-in management console, an alternative to Auth0 and Cognito. ![Stars](https://img.shields.io/github/stars/zitadel/zitadel?style=flat-square&label=%E2%AD%90)

## Backend as a Service

- [Appwrite](https://github.com/appwrite/appwrite) - Backend platform with auth, databases, storage and serverless functions, an alternative to Firebase. ![Stars](https://img.shields.io/github/stars/appwrite/appwrite?style=flat-square&label=%E2%AD%90)
- [Supabase](https://github.com/supabase/supabase) - Postgres-based backend with auth, APIs, storage and realtime, an alternative to Firebase. ![Stars](https://img.shields.io/github/stars/supabase/supabase?style=flat-square&label=%E2%AD%90)

## Secrets Management

- [Infisical](https://github.com/Infisical/infisical) - Secret management for developers, with versioning and per-environment sync, an alternative to Doppler and HashiCorp Vault. ![Stars](https://img.shields.io/github/stars/Infisical/infisical?style=flat-square&label=%E2%AD%90)
- [Vault](https://github.com/hashicorp/vault) - Secrets, encryption and identity-based access. Later versions use a Business Source licence, so read it before you use it commercially, an alternative to Doppler and AWS Secrets Manager. ![Stars](https://img.shields.io/github/stars/hashicorp/vault?style=flat-square&label=%E2%AD%90)

## Feature Flags

- [Flagsmith](https://github.com/Flagsmith/flagsmith) - Feature flags and remote config, with a friendly admin UI, an alternative to LaunchDarkly. ![Stars](https://img.shields.io/github/stars/Flagsmith/flagsmith?style=flat-square&label=%E2%AD%90)
- [GrowthBook](https://github.com/growthbook/growthbook) - Feature flags and A/B testing, with a stats engine for experiments, an alternative to LaunchDarkly and Optimizely. ![Stars](https://img.shields.io/github/stars/growthbook/growthbook?style=flat-square&label=%E2%AD%90)
- [Unleash](https://github.com/Unleash/unleash) - Feature-flag and experimentation platform, an alternative to LaunchDarkly. ![Stars](https://img.shields.io/github/stars/Unleash/unleash?style=flat-square&label=%E2%AD%90)

## Tunnels and Networking

- [frp](https://github.com/fatedier/frp) - Fast reverse proxy that exposes services behind NAT or firewalls, an alternative to Cloudflare Tunnel and ngrok. ![Stars](https://img.shields.io/github/stars/fatedier/frp?style=flat-square&label=%E2%AD%90)
- [Headscale](https://github.com/juanfont/headscale) - Self-hosted control server for Tailscale networks, an alternative to Tailscale and Cloudflare Zero Trust. ![Stars](https://img.shields.io/github/stars/juanfont/headscale?style=flat-square&label=%E2%AD%90)

## Workflow Orchestration

- [Apache Airflow](https://github.com/apache/airflow) - Platform to author, schedule and monitor data pipelines as DAGs, an alternative to Astronomer and Amazon MWAA. ![Stars](https://img.shields.io/github/stars/apache/airflow?style=flat-square&label=%E2%AD%90)
- [Kestra](https://github.com/kestra-io/kestra) - Orchestration for scheduled and event-driven workflows, defined in YAML, an alternative to Prefect and Airflow Cloud. ![Stars](https://img.shields.io/github/stars/kestra-io/kestra?style=flat-square&label=%E2%AD%90)

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

<div align="center">

If this list saved you a subscription, give it a ⭐ so others can find it.

</div>
