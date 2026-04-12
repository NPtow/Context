---
title: Telegram Contact Analysis Report
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-13
task_id: JJF-006
---

# Что произошло

- По Telegram sourcing для `jjforrussia` собран не только batch per-channel CSV, но и отдельный analytical layer поверх него.
- Для локальной папки `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-batch-2026-04-11` сделан воспроизводимый report pipeline:
  - объединение всех channel CSV;
  - нормализация `company`, `vacancy_title`, `contact_value`;
  - дедуп по `contact_type + contact_value`;
  - классификация контактов на `direct_employer`, `agency_or_intermediary`, `channel_or_aggregator`;
  - построение `master_raw`, `master_actionable`, company / role / channel quality summaries;
  - генерация PDF report.

# Как теперь practically ищутся контакты

- Рабочий entrypoint остаётся skill `telegram-hiring-contact-sourcing`.
- Первичный проход:
  - public channel;
  - `exact-only`;
  - чаще всего `date window` за последний год;
  - один канал = один CSV.
- После этого поиск больше не заканчивается на наборе CSV:
  - CSV собираются в общий batch;
  - raw contacts очищаются и canonical-dedup'ятся;
  - direct-layer отделяется от агентств и channel-like контактов;
  - каналы сравниваются по `direct share`, `noise share`, `unique direct contacts`, а не по одному объёму строк.

# Текущий analytical readout

## Batch-level numbers

- raw rows: `2492`
- unique canonical contacts: `1071`
- actionable direct contacts: `843`
- channels with non-zero data: `29`
- data window: `2025-04-11` → `2026-04-10`

## Что это говорит про sourcing quality

- raw count очень плохо отражает полезность канала;
- большие mixed/general каналы дают много строк, но часто шумят агрегаторами, агентствами и generic channel handles;
- узкие role-oriented каналы обычно дают лучший signal-to-noise и более usable direct-contact layer.

## Каналы, которые сейчас выглядят самыми полезными

По текущему batch strongest operator-value дают:
- `@product_jobs`
- `@productjobgo`
- `@fmcg_job`

Дополнительно:
- `@office_vacancies` даёт большой объём, но заметно шумнее;
- `@itjobs_nocode` даёт крупный raw поток, но очень слабый `direct share`, поэтому как первоочередной sourcing source выглядит хуже.

## Кого рынок искал чаще всего

После очистки role families распределяются так:
- основной слой: `product`
- затем `project/program`
- затем `executive/c-level`

Это поддерживает текущую project intuition, что PM / adjacent digital product roles остаются правильным первым клином, а руководительский слой стоит вести отдельно.

## Что важно помнить про ограничения

- `company` extraction остаётся самым шумным полем;
- не каждый Telegram contact = hiring manager;
- часть повторов — это recruiters, агентства, channel operators или посредники;
- поэтому полезный operator artifact теперь не raw CSV, а `master_actionable` плюс channel-quality summaries.

# Какие инсайты стоит использовать дальше

- Не расширять список Telegram-каналов вслепую.
- Сначала работать с лучшими источниками по `direct share`, а не по raw объёму.
- Следующий meaningful step для `JJF-006` — превратить текущий actionable layer в shortlist:
  - компаний;
  - repeat hiring points;
  - direct-contact queue для employer discovery / outreach.

# Связанные артефакты

- `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-batch-2026-04-11`
- `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-contacts-report-2026-04-12/telegram_contacts_report.pdf`
- `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-contacts-report-2026-04-12/master_raw.csv`
- `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-contacts-report-2026-04-12/master_actionable.csv`
- `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-contacts-report-2026-04-12/channel_quality_summary.csv`
