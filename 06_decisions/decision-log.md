---
title: Decision Log
type: decision-log
status: active
updated_at: 2026-04-11
---

# 2026-04-08

## D1. Уходим от referral marketplace как основной модели
Почему:
- модель выглядит плохо масштабируемой;
- ценность слишком завязана на социальный граф.

## D2. Фокусируем проект на AI-recruiting модели по мотивам Jack & Jill
Почему:
- она лучше собирает двусторонний контур;
- позволяет брать деньги с работодателя за outcome.

## D3. Первый сегмент — product managers
Почему:
- туда проще достучаться;
- можно собрать первые интервью и пилот быстрее, чем на широком рынке.

## D4. Главная цель пилота — 1 успешная оплата от работодателя
Почему:
- это сильнее любого "интереса" и лучше проверяет реальную ценность модели.

## D5. Репозиторий Context строится как LLM-first memory system
Почему:
- основная задача — не терять контекст и не пересобирать его в каждом разговоре заново.

## D6. Команда `обновись` должна поддерживать system-level updates
Почему:
- активная работа может относиться не к venture, а к самому репозиторию `Context`;
- в таком случае нужно обновлять system files и session log, не трогая venture canonical без необходимости.

## D7. У задач должен быть отдельный task-layer
Почему:
- задачи не должны извлекаться через интерпретацию `status`, `sessions` и `open edges`;
- нужен формализованный backlog по всем проектам и отдельные task-команды.

## D8. Старую `referalka` и новый AI-recruiting проект нужно хранить как два разных venture
Почему:
- старый referral marketplace и новый hiring-пилот имеют разную модель, economics и truth;
- без разделения память начинает смешивать candidate-paid referral и employer-paid recruiting.

## D9. Новый active venture получает отдельное имя `jjforrussia`
Почему:
- нужно убрать двусмысленность, где `referalka` означает то старый проект, то новый;
- отдельное имя упрощает retrieval, backlog и дальнейшие обновления.

## D10. Viewer для task-layer нужно держать как standalone сервис
Почему:
- он должен читать `Context` напрямую и не зависеть от Prisma, auth и product env;
- отдельный deploy упрощает проверку task-layer без вмешательства в runtime продукта;
- такой сервис лучше подходит как внешний operator surface для задач, чем встраивание в существующее приложение по умолчанию.

## D11. Если пользователь явно просит полный transcript, его нужно хранить в Context отдельным transcript file
Почему:
- для interview processing summary alone недостаточен;
- transcript должен жить отдельно от analytical note, чтобы не засорять project truth и meeting summary;
- такой формат нужен как база для будущего JJFR-specific transcription skill.

## D12. Top-level candidate segmentation в `jjforrussia` пока должна быть двухуровневой: `core PM` и `CPO/head-level`
Почему:
- более узкое top-level деление вроде `external/internal` слишком рано заужает supply;
- уже есть повторяющиеся кандидаты head-level сегмента со своей отдельной pain-map;
- на текущем этапе продукту полезнее разделять рынок по уровню и типу роли, а не по слишком тонкому устройству продуктовой среды.

# 2026-04-10

## D13. Candidate-facing problem survey и landing нужно держать как standalone surface
Почему:
- это исследовательский и funnel-инструмент, а не ядро продукта;
- отдельный deploy упрощает быстрые правки wording, ветвления и distribution по сообществам;
- такое разделение уменьшает связность с основным продуктовым репо и runtime по умолчанию.

# 2026-04-11

## D14. Telegram sourcing workflow фиксируется как safe operator layer, а не как gray scraping stack
Почему:
- для `jjforrussia` полезно иметь reusable surface для поиска вакансий и person-level hiring contacts в Telegram;
- этот surface должен быть ограничен `Telethon + own account + local session file + exact-only + evidence-backed CSV`;
- покупные аккаунты, прокси, account rotation и прочие обходные operational paths нельзя закреплять в канонической truth проекта или skill-hub.
