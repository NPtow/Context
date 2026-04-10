---
title: Telegram Sourcing Operator Surface Session
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-11
---

# Что произошло

- Для `jjforrussia` собран отдельный reusable skill `telegram-hiring-contact-sourcing`.
- Skill опубликован как canonical cloud copy в `00_system/skill-hub/skills/cloud/...` и как локальная установленная копия в `~/.codex/skills/...`.
- Для skill собраны reference-файлы по Telethon setup, session and security, source triage, contact extraction, CSV schema и review buckets.
- Отдельно оформлена human-readable инструкция по Telegram-подключению и lifecycle соединения.

# Что это теперь даёт проекту

- Появился reusable operator surface для Telegram-based sourcing ops под `JJF-006`.
- Контур явно ограничен:
  - Telegram only
  - exact-only
  - evidence-backed rows only
  - no LinkedIn enrichment
  - no outreach logic
- Это support-layer для pilot ops, а не ядро продукта и не публичный user-facing surface.

# Что было отдельно проверено

- Исследована проблема app creation на `my.telegram.org`, включая `ERROR` и `[object Object]`.
- По официальным и community источникам собран минимальный troubleshooting readout.
- Позже в разговоре всплыл серый path через покупной / замороженный аккаунт, прокси и готовый scraper stack.
- Этот path не принят как project truth и не должен закрепляться в канонической версии skill.

# Что теперь считается правильным default

- собственный Telegram-аккаунт пользователя;
- `Telethon`;
- локальный session file;
- чтение только тех источников, к которым пользователь уже имеет доступ;
- `one row = one contact x one vacancy`;
- отсутствие row в accepted CSV, если нет evidence.

# Связанные файлы

- [../../canonical/current-state.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/canonical/current-state.md)
- [../sources/2026-04-11-telegram-api-setup-and-app-creation.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-11-telegram-api-setup-and-app-creation.md)
- [../../../../00_system/skill-hub/skills/cloud/telegram-hiring-contact-sourcing/SKILL.md](/Users/NIKITA/.codex/context/Context/00_system/skill-hub/skills/cloud/telegram-hiring-contact-sourcing/SKILL.md)
