---
title: Current State
type: canonical
venture: jjforrussia
status: active
updated_at: 2026-04-13
---

# Summary
- Это отдельный venture, вынесенный из старого `referalka`.
- Проект ушел от referral marketplace как основной модели.
- Текущая гипотеза: двусторонний AI-recruiting product по мотивам Jack & Jill.
- Первый сегмент: `middle / middle+ / senior product managers` в digital product companies.
- Кандидат бесплатный; работодатель платит `10% success fee`.
- Главная цель пилота: получить хотя бы 1 успешную оплату от работодателя за найденного и устроенного кандидата.
- Execution layer уже формализован через backlog `JJF-001` ... `JJF-013`; ближайший live focus — `JJF-005` ... `JJF-009`.
- Поверх базовой гипотезы добавлен рыночный вывод: прямой 1-в-1 аналог на российском рынке публично не найден, но есть сильные частичные и полупрямые конкуренты.
- В candidate funnel появился отдельный public-facing problem survey landing, вынесенный в standalone deploy.
- Для sourcing ops появился reusable Telegram-only skill и connection guidance; серые workflows с покупными аккаунтами, прокси и account rotation не считаются частью канонического pilot flow.
- Telegram sourcing для `JJF-006` уже работает не как разовый scrape, а как двухслойный operator workflow: per-channel exact-only CSV плюс отдельный analytical cleaning/reporting layer.
- Исследовательские scaffolds и вспомогательные operator surfaces нужно держать local-first / standalone-first; они не должны автоматически попадать в продуктовые репозитории без явной команды.

# Current truth

## Что поменялось
Исходная идея про рефералку как рынок связей оказалась плохо масштабируемой и теперь хранится отдельно как venture `referalka`.  
Текущая линия — строить фильтр между кандидатами и работодателями, где:
- AI помогает собирать и структурировать данные;
- первые интро и калибровка делаются вручную;
- ценность для работодателя — shortlist, а не поток откликов.

После дополнительного market scan по российскому HR-tech это уточнилось так:
- главный прямой структурный аналог на рынке — `Getmatch`;
- главный конкурент за candidate trust и сопровождение — `careerspace`;
- главный системный конкурент по трафику и employer budget — экосистема `hh.ru + Talantix`;
- `Skillaz`, `Potok`, `FriendWork`, `HURMA`, `VCV` важны скорее как инфраструктурные HR-tech игроки, а не как прямые замены продукта;
- AI-native игроки вроде `Naimee AI`, `Nanimai`, `Наймус` важны как будущая угроза employer-side AI-слою, если venture начнет двигаться в сторону SaaS для HR.

## Для кого
- core first-wave segment: `middle / middle+ / senior product managers` в digital product companies;
- secondary adjacent segment: `CPO / head of product / senior product leadership`, особенно если уже есть повторяющиеся кандидаты и отдельная боль рынка;
- компании с реальной digital product-функцией;
- не "все IT", а digital product companies.

## Какой пилот сейчас считается правильным
- `ICP v1` уже зафиксирован как узкая первая волна по candidate-side и company-side;
- `PM role taxonomy v1` уже зафиксирована как первый рабочий фильтр по типам продуктовых ролей;
- `candidate interview protocol v1` уже собран как полный пакет, а не только список вопросов;
- `employer / HM outreach protocol v1` уже собран как полный пакет, а не только один текст первого контакта;
- `core wedge` и `secondary CPO/head-level segment` не нужно смешивать в один и тот же pilot funnel;
- `Head of Product / CPO / leadership` пока не считаются автоматически неподходящими; они идут отдельным руководительским потоком до следующего цикла проверки;
- интервью с кандидатами как вход в пилот;
- candidate interview v1 должен быть коротким и закрывать три задачи: ICP-fit, боль текущего поиска и резонанс формата `личный AI-рекрутер`;
- вопросы про желаемые роли и company preferences теперь вынесены в отдельную короткую анкету, а не живут внутри core interview;
- параллельно интервью с HR и hiring managers;
- employer-side первый шаг теперь выражен как `короткий аутрич -> discovery-разговор -> разбор одной живой роли`;
- Telegram sourcing теперь допустим как operator support-layer для поиска вакансий и contact points, но только через собственный Telegram-аккаунт пользователя, `Telethon`, local session file и evidence-backed extraction;
- текущий практический workflow поиска контактов теперь такой:
  - сначала public Telegram channels прогоняются через `telegram-hiring-contact-sourcing` в режиме `exact-only`;
  - стандартный рабочий срез — `date window` по последнему году, один канал = один CSV;
  - базовая единица данных остаётся `one row = one contact x one vacancy`;
  - затем per-channel CSV собираются в общий analytical batch, где контакты дедупятся по `contact_type + contact_value`;
  - после дедупа batch делится на `direct_employer`, `agency_or_intermediary` и `channel_or_aggregator`;
  - operator-value канала теперь оценивается не по raw row count, а по `direct share`, количеству unique direct contacts и качеству role/company extraction;
- опрос по продуктовым чатам как расширение candidate funnel;
- отдельный candidate-facing survey/landing теперь рассматривается как правильный surface для такого distribution, а не как часть core product repo;
- сбор первых вакансий и первых кандидатов;
- первый service surface теперь стоит понимать не как recommendation engine, а как двусторонний сбор structured data для ручного matching;
- ручной pilot flow без сложного matching engine.

## Что сейчас считается рабочей отстройкой
- не идти в широкий рынок "всех IT-вакансий";
- не продавать себя как очередной job board или карьерную консультацию;
- problem survey и landing тоже должны повторять эту рамку, а не выглядеть как generic vacancy aggregator;
- не конкурировать лоб в лоб с ATS/CRM для HR-команд;
- позиционироваться как `личный AI-рекрутер + curated matching layer` для `product/digital middle+`;
- держать фокус на candidate calibration, shortlist quality и employer-paid outcome.

