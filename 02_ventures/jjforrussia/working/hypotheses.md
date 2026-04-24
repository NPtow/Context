---
title: Hypotheses
type: working
venture: jjforrussia
status: active
updated_at: 2026-04-25
---

# Главные гипотезы пилота

## Г1. Кандидатская боль реальна
Product-кандидаты устали от хаотичного поиска, низкой конверсии в интервью и отсутствия обратной связи.

## Г2. Формат "личный AI-рекрутер" ощущается как отдельная ценность
Для кандидатов это не просто GPT, а сервис, который ведет их в релевантные процессы.

## Г3. Работодателю нужен shortlist, а не поток откликов
HR и hiring managers по PM-ролям страдают от низкого качества входящей воронки.

## Г4. Success fee продаваем
Работодатели готовы тестировать пилот с оплатой за успешный найм.

## Г5. Для product-ролей можно собрать рабочий фильтр
Если структурировать профиль кандидата, тип роли и причины отказов, можно вручную делать качественный мэтч.

## Г6. Пилот можно провести вручную
На первом этапе достаточно candidate onboarding, ручного intake вакансии и ручного matching workflow.

## Г7. Рынок открыт для более узкой и agentic-модели
Несмотря на наличие сильных игроков, на российском рынке пока нет доминирующего публичного продукта, который одновременно сочетает:
- доверительный candidate-side агент;
- employer-side shortlist;
- success fee за placement;
- узкий vertical focus на `product/digital middle+`.

## Г8. Отстройка от `Getmatch` / `careerspace` / `hh` критична
Если продукт будет считываться как "ещё один curated job service" или "карьерная помощь", он проиграет более сильным брендам. Нужен более острый тезис про calibration, релевантные процессы и employer-paid outcome.

## Г9. Краткосрочный employer-side спрос может быть сжат рынком
Даже если candidate-side боль и ручной matching реально работают, hire freeze и общее охлаждение найма могут резко просадить число живых PM-вакансий и замедлить монетизацию. Поэтому в ближайшем спринте надо смотреть не только на raw replies, но и на:
- готовность HR / HM идти в разговор;
- готовность делиться structured role data;
- наличие реальных live briefs, а не просто вежливого интереса.

# Что считаем успехом
- хотя бы 1 успешная оплата от работодателя;
- 2-3 живые вакансии;
- 10-15 калиброванных кандидатов;
- 3-5 ручных мэтчей;
- фидбек от HR / hiring manager.
- понятная verbal positioning, которую можно противопоставить `Getmatch`, `careerspace` и `hh`.

# Текущий readout после первых 3 candidate interviews

## Что уже выглядит подтвержденным
- `Г1` сейчас выглядит сильно поддержанной: во всех 3 интервью есть реальная и содержательная pain-map, а не абстрактное "рынок плохой";
- `Г5` уже поддержана: интервью позволяют уверенно разделять `fit / partial fit / not fit`;
- `Г6` тоже поддержана: manual triage и manual candidate calibration уже выглядят рабочими.

## Что пока подтверждено слабее
- `Г2` пока поддержана только слабо или умеренно: прямой value block по формату `личный AI-рекрутер` полноценно прошёл не во всех интервью;
- для более уверенного подтверждения `Г2` нужен ещё набор интервью с одинаковым direct question block.
- `Г4` и новая market-risk гипотеза пока остаются слабо проверенными: есть интуиция про hire freeze и сокращение вакансий, но пока мало живых employer-side разговоров, чтобы отделить макрориск от плохого аутрича или слабого оффера.

# Current readout после HR corpus v2

## Что теперь выглядит подтверждённее по employer-side боли

- `Г3` усилилась: после model-reviewed пересборки HR-корпуса есть повторяющийся и ссылочно подтверждённый набор тем про:
  - слабый сигнал о кандидате;
  - рассинхрон рекрутера и нанимающего менеджера;
  - потери кандидатов внутри воронки;
  - ошибку найма, которая вскрывается после выхода;
- `Г8` тоже стала конкретнее: отстройка должна идти не через обещание "больше кандидатов", а через calibration, shortlist quality и снижение ошибки решения.

## Что всё ещё нельзя считать подтверждённым

- `Г4` по-прежнему слабо подтверждена: HR-корпус показывает pain и язык рынка, но не доказывает willingness to pay.
- company-level target list пока не подтверждён: mention компании в HR-посте не равен доказанной боли компании.
- `Г9` остаётся открытой: content evidence по рынку не заменяет живые employer-side discovery calls и реальные hiring briefs.

## Что это подсветило про сегментацию
- first-wave core segment по-прежнему выглядит как `middle / middle+ / senior PM` в digital product companies;
- рядом уже всплыл отдельный `CPO / head-level` segment, который не надо смешивать с core wedge;
- технические и integrator-heavy PM-переходы пока стоит держать как gray-zone, а не как автоматический fit или no-fit.

# Current readout после HH AI recruiting event

## Что усилилось

