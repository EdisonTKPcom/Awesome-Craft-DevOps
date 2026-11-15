#!/usr/bin/env python3
import csv
import urllib.parse as U
from pathlib import Path

ROOT = Path(__file__).resolve().parent
S = {
    r[0]: dict(stars=int(r[1]), forks=int(r[2]), lic=r[3], lang=r[4], push=r[5])
    for r in csv.reader((ROOT / "stats.tsv").open(), delimiter="\t")
}
LICNAME = {"NOASSERTION": "Custom", "none": "None"}
AS = "2026-11-15"
ACTIVE_SINCE = "2026-10-15"

C = [
    (
        "PaaS and App Hosting",
        [
            ("CapRover", "caprover/caprover", "Heroku, DigitalOcean App Platform", "Heroku-style PaaS built on Docker, with one-click apps and SSL."),
            ("Coolify", "coollabsio/coolify", "Vercel, Netlify, Heroku, Railway", "PaaS for deploying apps, databases and services from a single dashboard."),
            ("Dokku", "dokku/dokku", "Heroku", "Small Docker-based PaaS that deploys from Git like Heroku."),
            ("Dokploy", "Dokploy/dokploy", "Vercel, Heroku, Railway", "Docker-based PaaS with Compose, databases and preview deploys."),
            ("Kamal", "basecamp/kamal", "Heroku, Render, Railway", "Deploy web apps to your own servers with Docker and zero-downtime rollouts."),
        ],
    ),
    (
        "Observability",
        [
            ("ClickStack", "ClickHouse/ClickStack", "Datadog, New Relic", "Observability platform, formerly HyperDX, that unifies session replay, logs, metrics, traces and errors."),
            ("Grafana", "grafana/grafana", "Datadog, New Relic", "Dashboards and visualization for metrics, logs and traces."),
            ("Jaeger", "jaegertracing/jaeger", "Datadog, New Relic", "Distributed tracing for microservices."),
            ("Loki", "grafana/loki", "Datadog, Logtail, Loggly", "Log aggregation designed to be cost-effective and easy to operate."),
            ("Netdata", "netdata/netdata", "Datadog, New Relic", "Real-time infrastructure monitoring with per-second metrics."),
            ("OpenObserve", "openobserve/openobserve", "Datadog, Splunk", "Logs, metrics and traces with a focus on lower storage cost."),
            ("Prometheus", "prometheus/prometheus", "Datadog, CloudWatch", "Metrics collection and alerting, the standard for Kubernetes monitoring."),
            ("SigNoz", "SigNoz/signoz", "Datadog, New Relic", "APM, metrics, logs and traces in one OpenTelemetry-native platform."),
            ("VictoriaMetrics", "VictoriaMetrics/VictoriaMetrics", "Datadog, Grafana Cloud", "Fast, cost-efficient time series database and long-term Prometheus storage."),
        ],
    ),
    (
        "Error Tracking",
        [
            ("Highlight", "highlight/highlight", "Sentry, LogRocket, Datadog", "Error monitoring, session replay, logging and tracing in one platform."),
            ("Sentry", "getsentry/sentry", "Sentry Cloud, Bugsnag, Rollbar", "Error tracking and performance monitoring you can self-host. Recent versions use the Functional Source Licence, so read it before you use it commercially."),
        ],
    ),
    (
        "Uptime and Status Pages",
        [
            ("Gatus", "TwiN/gatus", "Pingdom, Statuspage", "Automated health checks and status pages, configured as code."),
            ("Healthchecks", "healthchecks/healthchecks", "Cronitor, Dead Man's Snitch", "Cron job and heartbeat monitoring, with alerts when jobs fail to check in."),
            ("Uptime Kuma", "louislam/uptime-kuma", "Pingdom, UptimeRobot, Statuspage", "Self-hosted monitoring with a polished UI, alerts and status pages."),
        ],
    ),
    (
        "CI, CD and Git",
        [
            ("Argo CD", "argoproj/argo-cd", "GitHub Actions, Harness", "GitOps continuous delivery for Kubernetes."),
            ("Gitea", "go-gitea/gitea", "GitHub, GitLab", "Lightweight forge for Git hosting, issues, pull requests and packages."),
            ("Jenkins", "jenkinsci/jenkins", "GitHub Actions, CircleCI", "Extensible automation server for building and deploying projects."),
            ("Woodpecker CI", "woodpecker-ci/woodpecker", "GitHub Actions, CircleCI", "Lightweight CI engine that runs pipelines in containers, a community fork of Drone."),
        ],
    ),
    (
        "Container Registries",
        [
            ("Harbor", "goharbor/harbor", "Docker Hub, Amazon ECR", "Container registry with vulnerability scanning, replication and access control."),
            ("Verdaccio", "verdaccio/verdaccio", "npm, GitHub Packages", "Lightweight private npm registry and proxy."),
        ],
    ),
    (
        "Auth and Identity",
        [
            ("Authentik", "goauthentik/authentik", "Auth0, Okta", "Flexible identity provider with SSO, MFA and application proxying."),
            ("Authelia", "authelia/authelia", "Cloudflare Access, Auth0", "Authentication portal for self-hosted apps, with SSO and two-factor auth."),
            ("Keycloak", "keycloak/keycloak", "Auth0, Okta, Cognito", "Identity and access management with SSO, social login and user federation."),
            ("Zitadel", "zitadel/zitadel", "Auth0, Cognito", "Cloud-native identity platform with a built-in management console."),
        ],
    ),
    (
        "Backend as a Service",
        [
            ("Appwrite", "appwrite/appwrite", "Firebase", "Backend platform with auth, databases, storage and serverless functions."),
            ("Supabase", "supabase/supabase", "Firebase", "Postgres-based backend with auth, APIs, storage and realtime."),
        ],
    ),
    (
        "Secrets Management",
        [
            ("Infisical", "Infisical/infisical", "Doppler, HashiCorp Vault", "Secret management for developers, with versioning and per-environment sync."),
            ("Vault", "hashicorp/vault", "Doppler, AWS Secrets Manager", "Secrets, encryption and identity-based access. Later versions use a Business Source licence, so read it before you use it commercially."),
        ],
    ),
    (
        "Feature Flags",
        [
            ("Flagsmith", "Flagsmith/flagsmith", "LaunchDarkly", "Feature flags and remote config, with a friendly admin UI."),
            ("GrowthBook", "growthbook/growthbook", "LaunchDarkly, Optimizely", "Feature flags and A/B testing, with a stats engine for experiments."),
            ("Unleash", "Unleash/unleash", "LaunchDarkly", "Feature-flag and experimentation platform."),
        ],
    ),
    (
        "Tunnels and Networking",
        [
            ("frp", "fatedier/frp", "Cloudflare Tunnel, ngrok", "Fast reverse proxy that exposes services behind NAT or firewalls."),
            ("Headscale", "juanfont/headscale", "Tailscale, Cloudflare Zero Trust", "Self-hosted control server for Tailscale networks."),
        ],
    ),
    (
        "Workflow Orchestration",
        [
            ("Apache Airflow", "apache/airflow", "Astronomer, Amazon MWAA", "Platform to author, schedule and monitor data pipelines as DAGs."),
            ("Kestra", "kestra-io/kestra", "Prefect, Airflow Cloud", "Orchestration for scheduled and event-driven workflows, defined in YAML."),
        ],
    ),
]


