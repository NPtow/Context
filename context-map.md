---
title: Context Map
type: index
status: active
updated_at: 2026-04-08
---

# Назначение

Этот файл — главный маршрутизатор для LLM.  
Его нужно читать первым почти всегда.

# Что сейчас активно

- `active venture`: `jjforrussia`
- `latest session`: [07_sessions/2026/2026-04-08.md](/Users/NIKITA/.codex/context/Context/07_sessions/2026/2026-04-08.md)
- `founder memory`: [01_founder/working-with-nikita.md](/Users/NIKITA/.codex/context/Context/01_founder/working-with-nikita.md)
- `core commands`: [00_system/commands.md](/Users/NIKITA/.codex/context/Context/00_system/commands.md)
- `task index`: [09_tasks/active-index.md](/Users/NIKITA/.codex/context/Context/09_tasks/active-index.md)

# Где что лежит

## Если нужен текущий проект
Читать в таком порядке:
1. [02_ventures/jjforrussia/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/README.md)
2. [02_ventures/jjforrussia/canonical/current-state.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/canonical/current-state.md)
3. [02_ventures/jjforrussia/working/hypotheses.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/working/hypotheses.md)
4. Последнюю проектную сессию из `evidence/sessions/`

## Если нужен старый проект `referalka`
Читать в таком порядке:
1. [02_ventures/referalka/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/referalka/README.md)
2. [02_ventures/referalka/canonical/current-state.md](/Users/NIKITA/.codex/context/Context/02_ventures/referalka/canonical/current-state.md)
3. [02_ventures/referalka/working/hypotheses.md](/Users/NIKITA/.codex/context/Context/02_ventures/referalka/working/hypotheses.md)
4. [02_ventures/referalka/evidence/sessions/2026-03-cycle1-summary.md](/Users/NIKITA/.codex/context/Context/02_ventures/referalka/evidence/sessions/2026-03-cycle1-summary.md)

## Если нужен общий контекст по Никите
Читать в таком порядке:
1. [01_founder/working-with-nikita.md](/Users/NIKITA/.codex/context/Context/01_founder/working-with-nikita.md)
2. [01_founder/preferences.md](/Users/NIKITA/.codex/context/Context/01_founder/preferences.md)
3. [01_founder/profile.md](/Users/NIKITA/.codex/context/Context/01_founder/profile.md)

## Если нужен доменный контекст
Читать в таком порядке:
1. [03_domains/recruiting/jack-and-jill-analysis.md](/Users/NIKITA/.codex/context/Context/03_domains/recruiting/jack-and-jill-analysis.md)
2. [03_domains/recruiting/russian-pm-hiring-notes.md](/Users/NIKITA/.codex/context/Context/03_domains/recruiting/russian-pm-hiring-notes.md)

## Если нужен temporal context
Читать в таком порядке:
1. текущий `canonical/current-state.md`
2. [06_decisions/decision-log.md](/Users/NIKITA/.codex/context/Context/06_decisions/decision-log.md)
3. [07_sessions/2026/2026-04-08.md](/Users/NIKITA/.codex/context/Context/07_sessions/2026/2026-04-08.md)
4. при необходимости архив или старые project sessions

## Если нужны задачи
Читать в таком порядке:
1. [09_tasks/active-index.md](/Users/NIKITA/.codex/context/Context/09_tasks/active-index.md)
2. `09_tasks/projects/<project>.md`
3. [09_tasks/task-schema.md](/Users/NIKITA/.codex/context/Context/09_tasks/task-schema.md), если нужно понять формат или добавить новую задачу

# Правила чтения

- Начинать с `canonical`, а не с сырого session log.
- Читать session logs только для понимания изменений и причин.
- Читать founder-memory только если вопрос связан с тем, как работать с Никитой или что для него устойчиво.
- Не читать архив по умолчанию.

# Что считается правдой

## Каноническая правда
- `02_ventures/*/canonical/`
- `01_founder/*.md`, если в них указано `status: active`
- `06_decisions/decision-log.md`

## Рабочая зона
- `02_ventures/*/working/`
- `05_playbooks/`
- `docs/`
- `09_tasks/`

## Evidence / raw memory
- `07_sessions/`
- `02_ventures/*/evidence/`

## Неактуальное
- `08_archive/`

# Когда задавать уточняющий вопрос

Если по диалогу неясно, какой проект активный, допустим ровно один короткий вопрос.

Пример:
`Уточню: обновлять рефералку или другой проект?`
