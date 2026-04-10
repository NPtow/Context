#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


SOURCE_ROOT = Path("/Users/NIKITA/.codex/skills")
HUB_ROOT = Path("/Users/NIKITA/.codex/context/Context/00_system/skill-hub")
LOCAL_ROOT = HUB_ROOT / "skills" / "local"
CLOUD_ROOT = HUB_ROOT / "skills" / "cloud"
REGISTRY_PATH = HUB_ROOT / "registry.json"
CATALOG_PATH = HUB_ROOT / "catalog.md"

EXCLUDED_DIR_NAMES = {".secrets", "__pycache__"}
EXCLUDED_FILE_NAMES = {".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc"}


@dataclass(frozen=True)
class SkillSource:
    slug: str
    relative_path: Path
    source_dir: Path


def make_slug(relative_path: Path) -> str:
    parts = []
    for part in relative_path.parts:
        cleaned = part.lstrip(".") or part
        parts.append(cleaned.replace(" ", "-"))
    return "--".join(parts)


def iter_skill_sources() -> list[SkillSource]:
    skills: list[SkillSource] = []
    for skill_file in sorted(SOURCE_ROOT.rglob("SKILL.md")):
        source_dir = skill_file.parent
        relative_path = source_dir.relative_to(SOURCE_ROOT)
        skills.append(
            SkillSource(
                slug=make_slug(relative_path),
                relative_path=relative_path,
                source_dir=source_dir,
            )
        )
    return skills


def should_exclude(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDED_DIR_NAMES:
            return True
        if part.startswith(".env"):
            return True
    if path.name in EXCLUDED_FILE_NAMES:
        return True
    if path.suffix in EXCLUDED_SUFFIXES:
        return True
    return False


def reset_local_mirror() -> None:
    LOCAL_ROOT.mkdir(parents=True, exist_ok=True)
    for child in LOCAL_ROOT.iterdir():
        if child.name == "README.md":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def copy_skill(source: SkillSource) -> Path:
    destination = LOCAL_ROOT / source.slug
    destination.mkdir(parents=True, exist_ok=True)

    for path in sorted(source.source_dir.rglob("*")):
        relative = path.relative_to(source.source_dir)
        if should_exclude(relative):
            continue
        target = destination / relative
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)

    return destination


def extract_frontmatter(skill_file: Path) -> dict:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}

    marker = "\n---\n"
    end_index = text.find(marker, 4)
    if end_index == -1:
        return {}

    raw = text[4:end_index].strip()
    result: dict[str, object] = {"_raw": raw}

    for line in raw.splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")

    return result


def list_files(skill_dir: Path) -> list[str]:
    files = [
        str(path.relative_to(skill_dir))
        for path in sorted(skill_dir.rglob("*"))
        if path.is_file()
    ]
    return files


def build_registry_entry(
    *,
    skill_dir: Path,
    namespace: str,
    managed_by_sync: bool,
    origin_path: str | None,
) -> dict:
    skill_file = skill_dir / "SKILL.md"
    frontmatter = extract_frontmatter(skill_file)
    files = list_files(skill_dir)

    return {
        "id": skill_dir.name,
        "name": frontmatter.get("name", skill_dir.name),
        "description": frontmatter.get("description", ""),
        "namespace": namespace,
        "origin_path": origin_path,
        "hub_path": str(skill_dir.relative_to(HUB_ROOT)),
        "managed_by_sync": managed_by_sync,
        "files": files,
        "has_agents": any(file.startswith("agents/") for file in files),
        "has_references": any(file.startswith("references/") for file in files),
        "has_scripts": any(file.startswith("scripts/") for file in files),
        "has_assets": any(file.startswith("assets/") for file in files),
        "frontmatter": frontmatter,
        "updated_at": date.today().isoformat(),
    }