def k(n):
    if n >= 1e6:
        return f"{n/1e6:.2f}M"
    if n >= 1000:
        return f"{n/1000:.1f}k"
    return str(n)


def anchor(n):
    return n.lower().replace(",", "").replace(" ", "-")



def alt(s):
    parts = [x.strip() for x in s.split(",")]
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    return ", ".join(parts[:-1]) + " and " + parts[-1]


tools = [t for _, ts in C for t in ts]
missing = [t[1] for t in tools if t[1] not in S]
if missing:
    raise SystemExit(f"missing stats for: {missing}")

tot = sum(S[t[1]]["stars"] for t in tools)
forks = sum(S[t[1]]["forks"] for t in tools)
langs = sorted({S[t[1]]["lang"] for t in tools if S[t[1]]["lang"] not in ("", "none")})
saas = len({x.strip() for t in tools for x in t[2].split(",")})
active = sum(1 for t in tools if S[t[1]]["push"] >= ACTIVE_SINCE)

o = []
o.append(
    f"""<div align="center">

# Awesome Craft DevOps [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source, self-hostable alternatives to popular DevOps and hosting SaaS tools.

<img src="assets/craft-devops.svg" alt="Pixel-art DevOps scene with server racks, a dashboard and a deploy rocket" width="100%">

![Tools](https://img.shields.io/badge/tools-{len(tools)}-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-{len(C)}-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-{k(tot)}-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-DevOps?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-DevOps/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-DevOps?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-DevOps/commits/main)

</div>

Paid PaaS, observability and CI bills add up fast. Every project here can be self-hosted, and each entry names the paid tool it replaces. Check each project's licence before you host or resell it for clients.

Related list: [Awesome Craft](https://github.com/EdisonTKPcom/Awesome-Craft), open-source alternatives to popular SaaS tools.

## Contents
"""
)
o += ["- [Dashboard](#dashboard)"] + [f"- [{n}](#{anchor(n)})" for n, _ in C]
o.append("\n## Dashboard\n")
o.append(
    f"""<table>
<tr>
<td align="center"><h2>{len(tools)}</h2>open-source tools</td>
<td align="center"><h2>{saas}</h2>SaaS products replaced</td>
<td align="center"><h2>{k(tot)}</h2>combined GitHub stars</td>
<td align="center"><h2>{k(forks)}</h2>combined forks</td>
<td align="center"><h2>{active}/{len(tools)}</h2>pushed in the last 30 days</td>
<td align="center"><h2>{len(langs)}</h2>languages</td>
</tr>
</table>

Stats snapshot taken on {AS} from the GitHub API. Star badges next to each entry update live.
"""
)
top = sorted(tools, key=lambda t: -S[t[1]]["stars"])[:10]
mx = S[top[0][1]]["stars"]
o.append(
    '### 🏆 Leaderboard\n\n<table>\n<tr><th>Rank</th><th>Project</th><th>Replaces</th><th align="right">Stars</th><th></th></tr>'
)
for i, t in enumerate(top, 1):
    s = S[t[1]]["stars"]
    bar = "█" * max(1, round(s / mx * 20))
    medal = ["🥇", "🥈", "🥉"][i - 1] if i < 4 else i
    o.append(
        f'<tr><td align="center">{medal}</td><td><b>{t[0]}</b></td><td>{t[2]}</td><td align="right">{k(s)}</td><td><code>{bar}</code></td></tr>'
    )
