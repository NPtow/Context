# Session And Security

## Default session strategy

Use a `local session file`.

Recommended properties:
- stored outside the working repository
- stored in a private local folder
- reused between runs
- never committed to git

Recommended example path:

```text
~/.codex/.secrets/telegram/telegram-hiring-contact-sourcing.session
```

## Why the session matters

The session file is what makes repeat runs possible without re-entering the phone number and login code every time.

Treat it as sensitive local access material.

## Allowed security model

The skill may:
- use the user's own Telegram account
- read only sources already visible to that account
- process public contact data from vacancy posts

The skill may not:
- infer hidden personal data
- use gray-market datasets
- bypass source access controls
- promise visibility into channels the user cannot access

## Invalid session signals

Treat the session as invalid if:
- login is unexpectedly requested again
- Telegram reports revoked or expired authorization
- access suddenly fails for previously working reads

## Reset flow

If the session must be reset:
1. stop the run
2. delete the local session file
3. optionally revoke the session from Telegram settings
4. run the login flow again

## Troubleshooting

### Wrong `api_id` or `api_hash`

Check:
- the values were copied correctly
- `api_id` is treated as an integer
- both values belong to the same Telegram API app

### `SESSION_PASSWORD_NEEDED`

This means the Telegram account has `2FA` enabled.

Ask for the `2FA` password in addition to the login code.

### Inaccessible source

Likely causes:
- the user is not a member
- the source is private
- invite access is missing or invalid

Do not claim the skill can read that source.

### Flood or rate limits

Reduce request volume and respect retry windows.

### Session expired or revoked

Признаки: `AuthKeyUnregisteredError`, `SessionRevokedError`, неожиданный запрос логина на повторном запуске.

Действие:
1. Остановить скрипт
2. Удалить локальный session-файл
3. Завершить сессию в `Telegram → Settings → Devices` по желанию
4. Запустить login flow заново

### Аккаунт заморожен (frozen / spam ban)

Признаки: `UserDeactivatedBanError`, ошибка `frozen account` при вызове методов отправки.

Действие: написать `@SpamBot` для диагностики. Чтение каналов обычно продолжает работать даже при заморозке.