def scan_namespace(root: Path, namespace: str, managed_by_sync: bool) -> list[dict]:
    entries: list[dict] = []
    if not root.exists():
        return entries

    for skill_file in sorted(root.rglob("SKILL.md")):
        skill_dir = skill_file.parent
        origin_path = None
        if namespace == "local":
            origin_slug = skill_dir.name
            source = next(
                (
                    source
                    for source in iter_skill_sources()
                    if source.slug == origin_slug
                ),
                None,
            )
            if source is not None:
                origin_path = str(source.source_dir)

        entries.append(
            build_registry_entry(
                skill_dir=skill_dir,
                namespace=namespace,
                managed_by_sync=managed_by_sync,
                origin_path=origin_path,
            )
        )
    return entries


def write_registry(entries: list[dict]) -> None:
    payload = {
        "title": "Skill Hub Registry",
        "updated_at": date.today().isoformat(),
        "skills": entries,
    }
    REGISTRY_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def format_extras(entry: dict) -> str:
    extras = []
    if entry["has_agents"]:
        extras.append("agents")
    if entry["has_references"]:
        extras.append("references")
    if entry["has_scripts"]:
        extras.append("scripts")
    if entry["has_assets"]:
        extras.append("assets")
    return ", ".join(extras) if extras else "SKILL.md only"


def render_section(title: str, entries: Iterable[dict]) -> list[str]:
    lines = [f"## {title}", ""]
    entry_list = list(entries)
    if not entry_list:
        lines.append("_Пока пусто._")
        lines.append("")
        return lines

    for entry in entry_list:
        lines.append(f"### `{entry['id']}`")
        lines.append(f"- name: `{entry['name']}`")
        lines.append(f"- description: {entry['description'] or '—'}")
        lines.append(f"- path: `{entry['hub_path']}`")
        lines.append(f"- extras: {format_extras(entry)}")
        if entry["origin_path"]:
            lines.append(f"- origin: `{entry['origin_path']}`")
        lines.append("")
    return lines


def write_catalog(entries: list[dict]) -> None:
    local_entries = [entry for entry in entries if entry["namespace"] == "local"]
    cloud_entries = [entry for entry in entries if entry["namespace"] == "cloud"]

    lines = [
        "---",
        "title: Skill Catalog",
        "type: index",
        "status: active",
        f"updated_at: {date.today().isoformat()}",
        "---",
        "",
        "# Как читать",
        "",
        "- Сначала открыть `README.md` этого skill hub.",
        "- Потом выбрать skill из этого каталога.",
        "- Затем перейти в соответствующую папку и читать `SKILL.md` плюс соседние `agents/`, `references/`, `scripts/`, `assets/`.",
        "",
        "# Быстрая сводка",
        "",
        f"- total skills: `{len(entries)}`",
        f"- local mirrored skills: `{len(local_entries)}`",
        f"- cloud skills: `{len(cloud_entries)}`",
        "",
    ]
    lines.extend(render_section(f"Local Mirrored Skills ({len(local_entries)})", local_entries))
    lines.extend(render_section(f"Cloud Skills ({len(cloud_entries)})", cloud_entries))

    CATALOG_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if not SOURCE_ROOT.exists():
        raise SystemExit(f"Source root does not exist: {SOURCE_ROOT}")

    reset_local_mirror()

    sources = iter_skill_sources()
    for source in sources:
        copy_skill(source)

    local_entries = [
        build_registry_entry(
            skill_dir=LOCAL_ROOT / source.slug,
            namespace="local",
            managed_by_sync=True,
            origin_path=str(source.source_dir),
        )
        for source in sources
    ]
    cloud_entries = scan_namespace(CLOUD_ROOT, namespace="cloud", managed_by_sync=False)
    entries = sorted(local_entries + cloud_entries, key=lambda item: (item["namespace"], item["id"]))

    write_registry(entries)
    write_catalog(entries)

    print(f"Mirrored {len(local_entries)} local skills into {LOCAL_ROOT}")
    print(f"Indexed {len(cloud_entries)} cloud skills from {CLOUD_ROOT}")
    print(f"Wrote {REGISTRY_PATH}")
    print(f"Wrote {CATALOG_PATH}")


if __name__ == "__main__":
    main()
