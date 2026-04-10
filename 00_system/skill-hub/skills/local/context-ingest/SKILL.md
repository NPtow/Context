---
name: context-ingest
description: Use when the user asks to add a file or arbitrary information into the Context repo via phrases such as "пополни контекст", "добавь в контекст", "сохрани это в Context", "положи файл в контекст", "add this to context", or equivalent requests about importing notes, files, transcripts, source material, artifacts, or structured information.
---

# Context Ingest

Use this skill to place new information into the Context repository and explain the placement.

## Repository source of truth

Primary repository:
- `https://github.com/NPtow/Context.git`

Working checkout:
- `/Users/NIKITA/.codex/context/Context`

Before editing:
1. if the checkout exists, run `git -C /Users/NIKITA/.codex/context/Context pull --ff-only`
2. if missing, clone `https://github.com/NPtow/Context.git` into that path
3. create or update files only inside that repository checkout

## Read before editing

Always start with:
1. `/Users/NIKITA/.codex/context/Context/README.md`
2. `/Users/NIKITA/.codex/context/Context/context-map.md`
3. the active project `README.md` or the explicit target folder `README.md`
4. the nearest layer `README.md` for the chosen destination

Read these layer guides as needed:
- `02_ventures/*/artifacts/README.md` for reusable project docs
- `02_ventures/*/evidence/README.md` for source-bearing material and project session evidence
- `10_meetings/README.md` for calls, interviews, and transcripts
- `09_tasks/README.md` and `09_tasks/task-schema.md` for tasks
- `03_domains/*/README.md` for cross-project domain knowledge

## Required chat behavior

Before editing, send 1-2 short sentences that say:
- what target you believe this material belongs to
- which files you are about to create or update

If the target is genuinely ambiguous, ask one short clarifying question.

## Placement rules

- `02_ventures/<project>/canonical/`:
  Use only for stable current truth or decisions. Do not put raw files or bulky notes here.
- `02_ventures/<project>/working/`:
  Use for tentative hypotheses, drafts, open questions, and unstable framing.
- `02_ventures/<project>/artifacts/`:
  Use for reusable documents, templates, scripts, packs, and other stable working artifacts.
- `02_ventures/<project>/evidence/sources/`:
  Use for source-bearing external material, extracted notes from imported docs, or reusable evidence with lineage.
- `02_ventures/<project>/evidence/sessions/`:
  Use for session-specific summaries, project turns, and event notes that explain why truth changed.
- `10_meetings/<year>/`:
  Use for meeting notes, calls, interviews, and debriefs. If a full transcript must live in Context, store it separately in `10_meetings/<year>/transcripts/`.
- `09_tasks/projects/<project>.md` and `09_tasks/active-index.md`:
  Use for formal tasks.
- `03_domains/`:
  Use for cross-project knowledge that should survive the current venture.
- `01_founder/`:
  Use only for durable user preferences or stable founder patterns.

## File handling

- If the user gives a file path, do not blindly dump it into canonical files.
- Default to a Markdown note when structure is unclear.
- Preserve source lineage:
  - original absolute file path or URL
  - date
  - related project or domain
- Copy the original file into Context only when the file itself is a reusable artifact that should live there.
- Otherwise create a concise Markdown wrapper, source pack, meeting note, or artifact that points to the original file.
- Do not treat arbitrary local folders as the source of truth; the destination and final state must live in the `Context` repository.
- For transcripts, prefer:
  - a meeting note in `10_meetings/<year>/`
  - an optional cleaned transcript in `10_meetings/<year>/transcripts/` only if the user wants the full transcript inside Context

## Required final report

After edits, always tell the user:
- `Added to` — exact repo path(s)
- `Format` — note, source pack, artifact, transcript, task entry, canonical update, etc.
- `Why here` — why this layer fits better than neighboring ones
- `Also updated` — any index, task file, session, or canonical files changed alongside it

## Git workflow

After edits:
1. review changed files
2. `git add` relevant files
3. commit with a concise message
4. `git push`

Do not skip push unless the user explicitly says not to persist.

## Rules

- Keep one imported item = one clearly addressable artifact unless the user asked for a bundle.
- Do not promote raw evidence into canonical truth without a stable reason.
- Prefer repo `README.md` files as entrypoints before choosing a destination.
- If the best destination is still unclear after reading the relevant `README.md`, ask one short clarifying question.