- `Г3` усилилась ещё одним source-backed сигналом: крупные hiring-функции говорят не про нехватку резюме, а про слабый candidate signal, AI-distorted evidence, разрыв профиля и сложность принятия hiring decisions.
- `Г5` стала конкретнее: working filter для product roles должен быть не просто taxonomy, а `role profile -> skills -> indicators -> observed evidence -> risks / next probes`.
- `Г8` усилилась: отстройка от `hh` и enterprise ATS должна идти через узкий trusted evidence layer, а не через generic AI recruiter promise.
- Появился рабочий adjacent wedge: `AI-use skill assessment` как consent-based task для ролей, где умение пользоваться AI уже является частью работы.

## Что это не доказывает

- `Г4` всё ещё не доказана: event показывает pain language и operating patterns, но не willingness to pay.
- Тезис о конкретной стратегии HH по AI recruiter / AI career consultant сохранён как заметка Никиты, но доступные аудио не дают полного transcript-level подтверждения.
- Anti-fraud не стоит считать самостоятельным продуктом без assessment design, human review and post-hire validation.

## Новый рабочий artifact для проверки

- `candidate evidence pack v0`:
  - role brief and critical skills;
  - candidate evidence by skill;
  - evidence strength;
  - unresolved risks;
  - suggested next HM probes;
  - optional AI-use task trace.

# Current readout после уточнения skill-based механики

## Что теперь является рабочей продуктовой формулировкой

- Продукт не разворачивается в отдельный сервис "сделаем вам матрицу компетенций".
- Матрица компетенций становится основанием оценки и фильтрации внутри текущего продукта.
- Рабочая формула: `матрица роли × матрица кандидата`.
- Работодатель приходит с ролью; через разговор с работодателем / нанимающим менеджером роль раскладывается на навыки, поведенческие признаки, критичные требования и допустимые компромиссы.
- Кандидат проходит базовый созвон; из созвона собирается матрица кандидата: подтверждённые навыки, уровень опыта, поведенческие сигналы, риски, зоны, которые ещё не проверены.
- Матчинг строится не как "резюме подходит к вакансии", а как сравнение двух структур: чего требует роль и что кандидат реально показал или убедительно подтвердил.

## Какие гипотезы это усиливает

- `Г3` становится конкретнее: работодатель получает не поток откликов, а объяснимый отбор по критериям роли.
- `Г5` становится центральной: рабочий фильтр теперь должен уметь превращать созвон и brief в сравнимые матрицы.
- `Г8` получает более ясную отстройку: против `hh` и обычных баз кандидатов продукт может продавать не доступ к резюме, а доказательный слой оценки.
- `candidate evidence pack v0` нужно развивать в сторону `role matrix / candidate matrix / comparison summary`.

## Что нужно валидировать отдельно

- Понимают ли HR и нанимающие менеджеры формулировку `матрица роли × матрица кандидата`, или её нужно переводить в более простой язык вроде "покажем, почему человек подходит именно под вашу роль".
- Достаточно ли одного базового созвона, чтобы собрать надёжную матрицу кандидата, особенно по мягким навыкам.
- Какие soft signals можно честно извлекать из созвона, а какие нужно помечать как слабые гипотезы.
- Насколько работодатель готов доверять сравнению матриц, если рядом есть резюме, прошлые компании и привычные интервью.
- Улучшает ли такая выдача perceived relevance по сравнению с обычным shortlist.

## Будущая идея, но не текущий обязательный слой

- "Аватар нанимающего менеджера" стоит понимать как кодирование критериев нанимающего менеджера и его логики отбора, а не как автономное решение о найме.
- Возможная польза: расширить верх воронки, проводить первичный разговор с большим числом кандидатов и объяснять, почему кандидат проходит или не проходит дальше.
- Риск: если это подать как "ИИ решает, брать или не брать", доверие и юридическая/этическая устойчивость будут слабее. Корректнее говорить про помощника, который собирает evidence и готовит решение для человека.

# Current evidence

## Primary evidence files
- [../evidence/sessions/2026-04-08-product-pivot.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-08-product-pivot.md)
- [../artifacts/icp-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/icp-v1.md)
- [../../10_meetings/2026/2026-04-08-jjfr-candidate-interviews-synthesis.md](/Users/NIKITA/.codex/context/Context/10_meetings/2026/2026-04-08-jjfr-candidate-interviews-synthesis.md)

## Source-backed packs
- [../evidence/sources/2026-04-08-russian-market-scan.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-08-russian-market-scan.md)
- [../evidence/sources/2026-04-08-candidate-interviews-wave-1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-08-candidate-interviews-wave-1.md)
- [../evidence/sources/2026-04-12-pusser-zheleznov-transcript.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-12-pusser-zheleznov-transcript.md)
- [../evidence/sessions/2026-04-14-hr-topic-research-v2-evidence.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-14-hr-topic-research-v2-evidence.md)
- [../evidence/sources/2026-04-24-hh-ai-recruiting-event.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sources/2026-04-24-hh-ai-recruiting-event.md)
- [../evidence/sessions/2026-04-24-hh-event-analysis.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-24-hh-event-analysis.md)
- [../evidence/sessions/2026-04-25-skill-based-matching-mechanism.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-25-skill-based-matching-mechanism.md)
- [../artifacts/skill-based-matching-mechanism-v0.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/skill-based-matching-mechanism-v0.md)

# Read next
- [README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/README.md)
- [../evidence/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/README.md)
- [../artifacts/README.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/README.md)
