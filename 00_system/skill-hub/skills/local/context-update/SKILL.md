---
name: context-update
description: Use when the user asks to update their Context repo via natural-language commands such as "обновись", "обнови проект", "сохрани сессию", "архивируй проект", "обнови контекст", "поставить задачу", "добавь задачу", or equivalent Russian phrasing about saving new conversation context, refreshing project state, updating founder memory, or editing the formal task layer.
---

# Context Update

Use this skill when the user wants the Context repository to change.

## Source of truth

Prefer the local clone:
- `/Users/NIKITA/.codex/context/Context`

If it does not exist or is stale:
1. `git -C /Users/NIKITA/.codex/context/Context pull --ff-only`
2. if missing, clone `https://github.com/NPtow/Context.git` into that path

## Read before editing

Always start with:
1. `/Users/NIKITA/.codex/context/Context/context-map.md`
2. `/Users/NIKITA/.codex/context/Context/00_system/commands.md`
3. `/Users/NIKITA/.codex/context/Context/01_founder/working-with-nikita.md`
4. the active project `README.md` and `canonical/current-state.md` if the update is venture-level
5. `/Users/NIKITA/.codex/context/Context/docs/status.md` if the update is system-level
6. the target folder `README.md` if the user points to a folder or repo-relative path
7. `evidence/sources/README.md` if the update is source-bearing

## Required chat behavior

Before editing, send 1-2 short sentences that say:
- what you believe the active target is
- which files you are about to update

If the active project is unclear, ask one short clarifying question.

## Target and depth handling

Supported target forms:
- `по <project>`
- `в <folder>`
- `в <repo-relative-path>`

Resolve targets strictly in this order:
1. explicit repo-relative path
2. explicit project alias
3. unambiguous folder label inside the active project
4. implicit active project from dialogue context

Depth modes:
- `кратко`
- default `balanced`
- `глубоко` / `со всеми источниками`

Default mode is `balanced`: do not maximize compression, but also do not dump raw material into canonical.

## Command mapping

### `обновись`
Default meaning:
- update active project state
- append/update session log
- update founder memory only if a new stable pattern appeared
- update source-layer if new source-bearing material appeared

Possible write targets:
- `02_ventures/<active>/canonical/current-state.md`
- `02_ventures/<active>/working/hypotheses.md`
- `02_ventures/<active>/evidence/sessions/<date>.md`
- `02_ventures/<active>/evidence/sources/<date>-<slug>.md`
- `07_sessions/<year>/<date>.md`
- `06_decisions/decision-log.md`
- `01_founder/working-with-nikita.md` only for stable new patterns
- `docs/status.md` if the active work is about the Context system itself

Rules:
- session-layer updates whenever meaningful new material appeared;
- canonical updates only for stable truth or decisions;
- source-layer updates whenever the conversation or imported artifacts introduce reusable evidence or source lineage;
- if the user targets a folder/path, prefer writing into the nearest relevant layer rather than a repo-wide summary.

### `обнови проект`
Update only project-level files plus decision-log if needed. Do not update founder memory unless explicitly requested.

In default `balanced` mode this may include:
- project canonical
- project working file
- project evidence session
- project source pack when new sources matter

### `сохрани сессию`
Update only session files:
- `07_sessions/<year>/<date>.md`
- relevant project evidence session if needed
- relevant source pack if the session introduced source-bearing evidence

### `архивируй проект`
Move the project out of active use into `08_archive/`, preserve:
- a short project summary
- lessons learned
- final state

### `поставить задачу`
Default meaning:
- determine the target project
- add a formal task entry into `09_tasks/projects/<project>.md`
- update `09_tasks/active-index.md`
- update session log only if the task emerged from a meaningful planning or decision moment

Read before editing:
1. `09_tasks/README.md`
2. `09_tasks/task-schema.md`
3. `09_tasks/active-index.md`
4. `09_tasks/projects/<project>.md` if it exists

If the project is unclear, ask one short clarifying question.

Path behavior:
- explicit paths under `09_tasks/projects/` should be accepted without an extra clarification question.

## Git workflow

After edits:
1. review changed files
2. `git add` relevant files
3. commit with a concise message
4. `git push`

Do not skip push unless the user explicitly says not to persist.

## Rules

- Never overwrite canonical truth with tentative ideas from a single exchange.
- Prefer session logs for raw observations and canonical files for stable current truth.
- Update founder memory only when a pattern looks durable, not because of a one-off phrase.
- Default to `balanced` detail and explicit source lineage.
- Prefer folder `README.md` as the entrypoint for addressable folders.
- Treat source packs as first-class artifacts when they help future retrieval.
- For tasks, use the existing schema and keep one task = one concrete outcome.
