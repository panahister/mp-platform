# Repository map

Use this map to find the repository that owns a change. Cross-repository changes should still be split by
ownership so each source boundary can be reviewed and verified independently.

## Foundations

| Repository | Primary audience | Owns | Does not own |
|---|---|---|---|
| [`mpcore`](https://github.com/panahister/mpcore) | .NET backend teams | Runtime packages, CLI, templates, transport and persistence abstractions, messaging guarantees, security primitives, observability, backend AI procedures | Product rules, product data, deployment approval |
| [`mpfrontend`](https://github.com/panahister/mpfrontend) | React and Next.js platform teams | Contract tooling, CLI, frontend runtime packages, BFF and realtime boundaries, design-source lifecycle, frontend AI procedures | Product branding, private design files, backend authorization, hosted operation |

## Product references

| Repository | Primary audience | Owns | Does not own |
|---|---|---|---|
| [`mpcore-tiffin-sample`](https://github.com/panahister/mpcore-tiffin-sample) | Teams evaluating service architecture | Nine food-delivery services, business rules, service-owned data, sagas, scenarios, local integration topology | Identity credentials, frontend behavior, reusable framework repairs |
| [`mpfrontend-tiffin-reference`](https://github.com/panahister/mpfrontend-tiffin-reference) | Teams evaluating product integration | Customer and operations applications, presentation composition, product adapters, public Tiffin theme, localization | Backend authorization, identity credentials, private customer design sources |
| [`mpcore-storefront-sample`](https://github.com/panahister/mpcore-storefront-sample) | Teams learning mixed backend shapes | Commerce modular monolith, Fulfillment and Analytics services, commerce business rules, backend scenarios | Frontend product, reusable framework repairs |

## Integration boundaries

| Repository | Primary audience | Owns | Does not own |
|---|---|---|---|
| [`tiffin-keycloak`](https://github.com/panahister/tiffin-keycloak) | Identity and security teams | Realm import, roles, resources, permissions, credentials, lifecycle-event provider, outbox publisher, authentication theme | Food-delivery business records, operations role editor, service authorization shortcuts |
| [`tiffin-apisix`](https://github.com/panahister/tiffin-apisix) | Edge and platform teams | Declarative routes, TLS input, correlation, local throttling, optional token pre-validation | Backend authorization decisions, payment exposure, APISIX fork behavior |

## This repository

[`mp-platform`](https://github.com/panahister/mp-platform) owns ecosystem navigation, cross-repository
architecture, adoption guidance, evidence boundaries, and the machine-readable repository catalog. It
contains no runtime package, product behavior, credentials, private design material, or deployment secret.

## Where to open an issue

- A runtime, CLI, template, or reusable package defect belongs in its foundation repository.
- A Tiffin or Storefront business defect belongs in the corresponding reference repository.
- A role, realm, lifecycle-event, or authentication-theme defect belongs in `tiffin-keycloak`.
- A route, gateway-rendering, or edge-policy defect belongs in `tiffin-apisix`.
- A broken ecosystem link, unclear adoption path, or cross-repository ownership question belongs here.
- A vulnerability must use the private reporting path in the affected repository, never a public issue.

