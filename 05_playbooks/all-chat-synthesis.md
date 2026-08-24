# All-Chat Synthesis

## Purpose

Процедура для регулярной automation `обновись ко всем чатам`.

Цель не в том, чтобы пересказать все локальные Codex-чаты, а в том, чтобы найти durable deltas для `Context`: новые решения, новые рабочие паттерны, новые source-bearing артефакты, новые проекты или важные изменения в текущих ventures.

## Inputs

- automation memory: `$CODEX_HOME/automations/<automation_id>/memory.md`;
- local session logs: `$CODEX_HOME/sessions/**/*.jsonl`;
- previous run timestamp from automation prompt or memory;
- current `context-map.md`, `docs/status.md`, founder-memory and active project indexes.

## Windowing

- Default window starts at `Last run` from the automation prompt.
- If `Last run` is missing, use the latest prior all-chat session in `07_sessions/<year>/`.
- Include automation threads, but mark them separately from user-started work.
- Exclude the current all-chat run from synthesis except as run metadata.

## Signal Thresholds

Write to `07_sessions/<year>/<date>.md` when at least one thread contains:
- a decision or operating principle that should be retrievable later;
- a meaningful plan, synthesis, critique or artifact;
- evidence about how Никита works;
- a project or system state change.

Do not elevate to canonical just because a topic appeared once. Use session layer for raw-but-useful deltas.

Low-signal threads include:
- greetings without substantive follow-up;
- short copyediting requests with no reusable context;
- blocked automation runs that did not inspect or change durable state;
- exploratory tool noise without a user-visible conclusion.

## Routing Rules

- `venture canonical`: only stable venture truth, decisions, shipped artifacts or evidence-backed product shifts.
- `project evidence/session`: project-specific synthesis that may matter later but is not yet canonical.
- `docs/status.md`: changes to the Context system, automation behavior, skill routing or retrieval process.
- `01_founder/working-with-nikita.md`: only repeated or clearly durable collaboration patterns.
- `05_playbooks/*`: repeatable operating procedures discovered through the run.

## Output Shape

Each all-chat synthesis should include:
- window and source files;
- high-signal threads;
- low-signal threads intentionally skipped;
- decisions / changed understanding;
- project routing;
- next retrieval or update actions.

## Safety

- Never dump raw JSONL into Context.
- Do not include secrets, credentials, private keys or raw personal data unless the target context layer explicitly requires it and the user requested preservation.
- Prefer links to local source files plus compact paraphrase.
- Preserve unrelated dirty worktree changes; do not revert or normalize them during automation.
