---
title: Task Schema
type: protocol
status: active
updated_at: 2026-04-08
---

# Формат задачи

Каждая задача должна быть записана в одной строке таблицы и, при необходимости, иметь короткий detail block.

## Поля
- `Task ID` — уникальный ID
- `Project` — проект
- `Title` — короткое название
- `Status` — `now | next | blocked | done | later`
- `Priority` — `P0 | P1 | P2 | P3`
- `Type` — `research | product | ops | growth | infra | context`
- `Updated` — дата последнего обновления
- `Definition of done` — краткий критерий завершения

## Правила
- Одна задача = один конкретный outcome.
- Название должно быть коротким и проверяемым.
- Если задача расплывчатая, сначала дробить ее, потом добавлять.
- `Status` отвечает за порядок работы, а не за важность.
- `Priority` отвечает за важность, а не за порядок.

## Пример

| Task ID | Project | Title | Status | Priority | Type | Updated | Definition of done |
|---|---|---|---|---|---|---|---|
| RFL-001 | referalka | Описать taxonomy PM-ролей | now | P0 | research | 2026-04-08 | В Context есть taxonomy v1 по core/growth/platform/0→1 |

# Командная логика

## `поставить задачу`
- определить проект;
- создать новую строку в `09_tasks/projects/<project>.md`;
- обновить `09_tasks/active-index.md`;
- если проект неизвестен, задать один короткий вопрос.

## `все задачи по проекту X`
- читать `09_tasks/projects/<project>.md`;
- по умолчанию показывать только `now`, `next`, `blocked`;
- `done` показывать только по запросу.
