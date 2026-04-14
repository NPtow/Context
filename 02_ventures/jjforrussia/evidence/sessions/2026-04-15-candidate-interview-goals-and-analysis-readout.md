---
title: Candidate Interview Goals And Analysis Readout
type: evidence
venture: jjforrussia
status: active
updated_at: 2026-04-15
---

# Что было нужно понять

По Context видно, что интервью с кандидатами были не самостоятельной целью, а входным исследовательским слоем для пилота.

Главная цель пилота зафиксирована выше:
- не "провести интервью";
- а получить хотя бы `1` успешную оплату от работодателя за найденного и устроенного кандидата.

На этом фоне candidate interviews были нужны как более узкий инструмент, чтобы:
- проверить, существует ли candidate-side боль поиска;
- отфильтровать, кто вообще попадает в first-wave wedge;
- понять, как реально устроен поиск у PM-кандидатов;
- проверить, есть ли отклик на более точный matching / routing / guidance layer;
- понять, кого можно вести дальше в ручном пилоте.

# Какие данные интервью должны были дать

Из project artifacts и hypotheses следует, что после созвона нужно было получить не "общее впечатление", а конкретный набор данных:

1. `ICP / segment fit`
- core first-wave PM;
- adjacent / gray-zone;
- head-level separate track;
- not fit.

2. `Реальная роль, а не только тайтл`
- что человек реально делал;
- был ли у него свой product ownership;
- где роль была продуктовой, а где координационной, внедренческой или сервисной.

3. `Как человек реально выходит на рынок`
- активный поиск, пассивный мониторинг или network-led поиск;
- публичные площадки, прямые касания, люди, скрытый рынок;
- где именно ломается процесс.

4. `Живая боль`
- не общий тезис "рынок плохой";
- а конкретный bottleneck, который портит результат или отнимает время.

5. `Реакция на концепт`
- есть ли отклик на curated matching / routing / сопровождение;
- что выглядит ценным;
- что вызывает недоверие.

6. `Решение после интервью`
- вести;
- отложить;
- не вести.

# Что было нужно получить именно по первой десятке

По sprint plan rebase первая десятка интервью нужна была не только для pain discovery, но и для более прикладного readout:
- сделать summary первых `10` интервью с продактами;
- собрать инсайты;
- понять, работает ли ценностное предложение;
- понять, есть ли после интервью первые сигналы вида `давайте, мы готовы`.

То есть цель первой десятки была двойной:
- исследовательская: понять сегмент, pain-map и search mechanics;
- практическая: увидеть первые action signals и не продолжать строить продукт вслепую.

# Что уже было как методология

В Context methodology не отсутствовала полностью. Она уже существовала, но была разложена по нескольким документам:

- [candidate-interview-protocol-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-protocol-v1.md)
- [candidate-interview-protocol-v2.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-protocol-v2.md)
- [candidate-intake-fields-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-intake-fields-v1.md)
- [candidate-call-note-template-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-call-note-template-v1.md)
- [pm-role-taxonomy-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/pm-role-taxonomy-v1.md)
- [2026-04-08-jjfr-candidate-interviews-synthesis.md](/Users/NIKITA/.codex/context/Context/10_meetings/2026/2026-04-08-jjfr-candidate-interviews-synthesis.md)
- [2026-04-08-product-pivot.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-08-product-pivot.md)

Из них уже вытекал рабочий контур:
- `recording -> transcript -> per-interview note -> synthesis`;
- чтение интервью через `ICP / pain / value / hypothesis readout`;
- сохранение note и transcript отдельно;
- использование taxonomy и intake fields как стабилизатора анализа.

# Где был явный gap

При этом явного одного документа с answer на вопрос "как анализировать следующую волну интервью одинаково" не было.

Не хватало:
- явного разделения между `problem exists`, `this is our wedge` и `this person will act`;
- правил качества сигнала;
- правил, какие выводы считать сильными, а какие contaminated;
- общего метода для cross-interview synthesis после первой тройки и после первой десятки;
- правил, когда что поднимать в `working/hypotheses`, а когда оставлять на уровне notes.

# Что не было подтверждено интервью само по себе

По текущему Context нельзя считать, что интервью сами по себе доказывают:
- реальную готовность пользоваться сервисом;
- willingness to pay;
- product-market fit.

Интервью дают сильный signal про:
- сегментацию;
- candidate pain;
- search mechanics;
- trust blockers;
- language of value.

Но action-read и real demand должны подтверждаться уже следующим поведением, а не только словами в созвоне.

# Решение

В качестве следующего шага к этой evidence note добавлен отдельный reusable документ:
- [candidate-interview-analysis-method-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-analysis-method-v1.md)

Его задача:
- собрать разрозненные analytical rules в одну рамку;
- унифицировать per-interview readout;
- сделать следующую wave synthesis менее интуитивной и более сравнимой.

# Files used

- [current-state.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/canonical/current-state.md)
- [hypotheses.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/working/hypotheses.md)
- [candidate-interview-protocol-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-protocol-v1.md)
- [candidate-interview-protocol-v2.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-protocol-v2.md)
- [candidate-intake-fields-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-intake-fields-v1.md)
- [candidate-call-note-template-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-call-note-template-v1.md)
- [candidate-interviews-synthesis.md](/Users/NIKITA/.codex/context/Context/10_meetings/2026/2026-04-08-jjfr-candidate-interviews-synthesis.md)
- [product-pivot.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-08-product-pivot.md)
- [sprint-plan-rebase.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-13-sprint-plan-rebase.md)
