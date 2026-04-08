---
title: Hiring Signals Ledger v1
type: artifact
venture: jjforrussia
status: active
updated_at: 2026-04-09
---

# Purpose

- Завести накопительный блок для внешних сигналов о найме, оценке навыков и калибровке ролей.
- Отдельно фиксировать `insights` и `skill insights`, чтобы не смешивать raw source signal, продуктовые выводы и canonical truth.
- Использовать этот документ как пополняемый ledger: новые source packs добавляются сюда, а не растворяются в разовых сессиях.

# How to use this ledger

- `Insight` = что рынок, HR, hiring managers или кандидаты сигналят о проблеме.
- `Skill insight` = какой capability, framework или продуктовый слой из этого следует для `jjforrussia`.
- `Confidence` = насколько сильно это уже подтверждено.
- Если сигнал пришёл только из одного источника, он остаётся здесь или в `working`, а не становится canonical truth.

# Current insights

## I-001. Employer-side calibration is broken too

- insight:
  - не только кандидаты страдают от плохого hiring-процесса; HR и нанимающие команды сами признают, что калибровка навыков, требований и уровней часто не работает;
  - это прямо совпадает с твоим чтением: проблема не в одной компании, а в отсутствии внешнего и более универсального способа сегментировать людей.
- why it matters:
  - `jjforrussia` может решать не просто sourcing, а слой независимой калибровки между работодателем и кандидатом.
- skill insight:
  - нужен внешний skill framework, который не завязан на внутренние названия ролей одной компании;
  - нужен перевод между `market language`, `company brief` и `candidate reality`.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-09-hh-it-hiring-signals.md`

## I-002. The bottleneck moved from candidate volume to signal quality

- insight:
  - кандидатов становится больше, но найти реально подходящего человека не легче;
  - AI увеличивает объём polished signal, но не гарантирует рост настоящего skill visibility.
- why it matters:
  - продукт не должен соревноваться по объёму откликов; его wedge в том, чтобы извлекать signal из noisy input.
- skill insight:
  - нужен evidence-weighted profile, где отдельно живут self-report, observed experience, verified signal и ambiguous signal;
  - нужен anti-noise слой против `AI-polished but weakly-grounded` кандидата.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-09-hh-it-hiring-signals.md`

## I-003. Role definitions are unstable and often need to be rebuilt

- insight:
  - гибридные роли растут, а единый язык ролей и навыков запаздывает;
  - иногда найм ускоряется не после расширения воронки, а после пересборки требований.
- why it matters:
  - value продукта может начинаться ещё до подбора кандидата: с нормализации brief и разборки того, кого на самом деле ищут.
- skill insight:
  - нужен capability to reframe vacancy from title-based brief into capability-based brief;
  - нужен requirement reassembly flow: `title -> tasks -> decision scope -> skill evidence -> reject reasons`.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-09-hh-it-hiring-signals.md`

## I-004. AI creates both acceleration and false confidence in hiring

- insight:
  - рынок уже обсуждает не вопрос `использовать ли AI`, а вопрос `где AI ускоряет решение, а где создаёт ложные сигналы`.
- why it matters:
  - `jjforrussia` должен уметь не просто пользоваться AI, а объяснимо отделять реальный signal от tool-assisted performance.
- skill insight:
  - нужен signal provenance layer: что видно из резюме, что видно из разговора, что подтверждено кейсами, а что могло быть усилено инструментом;
  - нужен explainable decision trace, чтобы hiring side доверяла shortlist-решению.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-09-hh-it-hiring-signals.md`

## I-005. Assessment infrastructure is becoming a baseline, not a corporate luxury

- insight:
  - вопрос на рынке уже не только про интервью эксперта, а про переход к repeatable systems of evaluation;
  - это особенно важно для команд, где нельзя полагаться только на `экспертуитивность`.
- why it matters:
  - маленьким и средним командам тоже нужен lightweight assessment operating system, а не только enterprise-grade HR stack.
