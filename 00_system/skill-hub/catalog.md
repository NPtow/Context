---
title: Skill Catalog
type: index
status: active
updated_at: 2026-04-11
---

# Как читать

- Сначала открыть `README.md` этого skill hub.
- Потом выбрать skill из этого каталога.
- Затем перейти в соответствующую папку и читать `SKILL.md` плюс соседние `agents/`, `references/`, `scripts/`, `assets/`.

# Быстрая сводка

- total skills: `13`
- local mirrored skills: `12`
- cloud skills: `1`

## Local Mirrored Skills (12)

### `architect`
- name: `architect`
- description: Анализирует локальные папки пользователя (Desktop, Downloads, Documents, Movies, Music, Pictures и др.), предлагает структуру и безопасно систематизирует файлы: никогда не удаляет, только перемещает или архивирует. Триггерит на фразы: \"систематизируй файлы\", \"разбери папки\", \"почисти загрузки\", \"архивируй старое\", \"architect\", \"разбери Desktop\", \"организуй файлы\".
- path: `skills/local/architect`
- extras: SKILL.md only
- origin: `/Users/NIKITA/.codex/skills/architect`

### `context-ingest`
- name: `context-ingest`
- description: Use when the user asks to add a file or arbitrary information into the Context repo via phrases such as "пополни контекст", "добавь в контекст", "сохрани это в Context", "положи файл в контекст", "add this to context", or equivalent requests about importing notes, files, transcripts, source material, artifacts, or structured information.
- path: `skills/local/context-ingest`
- extras: SKILL.md only
- origin: `/Users/NIKITA/.codex/skills/context-ingest`

### `context-query`
- name: `context-query`
- description: Use when the user asks to read or summarize the Context repo, or writes `контекст`, `контеекст`, `context`, or another language equivalent and expects repo-grounded answers only. Triggers on requests such as "покажи контекст проекта", "что изменилось", "покажи память обо мне", "сравни с прошлым", "дай сводку", "все задачи по проекту X", "какие задачи сейчас есть", "show context", "use only Context", and similar requests about current project context, founder memory, deltas, or task lists.
- path: `skills/local/context-query`
- extras: SKILL.md only
- origin: `/Users/NIKITA/.codex/skills/context-query`

### `context-update`
- name: `context-update`
- description: Use when the user asks to update their Context repo via natural-language commands such as "обновись", "обнови проект", "сохрани сессию", "архивируй проект", "обнови контекст", "поставить задачу", "добавь задачу", or equivalent Russian phrasing about saving new conversation context, refreshing project state, updating founder memory, or editing the formal task layer.
- path: `skills/local/context-update`
- extras: SKILL.md only
- origin: `/Users/NIKITA/.codex/skills/context-update`

### `justdoit`
- name: `justdoit`
- description: Default execution-planning skill for almost any non-trivial repo task. Turns a raw task, feature request, PRD, or project brief into durable execution docs: `plans.md`, `status.md`, and `test-plan.md` (or existing repo equivalents), then proposes execution before starting. Use by default unless the user clearly wants a trivial one-shot answer, pure discussion, or no planning.
- path: `skills/local/justdoit`
- extras: agents, references
- origin: `/Users/NIKITA/.codex/skills/justdoit`

### `meeting-transcriber`
- name: `meeting-transcriber`
- description: Use when the user asks to transcribe a meeting, call, interview, voice note, or recorded conversation and save the result into the Context repository. Trigger on requests like "транскрибируй встречу", "сохрани встречу в контекст", "расшифруй созвон", "разбери запись интервью", or equivalent Russian phrasing about turning an audio/video recording into structured meeting notes linked to a project.
- path: `skills/local/meeting-transcriber`
- extras: agents, scripts
- origin: `/Users/NIKITA/.codex/skills/meeting-transcriber`

### `system--imagegen`
- name: `imagegen`
- description: Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.
- path: `skills/local/system--imagegen`
- extras: agents, references, scripts, assets
- origin: `/Users/NIKITA/.codex/skills/.system/imagegen`

### `system--openai-docs`
- name: `openai-docs`
- description: Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or explicit GPT-5.4 upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.
- path: `skills/local/system--openai-docs`
- extras: agents, references, assets
- origin: `/Users/NIKITA/.codex/skills/.system/openai-docs`

### `system--plugin-creator`
- name: `plugin-creator`
- description: Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.
- path: `skills/local/system--plugin-creator`
- extras: agents, references, scripts, assets
- origin: `/Users/NIKITA/.codex/skills/.system/plugin-creator`

### `system--skill-creator`
- name: `skill-creator`
- description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.
- path: `skills/local/system--skill-creator`
- extras: agents, references, scripts, assets
- origin: `/Users/NIKITA/.codex/skills/.system/skill-creator`

### `system--skill-installer`
- name: `skill-installer`
- description: Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).
- path: `skills/local/system--skill-installer`
- extras: agents, scripts, assets
- origin: `/Users/NIKITA/.codex/skills/.system/skill-installer`

### `telegram-hiring-contact-sourcing`
- name: `telegram-hiring-contact-sourcing`
- description: Use when the user asks to connect to their Telegram account, read vacancy posts from Telegram channels or chats, extract public HR/recruiter/hiring manager contacts tied to concrete vacancies, and save the accepted rows into CSV. Default to Telethon with a local session file, exact-only extraction, Telegram-only scope, and evidence-backed output.
- path: `skills/local/telegram-hiring-contact-sourcing`
- extras: agents, references
- origin: `/Users/NIKITA/.codex/skills/telegram-hiring-contact-sourcing`

## Cloud Skills (1)

### `telegram-hiring-contact-sourcing`
- name: `telegram-hiring-contact-sourcing`
- description: Use when the user asks to connect to their Telegram account, read vacancy posts from Telegram channels or chats, extract public HR/recruiter/hiring manager contacts tied to concrete vacancies, and save the accepted rows into CSV. Default to Telethon with a local session file, exact-only extraction, Telegram-only scope, and evidence-backed output.
- path: `skills/cloud/telegram-hiring-contact-sourcing`
- extras: agents, references
