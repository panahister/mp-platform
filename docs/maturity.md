# Maturity and evidence

MP Platform is a public source POC and reusable foundation with runnable references. Its repositories use
verification gates and name the scope of those gates. A green gate is evidence for what it executed, not
a universal production certificate.

## Current evidence

| Area | Evidence available |
|---|---|
| MP Core | Published `0.9.3` NuGet cohort; locked restore, API compatibility baseline, warnings-as-errors build, package tests, integration tests, templates, CLI, and reference-consumer verification |
| MP Frontend | Frozen install; lint, typecheck, test and build targets; dependency audit; immutable local package cohort; fresh independent Nx consumer; Redis-backed multi-replica session scenarios; deliberate negative controls |
| Backend AI procedures | Ten generated product skills use one canonical body with Codex and Claude Code discovery; Storefront records one controlled task in which both agents changed the same seven files while preserving the architecture |
| Frontend AI procedures | Eighteen finite source procedures; CLI and format tests cover catalog, repository-local installation, dry-run, ownership collision, locking, rollback conflict, and thirty-six installed Codex/Claude files for the combined profile |
| Tiffin AI routing | Ten root `tiffin-*` skills for both agents route work to the owning one of nine services; every service carries all ten canonical MP Core product procedures. The sixteen scenario stories prove system behavior, not model parity |
| Design-source lifecycle | Code-first `none` and consumer-owned `existing` paths, legacy-template refusal, attachment/status, reviewed candidate lifecycle, path/symlink controls, writer locking, ownership, drift, and isolated guard removals |
| Storefront | Release build with zero warnings or errors; 290 source tests in the current publication verification; complete edge-off and Keycloak scenario jobs on `main` |
| Tiffin backend | 313 Release tests in the current publication verification; full RustFS/edge-off and SeaweedFS/Keycloak-edge GitHub scenario matrices; sixteen local business scenarios with 286 checks |
| Tiffin frontend | Frozen install and nineteen uncached lint, typecheck, test, build, generated-contract, and design-theme targets |
| Tiffin identity | Repository and localization tests, source-built provider, authorization seed, signup-to-business projection, reconciliation, English/Arabic and LTR/RTL theme behavior |
| Tiffin edge | Declarative render and route-policy checks; backend-only and Keycloak edge-validation profiles exercised by complete backend scenarios |

Counts describe the recorded publication checkpoint and may grow. The owning repository and its latest CI
run are authoritative for the current count.

The AI evidence establishes canonical procedure and installation behavior for the tested cases. It does
not establish behavioral equivalence between models, autonomous product correctness, or automatic visual,
security, architecture, commit, release, or deployment acceptance.

## Status language

| Label | Meaning |
|---|---|
| **Published package** | An immutable package exists in its named registry and carries its own release evidence |
| **Public source POC** | Source is public and its documented gates pass; stable package and production guarantees are not implied |
| **Reference POC** | A real product path runs against the foundations and demonstrates bounded positive and negative cases |
| **Fits by standard** | The contract is standards-based, but this project has not run that particular product or topology |
| **Not run** | No compatibility or readiness claim is made |

## Gates that remain deployment-specific

- production threat model and vulnerability acceptance;
- managed secrets, key rotation, TLS, and certificate automation;
- multi-instance and multi-region HA;
- load, soak, failover, backup, restore, and capacity qualification;
- formal accessibility and device/browser acceptance;
- privacy, retention, regulatory, and data-residency controls;
- WAF, bot policy, distributed rate limits, and production gateway topology;
- production observability operations, incident response, and SLOs;
- stable MP Frontend package-registry publication and compatibility policy.
- a licensed, sanitized, versioned MP Community DLS and its corresponding CLI release; this path is not
  part of the MVP.

## Evidence rule

When documentation claims a behavior, it should identify the test, scenario, or observed run that supports
the claim. If a check is intended to guard a failure, maintainers should demonstrate that the check fails
when the guarded behavior is deliberately broken. Unsupported assumptions belong under limitations, not
under capabilities.