- skill insight:
  - opportunity: сделать компактную инфраструктуру оценки для узкого вертикального сегмента, а не тяжёлый ATS;
  - shortlist должен сопровождаться понятной structured reasoning, а не только мнением рекрутера.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-09-hh-it-hiring-signals.md`

## I-006. Self-calibration is a core candidate pain, not a side problem

- insight:
  - кандидатам тяжело понять, куда они реально подходят и как рынок читает их уровень;
  - проблема касается не только `CPO`, но и более широкого PM-рынка: границы между `middle`, `senior`, `head` и hybrid roles размыты.
- why it matters:
  - продукт может быть полезен ещё до мэтча: как слой рыночной self-calibration и role positioning.
- skill insight:
  - нужен calibration output, который говорит не только `подходит / не подходит`, но и `в какие role-buckets ты fit`, `где ты overqualified`, `где gray-zone`;
  - нужен explainable level model вместо одного title label.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-08-candidate-interviews-wave-1.md`

## I-007. Recruiter and hiring manager often evaluate different realities

- insight:
  - кандидат может не проваливаться по сути роли, а ломаться на разрыве между рекрутерским фильтром и реальной логикой нанимающего менеджера.
- why it matters:
  - matching без учёта этой асимметрии будет давать ложные отрицания и плохую конверсию даже при хорошем fit.
- skill insight:
  - нужен dual-view vacancy model: отдельно recruiter screen, отдельно hiring-manager success criteria;
  - нужен слой `translation / reconciliation`, который показывает, где именно brief расходится между сторонами.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-08-candidate-interviews-wave-1.md`

## I-008. Hidden market and fake-market-check vacancies distort public search

- insight:
  - не все вакансии публикуются, а часть публичных вакансий может существовать скорее как проверка рынка, чем как реальный активный найм.
- why it matters:
  - продукт, работающий только по публичной выдаче, будет системно неполон и будет терять trust.
- skill insight:
  - нужен market-access layer поверх публичных вакансий: intros, network paths, direct company monitoring, hidden-role signals;
  - нужна vacancy quality scoring model: `real / stale / market-check / unclear`.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-08-candidate-interviews-wave-1.md`

## I-009. Timing is part of matching, not just application hygiene

- insight:
  - в публичном рынке скорость отклика влияет на шанс попасть в раннюю выборку и быть замеченным;
  - кандидатам важно не только качество мэтча, но и freshness of opportunity.
- why it matters:
  - ценный продукт должен не только находить подходящее, но и приносить это вовремя.
- skill insight:
  - нужен freshness-aware discovery flow и alerting layer;
  - match should carry timing priority, not only fit score.
- confidence: low-medium
- primary source:
  - `../evidence/sources/2026-04-08-candidate-interviews-wave-1.md`

## I-010. The process bottleneck is not always getting in; it is getting through

- insight:
  - интро или первый контакт кандидат иногда получает без большого труда;
  - узкое место часто сдвигается в длинный, несогласованный и outcome-poor процесс после входа.
- why it matters:
  - продукт не должен мерить успех только `response rate`; ему нужен deeper funnel view.
- skill insight:
  - нужны funnel metrics beyond intro: `intro -> screen -> manager -> late stage -> offer`;
  - нужен process-risk layer: где кандидат likely to stall and why.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-08-candidate-interviews-wave-1.md`

## I-011. Resume optimization norms are degrading market signal

- insight:
  - рынок уже учит кандидатов копировать слова из вакансии в резюме; это делает ATS-совместимость более дешёвым и шумным сигналом.
- why it matters:
  - если продукт опирается только на resume-text matching, он будет воспроизводить шум текущего рынка.
- skill insight:
  - нужен evidence hierarchy, где резюме — лишь один слой рядом с interview signal, experience narratives и verified outcomes;
  - нужен anti-keyword-overfit подход к оценке кандидата.
- confidence: medium
- primary source:
  - `../evidence/sources/2026-04-08-candidate-interviews-wave-1.md`

# Open additions queue

- сравнить эти employer-side сигналы с реальными HR-интервью, когда они появятся;
- завести отдельный блок для `rejection insights`, если начнёт копиться pattern по отказам;
- при появлении новых источников добавлять новые записи по схеме `I-00X`.
- проверить, какие из candidate-side insights достаточно устойчивы, чтобы поднять их в `working/hypotheses.md`.
