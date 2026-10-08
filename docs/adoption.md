# Adoption paths

Adopt the smallest useful boundary first. Each path below has a bounded evaluation and an explicit point
where a team can stop without inheriting the rest of the ecosystem.

## Path A: backend foundation

Choose this path when the product needs .NET architecture and does not need MP Frontend.

1. Install MP Core CLI and templates at one immutable version.
2. Generate a disposable backend with the intended shape, transports, messaging, cache, and audit choices.
3. Select `--ai-tooling codex`, `claude`, or `both` if repository-scoped agent procedures are in scope.
4. Implement one real vertical slice with a business rule and a negative case, using the named generated
   skill rather than an ad hoc architecture prompt.
5. Run the generated test and architecture gates.
6. Compare the result with the Storefront or Tiffin backend reference.

**Accept when:** the team can explain the transaction, security, transport, message, idempotency, and
observability behavior of the slice and reproduce its checks from a clean clone.

**Stop when:** the generated architecture does not fit the product boundary. The evaluation does not
require MP Frontend or Tiffin.

## Path B: frontend foundation

Choose this path when the product already has APIs and may already own a Figma/DLS source.

1. Verify MP Frontend from source and run the independent-consumer gate.
2. Choose `none` for code-first design or `existing` for an approved consumer-owned export.
3. Dry-run, install, and check the Base AI skill profile for Codex, Claude Code, or both when agent
   procedures are in scope.
4. Capture one reviewed API contract and generate one bounded read or request flow.
5. Put provider tokens behind the Security BFF and expose an opaque application session.
6. Implement one product-owned adapter and prove generated drift is detected.

**Accept when:** a clean consumer can regenerate and verify the same artifacts, the browser contains no
provider token or internal origin, and product code remains outside generated ownership.

**Stop when:** the build-time contract or runtime trust model does not fit. The evaluation does not
require MP Core.

The MVP does not offer a Community DLS mode. This is an explicit contract, not missing setup
documentation. Read [Design-source paths](design-sources.md) before creating the consumer workspace.

## Path C: end-to-end platform

Choose this path when the team wants both foundations and needs evidence across identity, edge, frontend,
services, messaging, data, media, and realtime behavior.

1. Run the Tiffin backend scenario matrices with the default RustFS profile.
2. Run the customer and operations applications through the Security BFF and APISIX.
3. Complete one order from catalog discovery through payment, kitchen, dispatch, tracking, delivery, and
   notification.
4. Exercise a negative path: duplicate request, payment decline, unavailable courier, tenant boundary,
   stale identity claim, or service outage.
5. Repeat the media boundary with SeaweedFS if the alternative store is in scope.

**Accept when:** the team can trace authority, data ownership, transaction boundaries, compensation, and
observable failure behavior across the complete journey.

**Stop when:** a foundation boundary is valuable on its own. Full-stack adoption is not required.

## Production continuation

The public repositories provide source and reference evidence. A production program still owns:

- threat modeling, vulnerability disposition, secret and key custody;
- TLS and certificate automation;
- HA, backup/restore, load, soak, regional failover, and capacity evidence;
- accessibility, privacy, data retention, regulatory, and operational acceptance;
- version governance, dependency maintenance, incident response, and SLOs.

Do not convert a passing POC gate into a deployment approval without this continuation.

For both foundation paths, [AI engineering](ai-engineering.md) defines the procedure catalog, installation
model, human authority, evidence boundary, and the difference between source portability and model parity.
