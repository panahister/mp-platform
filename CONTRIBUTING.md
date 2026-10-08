# Contributing

Thank you for improving MP Platform. This repository is the ecosystem navigation and architecture hub;
it contains no runtime package or product behavior.

## Before proposing a change

- Identify the repository that owns the behavior. Use [the repository map](docs/repositories.md).
- Open runtime, CLI, template, product, identity, or edge changes in the owning repository.
- Keep this repository focused on cross-repository architecture, adoption, navigation, and evidence scope.
- Do not include credentials, private design files, customer assets, machine-local paths, or personal data.
- State what the proposal changes, who needs it, how ownership remains bounded, and how it will be proved.

## Local verification

The hub has no third-party build dependency. Run:

```bash
python3 scripts/verify.py
```

The verification checks required files, internal links, the machine-readable repository catalog, SVG
accessibility metadata, English-only public source, forbidden private-design identifiers, machine paths,
and symlinks.

## Pull requests

A pull request must include:

- the ecosystem problem and affected adoption path;
- the repository ownership impact;
- links to corresponding changes in other repositories, if any;
- the evidence supporting new capability or maturity claims;
- explicit limits and anything not run.

Do not turn a source gate into a production-readiness claim. If a platform, topology, failure mode, or
deployment profile was not run, say so plainly.

## Conduct and security

Follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Do not disclose vulnerabilities in a public issue;
use the private process in [SECURITY.md](SECURITY.md).

