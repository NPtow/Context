# CSV Schema

## Output contract

Main output is `CSV`.

Core rule:
- `one row = one contact x one vacancy`

Main CSV accepts only evidence-backed rows.

## Minimum required columns

```csv
source_channel,source_message_date,source_message_url,company,vacancy_title,contact_name,contact_role,contact_type,contact_value,confidence,evidence
```

## Recommended full schema

```csv
run_date,source_channel,source_message_date,source_message_url,company,vacancy_title,team_or_function,location,work_mode,seniority,employment_type,contact_name,contact_role,contact_type,contact_value,hiring_for,confidence,evidence,dedupe_key,notes
```

## Column rules

- `source_channel`: Telegram source name
- `source_message_date`: message date
- `source_message_url`: pointer back to the source message whenever possible
- `company`: explicit company name only
- `vacancy_title`: explicit role title only
- `contact_name`: optional if unknown
- `contact_role`: normalized role such as `HR`, `Recruiter`, `Hiring Manager`
- `contact_type`: `telegram`, `email`, or another explicit public type
- `contact_value`: actual public contact
- `confidence`: in v1 accepted rows should be `high`
- `evidence`: short snippet or pointer proving the link

## Hard acceptance rules

- no evidence -> not accepted
- no vacancy-contact linkage -> not accepted
- generic application channel -> not mixed into person-level accepted rows

## Generic application channels

If the source contains only a form or ATS link:
- do not put it into the main person-level CSV
- either reject it or keep it in a separate review/output layer
