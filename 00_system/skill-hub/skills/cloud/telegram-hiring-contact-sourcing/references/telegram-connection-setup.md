# Telegram Connection Setup

## Default connection model

Use `Telethon` with:
- `api_id`
- `api_hash`
- local session file

This skill does not use `bot token` as the primary connection mode.

## Required prerequisites

The user must provide or configure:
- `Python 3`
- `telethon`
- `api_id`
- `api_hash`
- a local path for session storage
- access to the target Telegram sources

## Where `api_id` and `api_hash` come from

Direct the user to:
1. open `https://my.telegram.org`
2. log in with their Telegram phone number
3. open `API development tools`
4. create an app
5. copy `api_id` and `api_hash`

## First-run login flow

On first run:
1. start the client with `api_id`, `api_hash`, and a local session path
2. if session does not exist, ask for the phone number
3. request the Telegram login code
4. if needed, request the `2FA` password
5. save the local session file

## Repeat-run flow

On later runs:
1. reuse the same local session path
2. if the session is valid, do not ask for login again
3. proceed directly to source reading

If the session is invalid or revoked, re-auth is required.

## Connection boundaries

Explain these limits clearly:
- the client acts as the user's Telegram account
- it sees only sources the user can already access
- it does not bypass private-channel restrictions
- it does not create special admin-level access

## Minimum operator checklist

Before starting a sourcing run, confirm:
- credentials exist
- session path is defined
- target sources are known
- the user is a member of those sources
- the output CSV path is known