o.append("</table>\n")
o.append("\n### Stars by category\n\n```mermaid\npie showData\n    title Combined GitHub stars by category")
for n, ts in C:
    o.append(f'    "{n}" : {sum(S[t[1]]["stars"] for t in ts)}')
o.append("```\n")
lc = {}
for t in tools:
    L = LICNAME.get(S[t[1]]["lic"], S[t[1]]["lic"])
    lc[L] = lc.get(L, 0) + 1
o.append(
    "### Licences\n\n"
    + " ".join(
        f"![{L}](https://img.shields.io/badge/{U.quote(L.replace('-', '--'))}-{c}-64748b?style=flat-square)"
        for L, c in sorted(lc.items(), key=lambda x: -x[1])
    )
    + "\n\n\"Custom\" means GitHub couldn't match the licence to a standard one, often because of open-core or extra terms. Read it before you use the project commercially.\n"
)
for n, ts in C:
    o.append(f"## {n}\n")
    for t in sorted(ts, key=lambda t: t[0].lower()):
        o.append(
            f"- [{t[0]}](https://github.com/{t[1]}) - {t[3][:-1]}, an alternative to {alt(t[2])}. ![Stars](https://img.shields.io/github/stars/{t[1]}?style=flat-square&label=%E2%AD%90)"
        )
    o.append("")
o.append(
    "## Contributing\n\nContributions welcome! Read the [contribution guidelines](contributing.md) first.\n\n"
    '<div align="center">\n\n'
    "If this list saved you a subscription, give it a ⭐ so others can find it.\n\n"
    "</div>\n"
)
(ROOT / "README.md").write_text("\n".join(o))
print(f"wrote README.md tools={len(tools)} stars={tot} forks={forks} langs={len(langs)} active={active}/{len(tools)} saas={saas}")
