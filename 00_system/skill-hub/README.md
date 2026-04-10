---
title: Skill Hub
type: index
status: active
updated_at: 2026-04-10
---

# Что это

`skill-hub` — system-level слой, где локальные skills складываются в читаемый для LLM вид внутри самого `Context`.

Цель:
- дать cloud-агенту доступ к skill-контексту без чтения локальной файловой системы;
- хранить не только описания, но и реальные skill-папки;
- разделить sync-managed локальное зеркало и cloud-only пополнения.

# Что читать первым

1. этот `README.md`
2. [catalog.md](/Users/NIKITA/.codex/context/Context/00_system/skill-hub/catalog.md)
3. [registry.json](/Users/NIKITA/.codex/context/Context/00_system/skill-hub/registry.json), если нужен машинный индекс
4. конкретную папку skill в `skills/local/` или `skills/cloud/`

# Структура

- `skills/local/` — зеркало локальных skills из `/Users/NIKITA/.codex/skills`
- `skills/cloud/` — append-only зона для skills, добавленных cloud-агентом или вручную
- `catalog.md` — короткий LLM-friendly обзор всех skills в hub
- `registry.json` — машинный индекс по всем skills
- `scripts/sync_local_skills.py` — sync локального зеркала и пересборка индексов

# Что считается truth

- Для полного списка skills и их путей истины достаточно `registry.json`.
- Для короткого обзора сначала читать `catalog.md`.
- Для реального skill-контракта truth лежит в конкретной skill-папке, начиная с `SKILL.md`.
- `skills/local/` переписывается sync-скриптом.
- `skills/cloud/` sync-скрипт не трогает.

# Как обновлять

Локальный refresh:

```bash
python3 /Users/NIKITA/.codex/context/Context/00_system/skill-hub/scripts/sync_local_skills.py
```

Что делает sync:
- читает только `/Users/NIKITA/.codex/skills`;
- зеркалит найденные skill-папки в `skills/local/`;
- исключает `.secrets`, `.env*`, `__pycache__`, `*.pyc`, `.DS_Store`;
- пересобирает `catalog.md` и `registry.json`;
- не удаляет и не переписывает `skills/cloud/`.

# Как расширять hub из cloud

- Создать новую папку в `skills/cloud/<skill-slug>/`
- Положить туда как минимум `SKILL.md`
- При необходимости добавить `agents/`, `references/`, `scripts/`, `assets/`, `README*`, `LICENSE*`
- После этого локальный sync можно запускать безопасно: cloud-папки сохранятся и попадут в общий индекс
