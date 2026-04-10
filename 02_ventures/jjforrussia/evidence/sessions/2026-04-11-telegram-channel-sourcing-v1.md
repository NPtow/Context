---
title: Telegram Channel Sourcing v1
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-11
task_id: JJF-006
---

# Что произошло

- Для `jjforrussia` обновлен operational skill `telegram-hiring-contact-sourcing`, чтобы он поддерживал оба режима: `latest N posts` и `date window`.
- После обновления выполнен first-pass sourcing по 5 публичным Telegram-каналам за окно `2025-04-11` → `2026-04-11`.
- Результаты сохранены как отдельные per-channel CSV в локальной папке `/Users/NIKITA/Desktop/JJFR/artifacts/telegram-channel-contacts-2026-04-11`.

# Каналы и first-pass результат

| Channel | Accepted rows | Readout |
|---|---:|---|
| `@job_for_analysts` | 16 | Полезный, но узкий слой; много review/noise |
| `@careerstation_pm` | 43 | Наиболее рабочий first-wave результат среди перечисленных |
| `@employ_work` | 0 | В strict `exact-only` accepted-контактов не нашлось |
| `@c_level_top` | 701 | Очень шумный поток, нужен дедуп и отсев generic/agency patterns |
| `@JobOfferInside` | 25 | Есть usable контакты, но покрытие умеренное |

# Что это уточнило

- Telegram channel sourcing уже можно считать реальной частью `JJF-006`, а не только методологической идеей;
- качество источников нельзя оценивать по одному лишь объему строк:
  - `careerstation_pm` выглядит сильнее по signal-to-noise;
  - `c_level_top` слишком грязный для прямого использования без cleaning layer;
  - `employ_work` в текущем exact-only режиме скорее плохой источник person-level контактов;
- strict `exact-only` полезен как первый проход, но для некоторых mixed/general каналов он даст много review/no-contact кейсов и мало готовых строк.

# Связанные артефакты

- [job_for_analysts_contacts_last_year.csv](/Users/NIKITA/Desktop/JJFR/artifacts/telegram-channel-contacts-2026-04-11/job_for_analysts_contacts_last_year.csv)
- [careerstation_pm_contacts_last_year.csv](/Users/NIKITA/Desktop/JJFR/artifacts/telegram-channel-contacts-2026-04-11/careerstation_pm_contacts_last_year.csv)
- [employ_work_contacts_last_year.csv](/Users/NIKITA/Desktop/JJFR/artifacts/telegram-channel-contacts-2026-04-11/employ_work_contacts_last_year.csv)
- [c_level_top_contacts_last_year.csv](/Users/NIKITA/Desktop/JJFR/artifacts/telegram-channel-contacts-2026-04-11/c_level_top_contacts_last_year.csv)
- [JobOfferInside_contacts_last_year.csv](/Users/NIKITA/Desktop/JJFR/artifacts/telegram-channel-contacts-2026-04-11/JobOfferInside_contacts_last_year.csv)

# Следующий полезный шаг

- не собирать новые каналы вслепую, а сначала:
  - дедупнуть `c_level_top`;
  - вручную просмотреть `careerstation_pm` и `JobOfferInside`;
  - собрать shortlist контактов первой волны с приоритетом outreach.
