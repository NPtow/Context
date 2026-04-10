---
name: telegram-hiring-contact-sourcing
description: Use when the user asks to connect to their Telegram account, read vacancy posts from Telegram channels or chats, extract public HR/recruiter/hiring manager contacts tied to concrete vacancies, and save the accepted rows into CSV. Default to Telethon with a local session file, exact-only extraction, Telegram-only scope, and evidence-backed output.
---

# Telegram Hiring Contact Sourcing

Use this skill for `Telegram -> vacancy detection -> contact extraction -> CSV`.

Default scope:
- Telegram sources only
- `Telethon` as the connection model
- `local session file` as the auth/session strategy
- `exact-only` as the extraction mode
- no LinkedIn or external enrichment in v1

## Source of truth

- Canonical skill: `/Users/NIKITA/.codex/context/Context/00_system/skill-hub/skills/cloud/telegram-hiring-contact-sourcing`
- Local install: `/Users/NIKITA/.codex/skills/telegram-hiring-contact-sourcing`

## Use this skill when

Trigger this skill when the user wants to:
- connect Codex or a local script to their Telegram account;
- read vacancy posts from Telegram channels, groups, or chats they already have access to;
- extract public `HR`, `recruiter`, `talent acquisition`, `hiring manager`, or equivalent contact points;
- save accepted contacts into `CSV`;
- understand how Telegram session setup, login, reuse, or reset works for this sourcing flow.

Do not use this skill for:
- LinkedIn enrichment;
- outreach or message drafting;
- non-Telegram sourcing;
- collecting hidden or private personal data.

## Inputs you need

Minimum required inputs:
- Telegram sources
- date window
- role or keyword filters
- output `CSV` path

Connection inputs:
- `api_id`
- `api_hash`
- session file path

Optional inputs:
- blacklist channels
- blacklist companies
- geography or seniority filters

## Read these files only when needed

- Read [references/telegram-connection-setup.md](references/telegram-connection-setup.md) when the user asks how setup, login, reconnect, or session reuse works.
- Read [references/session-and-security.md](references/session-and-security.md) when handling session storage, reset, privacy, or access-boundary questions.
- Read [references/source-triage.md](references/source-triage.md) when deciding whether a message is a vacancy and whether a source is in scope.
- Read [references/contact-extraction-rules.md](references/contact-extraction-rules.md) when extracting contacts and assigning confidence.
- Read [references/csv-schema.md](references/csv-schema.md) when creating, validating, or reviewing the output CSV.
- Read [references/review-buckets.md](references/review-buckets.md) when deciding whether a row is `Accepted`, `Needs review`, or `Rejected`.

## Default workflow

### 1. Validate connection prerequisites

Confirm that the user has:
- `api_id`
- `api_hash`
- a local session path
- access to the target Telegram sources

If not, use `references/telegram-connection-setup.md`.

### 2. Establish or reuse Telegram session

Default flow:
- try the existing local session first;
- if the session does not exist or is invalid, explain the login flow;
- do not claim access to channels the user cannot already access.

Session and security rules live in `references/session-and-security.md`.

### 3. Triage sources and messages

Read Telegram messages in scope and classify them:
- vacancy
- not a vacancy
- ambiguous

Use `references/source-triage.md`.

### 4. Normalize each vacancy

For every accepted vacancy candidate, capture:
- company
- vacancy title
- source channel
- source message date
- source message URL or equivalent pointer

Never invent missing fields.

### 5. Extract contacts

Only accept contacts that are explicitly tied to the vacancy in Telegram or in the linked vacancy artifact allowed by this skill's Telegram-only scope.

Default accepted contact types:
- `telegram`
- `email`
- other explicit public vacancy contact points

Use `references/contact-extraction-rules.md`.

### 6. Apply output rules

Default output contract:
- `one row = one contact x one vacancy`
- main output is `CSV`
- default mode is `exact-only`
- generic application channels are not mixed into person-level accepted rows
- rows without evidence do not go into the main CSV

Use `references/csv-schema.md` and `references/review-buckets.md`.

### 7. Return both data and summary

At the end return:
- path to the output `CSV`
- count of reviewed messages
- count of detected vacancies
- count of `Accepted`, `Needs review`, and `Rejected` rows
- major blockers or ambiguity reasons

## Hard rules

- Do not guess contacts.
- Do not infer hidden personal data.
- Do not include non-public data.
- Do not claim access to unavailable Telegram sources.
- Do not put rows without evidence into the accepted CSV.
- Do not expand scope into LinkedIn or external enrichment in v1.

## Stop and ask the user if

- `api_id` and `api_hash` are missing;
- Telegram access is not configured;
- target sources are unclear;
- the user asks to read private sources they do not clearly have access to;
- the user asks to save or infer non-public personal data.
