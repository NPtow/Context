---
name: context-query
description: Use when the user asks to read or summarize the Context repo, or writes `контекст`, `контеекст`, `context`, or another language equivalent and expects repo-grounded answers only. Triggers on requests such as "покажи контекст проекта", "что изменилось", "покажи память обо мне", "сравни с прошлым", "дай сводку", "все задачи по проекту X", "какие задачи сейчас есть", "show context", "use only Context", and similar requests about current project context, founder memory, deltas, or task lists.
---

# Context Query

Use this skill to answer read-only questions against the Context repository.

## Hard boundary

- Use only the `Context` repository as the source.
- Read from the checked-out repository at `/Users/NIKITA/.codex/context/Context` after syncing it when needed.
- Do not browse the web.
- Do not read the current workspace, desktop files, or any repo other than `Context` to answer a Context request.
- Do not fill gaps from general model memory.
- If the answer is missing in Context, say so plainly and list the best next repo files instead of guessing.

## Repository source of truth

Primary repository:
- `https://github.com/NPtow/Context.git`

Working checkout:
- `/Users/NIKITA/.codex/context/Context`

Before reading:
1. if the checkout exists, run `git -C /Users/NIKITA/.codex/context/Context pull --ff-only`
2. if the checkout is missing, clone `https://github.com/NPtow/Context.git` into that path
3. read only files that belong to that repository checkout

## First files to read

Always start with:
1. `/Users/NIKITA/.codex/context/Context/README.md`
2. `/Users/NIKITA/.codex/context/Context/context-map.md`
3. `/Users/NIKITA/.codex/context/Context/00_system/commands.md`

Then follow the retrieval path from `README.md`, `context-map.md`, and the resolved folder `README.md`.

If the target is a folder or path, its `README.md` is a mandatory first read before any deeper file.

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

If the target is a folder or path, read that folder's `README.md` first.

Depth modes:
- `кратко` — nearest canonical / index files only
- default `balanced` — truth + nearby evidence + nearby sources
- `глубоко` / `со всеми источниками` — source packs, related sessions, adjacent folders

For Context answers, propose only repo-internal sources discovered through that read chain.

## Command mapping

### `покажи контекст проекта`
Read only:
1. `README.md`
2. `context-map.md`
3. the resolved project, folder, or path `README.md`
3. nearest `canonical/current-state.md` if the target is venture-level
4. nearest `working/hypotheses.md` if it exists
5. `evidence/README.md` or relevant folder README when present
6. nearest source-layer in default `balanced` mode

Return:
- `Answer`
- `Files used`
- `Next repo sources`

### `что изменилось`
Read only:
1. `README.md`
2. `context-map.md`
3. `06_decisions/decision-log.md`
4. latest `07_sessions/...`
5. latest project or folder session if needed
6. relevant folder README if target is explicit
7. related sources if the change is source-bearing

Return:
- `Answer`
- `Files used`
- `Next repo sources`

### `покажи память обо мне`
Read only:
1. `01_founder/working-with-nikita.md`
2. `01_founder/preferences.md`
3. `01_founder/profile.md`

Return founder-only context unless the user explicitly broadens scope.

### `сравни с прошлым`
Read:
1. `README.md`
2. `context-map.md`
3. current canonical file
4. `06_decisions/decision-log.md`
5. relevant session logs
6. relevant folder README if target is explicit
7. archive only if needed
8. source packs if the comparison depends on source lineage

### `все задачи по проекту X`
Read only:
1. `09_tasks/projects/<project>.md`
2. `09_tasks/task-schema.md` only if format clarification is needed

Return only active tasks by default:
- `now`
- `next`
- `blocked`

### `какие задачи сейчас есть`
Read only:
1. `09_tasks/active-index.md`

Return active tasks across projects, preferably grouped by project if that keeps the answer short.

## Rules

- Default to `balanced` detail, not maximum compression.
- Prefer `README.md`, canonical, and folder-index files as entrypoints, then expand into evidence and sources.
- Treat sources as first-class only when they are inside Context and materially support the answer.
- Ask one short clarifying question only if the active project is genuinely ambiguous.
- Never cite or suggest anything outside the Context repo in this skill.
- When the user asks for sources, return repo file paths only.
- Do not edit the repo in this skill unless the user explicitly changes the task from query to update.
