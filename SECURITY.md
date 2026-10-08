# Security policy

## Reporting a vulnerability

Report a vulnerability privately in the repository that owns the affected behavior. The
[repository map](docs/repositories.md) identifies each boundary. Do not open a public issue, discussion,
or pull request for an undisclosed vulnerability.

If the vulnerability crosses repository boundaries or the owner is unclear, use
[MP Platform private vulnerability reporting](https://github.com/panahister/mp-platform/security/advisories/new).

Include affected repositories and revisions, prerequisites, impact, a minimal reproduction, and any
known mitigation. Remove credentials, tokens, cookies, private URLs, personal data, and private design
material from the report.

The maintainer will investigate a complete report and coordinate disclosure after a fix or mitigation is
available. No fixed response time is promised for this proof-of-concept ecosystem.

## Supported versions

This repository contains documentation and navigation only. Its latest `main` is the supported source.
Runtime support and release lines are documented by each owning repository.

## Security boundary

The public repositories and their CI provide development evidence. Consumers remain responsible for
deployment-specific threat modeling, dependency maintenance, identity-provider policy, authorization,
TLS, secret and key custody, gateway policy, data protection, monitoring, incident response, and
vulnerability acceptance.

