---
title: Meetings Layer
type: index
status: active
updated_at: 2026-04-08
---

# Назначение

Отдельный слой для встреч, звонков, интервью и разборов, которые нужно сохранять в Context.

Этот слой нужен, чтобы:
- не терять смысл длинных созвонов;
- не тащить сырые транскрипты в `canonical`;
- держать summary, decisions и action items отдельно от project truth.

# Структура

- `10_meetings/<year>/<date>-<slug>.md` — краткая meeting note
- `10_meetings/<year>/transcripts/<date>-<slug>-transcript.md` — полный cleaned transcript, если нужно хранить полную расшифровку внутри Context
- сырые transcript artifacts могут храниться рядом с source file вне Context или быть упомянуты абсолютным путем в note

# Формат meeting note

Каждая встреча должна содержать:
- `related_to` — к чему она относится;
- `source_file` — исходная запись;
- `raw_transcript` — путь к текстовой расшифровке;
- `transcript_file` — путь к full transcript в Context, если он сохранён;
- `Summary`;
- `Decisions`;
- `Action items`;
- `Open questions`.

# Правила

- По умолчанию писать встречу сюда, а не в `02_ventures/*/evidence/`.
- В venture evidence переносить только если встреча изменила проектовую truth.
- По умолчанию не копировать в Context полный transcript, если достаточно summary + ссылки на raw transcript.
- Special case: если пользователь явно просит хранить полный transcript в Context, сохранять его отдельным файлом в `10_meetings/<year>/transcripts/`, а аналитическую note держать отдельным файлом.
- Если transcript сохранён в Context, он должен быть cleaned, speaker-labeled и с таймкодами; raw JSON в Context не хранить.
