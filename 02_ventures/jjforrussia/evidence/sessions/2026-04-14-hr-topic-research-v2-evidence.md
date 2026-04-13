---
title: HR Topic Research V2 Evidence
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-14
task_id: JJF-008
---

# Что произошло

- Первый проход по HR-корпусу (`v1`) был признан методологически слабым:
  - релевантность каналов определялась rule-based логикой;
  - темы были слишком широкими и ловили много карьерного и vacancy-шумa;
  - company-layer строился на mention-level сигналах и давал ложные выводы.
- После этого employer-side market read для `jjforrussia` был пересобран как evidence-first `v2`.
- Новый проход опирается только на модельно проверенные каналы и консервативные topic-buckets с пакетом прямых ссылок.

# Как теперь устроен employer-side research слой

## Channel gating

- Для top-80 каналов по объёму был собран sample-pack с representative постами.
- Каналы больше не считались релевантными автоматически по keyword/profile rules.
- Итог strict keep:
  - `17` каналов оставлены как HR/business-relevant;
  - `1612` постов вошли в strict corpus;
  - после отсечения шума осталось `1374` поста.

## Noise exclusion

Из strict corpus до тематизации исключались:
- `promo_or_event`: `145`
- `short_or_empty`: `65`
- `job_ad`: `28`

Принцип:
- сначала убрать `вебинары / регистрацию / рекламу / курсы / короткие пустые посты / чистые вакансии`;
- только потом строить темы.

## Evidence rule

- Сильный рыночный тезис не считается годным без минимум `10` прямых ссылок на посты.
- Все counts в `v2` трактуются как conservative lower bound, а не как попытка измерить весь рынок.
- Company-layer сознательно убран из core report до explicit-case pass.

# Что сейчас подтверждено лучше всего

## 1. Слабый сигнал о кандидате

- `16` постов
- `7` каналов
- охват `84890`
- свежих за `90` дней: `11`

Смысл для продукта:
- рынок регулярно обсуждает, что резюме, бренд работодателя, диплом, харизма и первое впечатление слабо предсказывают реальную силу кандидата.
- Это поддерживает wedge вокруг candidate calibration и более структурированной оценки.

## 2. Рассинхрон рекрутера и нанимающего менеджера

- `12` постов
- `3` канала
- охват `20180`
- свежих за `90` дней: `2`

Смысл для продукта:
- появляется опора для тезиса про калибровку роли и критериев до активного поиска.

## 3. Потери кандидатов внутри воронки

- `17` постов
- `9` каналов
- охват `80540`
- свежих за `90` дней: `8`

Смысл для продукта:
- рынок обсуждает не только sourcing, но и потерю сильных кандидатов на этапах, в скорости и в обратной связи.

## 4. Ошибка найма часто вскрывается после выхода

- `12` постов
- `7` каналов
- охват `57040`
- свежих за `90` дней: `7`

Смысл для продукта:
- усиливается ценность качественного match и более явной передачи ожиданий между наймом и выходом человека в роль.

## 5. ИИ делает найм шумнее

- `11` постов
- `5` каналов
- охват `49590`
- свежих за `90` дней: `7`

Смысл для продукта:
- тема пригодна как urgency amplifier, но сама по себе не должна быть единственным ядром позиционирования.

## 6. Бизнес ждёт от HR решений, а не просто отчётов

- `10` постов
- `5` каналов
- охват `68300`
- свежих за `90` дней: `6`

Смысл для продукта:
- это рабочий язык разговора с HRD и бизнесом, когда нужно объяснять ценность structured hiring signal.

# Что это меняет для JJFR

- Employer-side messaging нельзя строить на generic формуле "дадим больше кандидатов".
- Сильнее всего сейчас поддержаны четыре линии:
  - quality of candidate signal;
  - recruiter / hiring-manager alignment;
  - funnel loss;
  - onboarding / bad-hire exposure.
- `AI noise` лучше использовать как фактор срочности, а не как единственную сущность оффера.
- Company targeting пока нельзя считать подтверждённым на основании одних только упоминаний компаний в HR-постах.

# Связанные артефакты

- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/channel_model_review_pack.md`
- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/channel_model_review_top80.tsv`
- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/keep_channels_strict_posts.jsonl`
- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/pipeline_summary_v2.json`
- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/topic_metrics_v2.csv`
- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/topic_evidence_v2.md`
- `/Users/NIKITA/Desktop/JJFR/artifacts/hr-topic-research-v2/hr-topic-research-v2-final-report.pdf`

# Связанные решения

- core report больше не должен включать company shortlist без explicit evidence;
- для market-claims по HR-корпусу нужен model-reviewed channel set и пакет ссылок;
- v1 readout остаётся полезным как exploratory scaffold, но не как канонический evidence-backed report.
