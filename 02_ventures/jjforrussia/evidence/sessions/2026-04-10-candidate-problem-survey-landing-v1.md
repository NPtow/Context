---
title: Candidate Problem Survey Landing v1 Session
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-10
---

# Что произошло

- Для `jjforrussia` собран отдельный candidate-facing problem survey и вынесен в standalone landing.
- Лендинг реализован как отдельный `Next.js`-проект в локальной папке `/Users/NIKITA/Desktop/jjfr-survey`.
- Данные опроса пишутся в `Postgres` через `Prisma`; для сохранения добавлен отдельный `POST /api/survey`.
- Пользователь явно попросил не связывать этот surface с основным репо и держать его отдельным.

# Что теперь существует

- спокойный public-facing landing без агрессивного маркетингового слоя;
- пошаговый wizard-survey вместо длинной анкеты на одной странице;
- conditional logic по каналам поиска:
  - сначала человек выбирает, чем он пользуется;
  - затем оценивает только выбранные каналы;
- contact step для пилота показывается только если интерес к формату положительный;
- pilot copy зафиксирована как:
  - не ещё один список вакансий;
  - не карьерная консультация;
  - `личный AI-рекрутер / curated matching layer` для product/digital ролей.

# Что это уточнило

- problem survey теперь живёт отдельно от core interview и отдельно от `candidate-preferences-survey-v1`;
- candidate funnel получил новый public entrypoint для распространения по продуктовым сообществам;
- отдельный deploy признан более подходящим, чем встраивание в основной продуктовый код;
- survey logic стала ближе к problem research:
  - короткие и понятные closed-ended вопросы;
  - один открытый pain question;
  - reference frame `за последние 4 недели` там, где это materially важно.

# Что было с деплоем

- был создан отдельный Vercel-проект `jjfr-survey`;
- для него был поднят `Prisma Postgres`;
- первый production deploy был выполнен из standalone-папки;
- после первой попытки пользователь сообщил про `404 / NOT_FOUND`, а затем отдельно написал, что задачу уже завершил и нужно просто обновить `Context`.

# Связанные файлы

- [../../artifacts/candidate-problem-survey-landing-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-problem-survey-landing-v1.md)
- [../../canonical/current-state.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/canonical/current-state.md)
