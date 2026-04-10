# Review Buckets

## Accepted

A row goes to `Accepted` only if all are true:
- the source is in scope
- the message is a real vacancy
- the contact is explicit
- the contact is tied to the vacancy
- the row has evidence

These rows go to the main CSV.

## Needs review

Use `Needs review` when:
- the message is probably a vacancy but wording is ambiguous
- the contact looks real but the vacancy link is not explicit enough
- the source pointer exists but the evidence is weak

Do not mix these rows into the accepted CSV by default.

## Rejected

Reject when:
- the message is not a vacancy
- there is no explicit contact
- the contact is generic only
- the link between person and vacancy is missing
- the data would require guessing

## Summary output

At the end of a run, report:
- messages reviewed
- vacancies found
- accepted rows
- needs-review rows
- rejected rows
- main reasons for ambiguity or rejection
