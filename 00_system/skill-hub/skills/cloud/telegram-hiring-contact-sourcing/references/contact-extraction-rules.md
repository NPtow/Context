# Contact Extraction Rules

## Default mode

Use `exact-only` by default.

That means:
- only explicit contacts tied to the vacancy are accepted
- no LinkedIn or external enrichment in v1
- no person guessing by name

## Accepted contact categories

Person-level contacts:
- `HR`
- `Recruiter`
- `Talent Acquisition`
- `Hiring Manager`
- equivalent explicit recruiting contact

Allowed contact values:
- Telegram username
- Telegram link
- email
- another explicit public vacancy contact shown in the Telegram artifact

## Contact priority

Prefer these in order:
1. Telegram username or `t.me/...`
2. explicit email
3. another explicit public contact point

## Contact must be tied to the vacancy

Accept the row only if the contact is clearly linked to the vacancy, for example:
- `писать @anna_hr`
- `HR: Maria Ivanova`
- `for details contact ...`
- `send CV to ...`

If the contact exists but is not clearly tied to the vacancy, do not accept it into the main CSV.

## Confidence

### `high`

The contact is explicitly present in the vacancy message or an immediately attached vacancy artifact in scope.

### `medium`

Do not use this for accepted rows in v1 exact-only mode.

### `low`

Do not use this for accepted rows in v1 exact-only mode.

## Explicit exclusions

Do not accept as a person-level contact:
- generic ATS form
- career site without a named person
- vague `write in DM` with no username
- guessed profiles
- inferred external profiles

## Normalization

Normalize before writing:
- Telegram username as `@username`
- Telegram URL without tracking params
- email in lowercase

One row remains one `contact x vacancy`, even if the same person appears in multiple vacancies.
