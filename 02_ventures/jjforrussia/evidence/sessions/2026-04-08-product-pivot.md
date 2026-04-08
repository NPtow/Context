---
title: JJFORRUSSIA Product Pivot Session
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-08
---

# Что обсуждали
- почему исходная модель рефералки плохо масштабируется;
- как устроен Jack & Jill и чем он отличается от прошлой гипотезы;
- почему стоит фокусироваться на product-ролях;
- как должен выглядеть первый pilot flow;
- зачем нужен отдельный репозиторий `Context`.
- почему новый AI-recruiting контур нужно отделить от старой `referalka`.
- кто именно на российском рынке уже решает похожую задачу и где проходит граница конкуренции.
- как должен выглядеть первый короткий candidate interview и какие вопросы нельзя смешивать в одном созвоне.

# Главные выводы
- referral marketplace сам по себе не выглядит как масштабируемый бизнес;
- более сильная гипотеза — AI-recruiting layer с ручным пилотом;
- идти стоит в узкий сегмент product managers, а не в весь рынок;
- главная цель пилота — не "провести интервью", а получить 1 успешную оплату;
- этот контур нужно держать отдельным venture с собственным backlog;
- знания из чатов нужно поднимать в постоянный контекст, а не терять в диалоге.
- самый близкий структурный аналог на российском рынке — `Getmatch`;
- самый сильный кандидатский конкурент за trust и сопровождение — `careerspace`;
- `hh.ru + Talantix` — главный системный игрок по трафику и employer budget;
- ATS/HRM-платформы вроде `Skillaz`, `Potok`, `FriendWork`, `HURMA`, `VCV` важны, но конкурируют в основном с будущим employer-side stack, а не с core value пилота;
- окно возможности лежит в более узкой, category-specific и agentic-модели для `product/digital middle+`.
- `ICP v1` уже можно зафиксировать как первый рабочий фильтр для кандидатов и компаний.
- candidate interview на первом этапе должен быть узким: ICP qualification, разбор боли текущего поиска и проверка резонанса формата `личный AI-рекрутер`.
- вопросы про role preferences лучше вынести в отдельный survey, чтобы не размывать pain interview.

# Что это изменило
- появилась новая каноническая формулировка проекта;
- появился первый набор гипотез пилота;
- появилась идея долгой LLM-first memory system.
- появился более чёткий threat map по российскому рынку;
- стало ясно, что следующая важная работа — verbal positioning и GTM-отстройка, а не просто общий market scan.
- появился первый draft candidate interview questions без смешивания с отдельным preference survey.

# Candidate interview processing
- 3 candidate interviews из Zoom были полностью транскрибированы через Deepgram и сохранены в `10_meetings/2026/transcripts/` как full cleaned transcripts;
- по каждому интервью создан отдельный подробный analytical report в `10_meetings/2026/`;
- по набору интервью собран отдельный synthesis file с чтением через `ICP / Pain / Value / Gain / Hypothesis readout`;
- для `jjforrussia` это стало первым полным циклом `recording -> transcript -> report -> synthesis`, который потом можно превращать в отдельный skill.

# Что показали первые 3 интервью
- `prodakt-2` дал сильный `core fit` под первую волну: middle PM, реальный product ownership, высокая pain intensity, внятный response на формат `личный AI-рекрутер`;
- `proadkt-1` оказался `partial fit`: технический и integrator-heavy продуктовый переход, полезный как gray-zone сегмент;
- `prodakt-3` не подходит в `core PM` wedge, но выглядит валидным кандидатом для отдельного `CPO / head-level digital product leadership` сегмента;
- после этого стало ясно, что слишком тонкое деление на `external/internal` сейчас только сузит supply и не нужно на уровне top-level segmentation;
- рабочая рамка упрощена до 2 сегментов: `core PM` и `CPO/head-level`.
