---
title: Tasks Layer
type: task-index
status: active
updated_at: 2026-04-08
---

# Назначение

Единый слой задач для всех проектов.

Он нужен, чтобы:
- не искать задачи по `status`, `sessions` и `open edges`;
- держать формализованный backlog;
- быстро отвечать на команды:
  - `поставить задачу`
  - `все задачи по проекту X`
  - `какие задачи сейчас есть`

# Структура

- [active-index.md](/Users/NIKITA/.codex/context/Context/09_tasks/active-index.md) — глобальный индекс активных задач
- [task-schema.md](/Users/NIKITA/.codex/context/Context/09_tasks/task-schema.md) — формат записи задач
- `projects/<project>.md` — полный backlog по конкретному проекту

# Как читать

## Если нужен общий список текущих задач
1. `09_tasks/active-index.md`

## Если нужны задачи конкретного проекта
1. `09_tasks/projects/<project>.md`

## Если нужно понять формат
1. `09_tasks/task-schema.md`
