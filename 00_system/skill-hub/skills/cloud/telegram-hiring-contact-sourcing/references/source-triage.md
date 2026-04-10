# Source Triage

## Source scope

This skill works only with Telegram sources the user can already access:
- channels
- groups
- chats

If source ownership or access is unclear, ask the user.

## Vacancy detection

Treat a message as a vacancy when at least one is true:
- it explicitly says `vacancy`, `вакансия`, `hiring`, `looking for`, `ищем`, `open role`
- it has a job-like structure: role, company, requirements or conditions, and a response path
- it links to a job artifact and the text clearly frames it as a role

## Not-a-vacancy cases

Reject messages that are clearly:
- career advice
- course ads
- market news
- candidate self-promotion
- generic hiring digest without a concrete role

## Vacancy normalization

When a message is accepted as a vacancy, capture what is explicitly present:
- company
- vacancy title
- source channel
- source message date
- source message URL or equivalent pointer

Optional if explicit:
- location
- work mode
- seniority
- employment type

Do not fill missing data with guesses.
