#!/usr/bin/env python3
"""Verify the public MP Platform navigation repository without third-party dependencies."""

from __future__ import annotations

import json
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "README.md",
    "LICENSE",
    "NOTICE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CODE_OF_CONDUCT.md",
    "repository-catalog.json",
    "docs/architecture.md",
    "docs/adoption.md",
    "docs/ai-engineering.md",
    "docs/design-sources.md",
    "docs/local-workflows.md",
    "docs/repositories.md",
    "docs/maturity.md",
    "docs/images/hero.svg",
    "docs/images/ai-engineering-light.svg",
    "docs/images/ai-engineering-dark.svg",
    "docs/images/backend-skills-light.svg",
    "docs/images/backend-skills-dark.svg",
    "docs/images/design-sources-light.svg",
    "docs/images/design-sources-dark.svg",
    "docs/images/skill-lifecycle-light.svg",
    "docs/images/skill-lifecycle-dark.svg",
    "docs/images/tiffin-ai-reference-light.svg",
    "docs/images/tiffin-ai-reference-dark.svg",
    "docs/images/ecosystem-light.svg",
    "docs/images/ecosystem-dark.svg",
    "docs/images/README.md",
    ".github/workflows/ci.yml",
}

EXPECTED_REPOSITORIES = {
    "mpcore",
    "mpfrontend",
    "mpcore-tiffin-sample",
    "mpfrontend-tiffin-reference",
    "tiffin-keycloak",
    "tiffin-apisix",
    "mpcore-storefront-sample",
}

TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".svg", ".py", ".txt"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
ARABIC_SCRIPT = re.compile(r"[\u0600-\u06ff]")
ARTWORK_ROW = re.compile(r"\| `([^`]+\.svg)` .* \| `([a-f0-9]{64})` \|")

FORBIDDEN_PUBLIC_TEXT = {
    "/" + "Users" + "/": "machine-local macOS path",
    "file" + "://": "machine-local file URL",
    "Zar" + "X": "private consumer brand",
    "IykZ1LCb9Ubu7" + "gPPFYBhpY": "private design-file identifier",
    "xCv9hpyi1WV9" + "zzFxS1DT71": "parked design-copy identifier",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def public_text_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__"}
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not ignored_parts.intersection(path.parts)
    )


def verify_required_files(failures: list[str]) -> None:
    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            fail(f"required file is missing: {relative}", failures)


def verify_public_boundary(failures: list[str]) -> None:
    for path in public_text_files():
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if ARABIC_SCRIPT.search(text):
            fail(f"Arabic/Persian script is not allowed in public source: {relative}", failures)
        for candidate, description in FORBIDDEN_PUBLIC_TEXT.items():
            if candidate in text:
                fail(f"{description} found in {relative}: {candidate}", failures)

    for path in ROOT.rglob("*"):
        if path.is_symlink():
            fail(f"public repository must not contain a symlink: {path.relative_to(ROOT)}", failures)


def normalize_markdown_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        target = target.split(" ", 1)[0]
    return unquote(target)


def verify_markdown_links(failures: list[str]) -> None:
    markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = normalize_markdown_target(match.group(1))
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative_target = target.split("#", 1)[0].split("?", 1)[0]
            if not relative_target:
                continue
            resolved = (path.parent / relative_target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link leaves the repository: {path.relative_to(ROOT)} -> {target}", failures)
                continue
            if not resolved.exists():
                fail(f"broken local link: {path.relative_to(ROOT)} -> {target}", failures)


def verify_catalog(failures: list[str]) -> None:
    path = ROOT / "repository-catalog.json"
    if not path.is_file():
        return
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"repository-catalog.json is invalid JSON: {error}", failures)
        return

    if document.get("schemaVersion") != 1:
        fail("repository catalog must use schemaVersion 1", failures)

    repositories = document.get("repositories")
    if not isinstance(repositories, list):
        fail("repository catalog must contain a repositories array", failures)
        return

    names: list[str] = []
    for index, repository in enumerate(repositories):
        if not isinstance(repository, dict):
            fail(f"repository catalog entry {index} must be an object", failures)
            continue
        name = repository.get("name")
        url = repository.get("url")
        if not isinstance(name, str) or not name:
            fail(f"repository catalog entry {index} has no name", failures)
            continue
        names.append(name)
        expected_url = f"https://github.com/panahister/{name}"
        if url != expected_url:
            fail(f"repository {name} must use canonical URL {expected_url}", failures)
        for field in ("group", "role", "maturity"):
            if not isinstance(repository.get(field), str) or not repository[field]:
                fail(f"repository {name} has no {field}", failures)

    if len(names) != len(set(names)):
        fail("repository catalog contains duplicate names", failures)
    if set(names) != EXPECTED_REPOSITORIES:
        missing = sorted(EXPECTED_REPOSITORIES - set(names))
        extra = sorted(set(names) - EXPECTED_REPOSITORIES)
        fail(f"repository catalog mismatch; missing={missing}, extra={extra}", failures)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    repository_map = (ROOT / "docs/repositories.md").read_text(encoding="utf-8")
    for name in sorted(EXPECTED_REPOSITORIES):
        canonical_url = f"https://github.com/panahister/{name}"
        if canonical_url not in readme:
            fail(f"README does not link to {canonical_url}", failures)
        if canonical_url not in repository_map:
            fail(f"repository map does not link to {canonical_url}", failures)


def verify_svg_accessibility(failures: list[str]) -> None:
    for path in sorted((ROOT / "docs/images").glob("*.svg")):
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as error:
            fail(f"invalid SVG {path.relative_to(ROOT)}: {error}", failures)
            continue
        if not root.get("viewBox"):
            fail(f"SVG has no viewBox: {path.relative_to(ROOT)}", failures)
        if root.get("role") != "img":
            fail(f"SVG must declare role=img: {path.relative_to(ROOT)}", failures)
        if not root.get("aria-label"):
            fail(f"SVG has no aria-label: {path.relative_to(ROOT)}", failures)
        title_tag = "{http://www.w3.org/2000/svg}title"
        title = root.find(title_tag)
        if title is None or not (title.text or "").strip():
            fail(f"SVG has no non-empty title: {path.relative_to(ROOT)}", failures)


def verify_artwork_manifest(failures: list[str]) -> None:
    directory = ROOT / "docs/images"
    manifest = (directory / "README.md").read_text(encoding="utf-8")
    recorded = dict(ARTWORK_ROW.findall(manifest))
    artwork = {path.name for path in directory.glob("*.svg")}
    if set(recorded) != artwork:
        missing = sorted(artwork - set(recorded))
        extra = sorted(set(recorded) - artwork)
        fail(f"artwork manifest mismatch; missing={missing}, extra={extra}", failures)
    for name, expected in sorted(recorded.items()):
        path = directory / name
        if not path.is_file():
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            fail(f"artwork digest mismatch: {name}; expected={expected}, actual={actual}", failures)


def main() -> int:
    failures: list[str] = []
    verify_required_files(failures)
    verify_public_boundary(failures)
    verify_markdown_links(failures)
    verify_catalog(failures)
    verify_svg_accessibility(failures)
    verify_artwork_manifest(failures)

    if failures:
        print("MP Platform verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"MP Platform verification passed: {len(public_text_files())} public text files checked")
    print(f"Repository catalog: {len(EXPECTED_REPOSITORIES)} canonical repositories")
    print("Public boundary: English-only source, no private design identifiers, no machine paths")
    return 0


if __name__ == "__main__":
    sys.exit(main())