## Что уже решено
- идти в двустороннюю модель;
- использовать интервью как способ вскрывать реальные боли, а не продавать пилот в лоб;
- candidate-facing problem survey / landing держать как отдельный standalone surface, а не встраивать в основной продуктовый код по умолчанию;
- держать Telegram sourcing workflow как reusable exact-only ops layer, а не превращать его в серый scraping stack;
- считать batch-level analytical cleaning обязательной частью Telegram sourcing, если каналов становится много и raw CSV перестают быть читаемым operator artifact;
- не принимать покупные / spam-banned аккаунты, прокси и rotation logic как часть канонического workflow;
- exploratory research scaffolds, landscape maps и вспомогательные surface-ы по умолчанию держать локально или отдельно от product repo; не пушить их в `referalka` и соседние продуктовые репозитории без явной команды;
- держать новый AI-recruiting venture отдельно от historical `referalka`;
- держать проектовый контекст отдельно от долгой памяти о Никите;
- хранить каноническое состояние, логи и архив раздельно.

## Supporting evidence
- [evidence/sessions/2026-04-08-product-pivot.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-08-product-pivot.md) — главный pivot-session и первый market/pilot readout.
- [artifacts/icp-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/icp-v1.md) — уже зафиксированный узкий стартовый сегмент.
- [artifacts/pm-role-taxonomy-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/pm-role-taxonomy-v1.md) — первый рабочий фильтр по типам PM-ролей и серым зонам.
- [artifacts/candidate-interview-pack-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-pack-v1.md) — полный пакет по `JJF-003`.
- [artifacts/employer-outreach-pack-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/employer-outreach-pack-v1.md) — полный пакет по `JJF-004`.
- [evidence/sessions/2026-04-09-jjf-002-taxonomy-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-09-jjf-002-taxonomy-v1.md) — почему taxonomy была упрощена и как сейчас трактуется руководительский поток.
- [evidence/sessions/2026-04-09-jjf-003-candidate-protocol-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-09-jjf-003-candidate-protocol-v1.md) — почему `JJF-003` был расширен до полного пакета.
- [evidence/sessions/2026-04-09-jjf-004-employer-outreach-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-09-jjf-004-employer-outreach-v1.md) — как сейчас устроен employer-side first contact и discovery.
- [evidence/sessions/2026-04-10-candidate-problem-survey-landing-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-10-candidate-problem-survey-landing-v1.md) — как собран отдельный public-facing survey landing и почему он вынесен в standalone deploy.
- [evidence/sessions/2026-04-11-telegram-sourcing-operator-surface.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-11-telegram-sourcing-operator-surface.md) — как для проекта оформлен reusable Telegram sourcing skill и почему unsafe account path не принят в truth.
- [evidence/sessions/2026-04-13-telegram-contact-analysis-report.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-13-telegram-contact-analysis-report.md) — как текущий sourcing workflow был доведён до actionable analytical layer, PDF report и channel-quality readout.
- [evidence/sessions/2026-04-13-context-audit-and-execution-guardrails.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-13-context-audit-and-execution-guardrails.md) — audit recent chats и уточнение execution guardrails без нового product pivot.
- [evidence/sessions/2026-04-13-sprint-plan-rebase.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-13-sprint-plan-rebase.md) — как weekend-задания были переведены в рабочий будничный спринт и что считается expected output к пятнице.
- [artifacts/candidate-problem-survey-landing-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-problem-survey-landing-v1.md) — reusable survey/landing artifact для candidate-side problem research.
- [working/hypotheses.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/working/hypotheses.md) — рабочие гипотезы и границы подтверждения.

## Source trail
- [evidence/sources/2026-04-08-russian-market-scan.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-08-russian-market-scan.md) — откуда взята текущая competitive map по РФ-рынку.
- [evidence/sources/2026-04-08-candidate-interviews-wave-1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-08-candidate-interviews-wave-1.md) — чем подтверждены candidate pain, segmentation и manual-calibration readout.
- [evidence/sources/2026-04-11-telegram-api-setup-and-app-creation.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-11-telegram-api-setup-and-app-creation.md) — официальный и community-backed source layer по Telethon onboarding и `my.telegram.org` app creation troubleshooting.
- [evidence/sources/2026-04-12-pusser-zheleznov-transcript.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-12-pusser-zheleznov-transcript.md) — transcript-backed source pack по ближайшему спринту, ручному matching-first flow и employer-side рискам.

## Read next
- [evidence/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/README.md)
- [working/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/working/README.md)
- [artifacts/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/README.md)

# Open edges
- уточнение границы между `core PM`, `technical PM` и внедренческой серой зоной;
- проверка, выдержит ли ручной pilot отдельный `CPO/head-level` поток;
- rejection taxonomy;
- employer-side GTM в первой волне.
- конкретная verbal positioning against `Getmatch`, `careerspace` and `hh`;
- выбор первого wedge: "личный AI-рекрутер", "product hiring intelligence" или "shortlist-as-a-service".
- distribution plan по product-сообществам и пороги качества для candidate survey funnel.
- yield Telegram-only sourcing для `JJF-006` на собственном легитимном аккаунте пользователя.
- как быстро превратить `843` actionable direct contacts из текущего batch в shortlist компаний и first-wave outreach queue без ручной возни по всем `2492` raw rows.
- как именно конвертировать первые HR-ответы и expert calls в живые hiring briefs при сжатом рынке и возможном hire freeze.
