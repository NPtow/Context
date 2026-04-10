---
name: meeting-transcriber
description: Use when the user asks to transcribe a meeting, call, interview, voice note, or recorded conversation and save the result into the Context repository. Trigger on requests like "транскрибируй встречу", "сохрани встречу в контекст", "расшифруй созвон", "разбери запись интервью", or equivalent Russian phrasing about turning an audio/video recording into structured meeting notes linked to a project.
---

# Meeting Transcriber

Use this skill to transcribe recorded meetings with Deepgram and save them into Context.

## Source of truth

- Skill location: `/Users/NIKITA/.codex/skills/meeting-transcriber`
- Context repo: `/Users/NIKITA/.codex/context/Context`

## What this skill does

1. Transcribes an audio or video file with Deepgram.
2. Produces a clean speaker-labeled transcript.
3. Writes a meeting note into Context under `10_meetings/<year>/`.
4. Links the meeting to the most relevant venture, system, or domain context.

## First files to read

1. `/Users/NIKITA/.codex/context/Context/context-map.md`
2. `/Users/NIKITA/.codex/context/Context/10_meetings/README.md`
3. If the meeting is clearly project-related, read that venture `README.md` and `canonical/current-state.md`

## Input requirements

You need a full local file path to the recording.

Supported practical inputs:
- `.m4a`
- `.mp3`
- `.wav`
- `.mp4`
- `.mov`
- `.webm`

If the user gave only a filename and not a path, ask for the full path.

## Default workflow

### Step 1. Transcribe with Deepgram

Run:

```bash
python3 /Users/NIKITA/.codex/skills/meeting-transcriber/scripts/deepgram_transcribe.py \
  --input "/absolute/path/to/recording.m4a"
```

By default the script:
- uses `nova-3`
- uses `language=multi`
- enables `smart_format`, `diarize`, `utterances`, `paragraphs`, `punctuate`
- writes outputs next to the source file into `.meeting-transcriber/<basename>/`

Important output files:
- `transcript.txt`
- `utterances.json`
- `raw.json`

### Step 2. Understand what the meeting is about

Infer the relation in this order:
1. explicit user statement
2. active venture from `context-map.md`
3. transcript content

If confidence is low, ask one short question:

`Уточню: эту встречу привязать к jjforrussia, referalka или другому контексту?`

### Step 3. Write a meeting note into Context

Write one markdown file under:

- `/Users/NIKITA/.codex/context/Context/10_meetings/<year>/<date>-<slug>.md`

Use this structure:

```md
---
title: <short meeting title>
type: meeting
status: active
updated_at: YYYY-MM-DD
date: YYYY-MM-DD
related_to:
  - venture: <jjforrussia|referalka|none>
  - domain: <optional>
source_file: </absolute/path/to/file>
raw_transcript: </absolute/path/to/transcript.txt>
---

# Context
- what this meeting was
- why it matters
- how confident you are about the relation

# Summary
- 5-10 bullets max

# Decisions
- only explicit decisions

# Action items
- owner if known
- action

# Open questions
- unresolved issues only

# Transcript highlights
- important quotes or moments, paraphrased
```

Keep the note compact. Do not paste the full transcript into Context markdown.

### Step 4. Optional project update

Do not update project `canonical` by default.

Only update venture files if the meeting clearly changes project truth.
In that case, prefer:
- venture evidence session
- task layer
- decision log

over rewriting `canonical/current-state.md` too eagerly.

## Naming rules

- Date format: `YYYY-MM-DD`
- Slug: short and descriptive, e.g. `candidate-interview-anna-pm`
- If the file is a generic sync, use `sync`, `discovery`, `candidate-interview`, `hm-call`, etc.

## Rules

- If relation is ambiguous, ask exactly one short question.
- Save every processed meeting into `10_meetings`, not into random venture folders.
- Do not store the API key in Context or in git-tracked files.
- Keep the meeting note as retrieval-friendly summary, not raw dump.
- Prefer Russian meeting notes unless the user explicitly asks for English.
