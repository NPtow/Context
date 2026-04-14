---
title: Candidate Interview Analysis Method v1
type: artifact
venture: jjforrussia
status: active
updated_at: 2026-04-15
---

# JJFORRUSSIA · Метод анализа candidate interviews v1

## Зачем нужен этот документ

- Собрать в одно место правила анализа кандидатских интервью.
- Сделать readout по интервью сравнимым между собой.
- Уменьшить риск, что следующий synthesis снова будет зависеть только от интуиции интервьюера.

## Что этот метод должен отвечать

После анализа одного интервью должно быть ясно:

1. Это наш сегмент или нет.
2. Есть ли у человека живая проблема, а не просто разговорный шум.
3. Как у него реально устроен поиск.
4. На что именно он откликается в концепте решения.
5. Есть ли у него action signal, а не только вежливое согласие.
6. Что это меняет для pilot wedge и гипотез.

## На каких документах строится

- [candidate-interview-protocol-v2.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-interview-protocol-v2.md)
- [candidate-intake-fields-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-intake-fields-v1.md)
- [candidate-call-note-template-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/candidate-call-note-template-v1.md)
- [pm-role-taxonomy-v1.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/pm-role-taxonomy-v1.md)
- [working/hypotheses.md](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/working/hypotheses.md)

## Входы для анализа

Минимальный вход:
- meeting note;
- raw transcript или cleaned transcript, если он сохранён;
- текущая taxonomy ролей;
- текущие hypotheses проекта.

Если transcript нет, analysis допустим, но confidence ниже.

## Единица анализа: одно интервью

По каждому интервью нужно заполнить не меньше восьми полей:

1. `Segment tag`
- `core PM`
- `head/CPO`
- `adjacent`
- `gray zone`
- `not fit`

2. `Role reality`
- что реально делал;
- какой был ownership;
- где тайтл вводит в заблуждение.

3. `Search mode`
- активный отклик;
- direct/network;
- hidden market;
- пассивный мониторинг;
- смешанный режим.

4. `Pain`
- одна главная боль;
- насколько она конкретна;
- какой эпизод её подтверждает.

5. `Workaround`
- что человек уже делает, чтобы это обойти.

6. `Value resonance`
- что ему звучит ценным;
- что вызывает недоверие.

7. `Action signal`
- готов ли он сделать следующий шаг;
- это verbal signal или уже behavioral signal.

8. `Recommendation`
- `вести`
- `отложить`
- `не вести`

## Правила качества сигнала

### Strong signal

Считать сильным, если есть хотя бы два из трёх признаков:
- недавний конкретный эпизод;
- наблюдаемое поведение или workaround;
- числа, диапазоны или другой проверяемый факт.

Примеры:
- кандидат описывает последний провалившийся процесс;
- кандидат уже придумал свой обходной путь;
- кандидат называет объём откликов, ответов или длительность цикла.

### Medium signal

Считать средним, если:
- есть содержательная мысль;
- но нет чисел или поведенческого подтверждения;
- или пример слишком общий.

### Weak or contaminated signal

Считать слабым или загрязнённым, если:
- это broad market opinion без примера;
- это реакция после длинного pitch;
- это ответ на наводящий вопрос;
- это гипотетическое `я бы, наверное, пользовался`;
- это пост-объяснение интервьюера, а не raw signal кандидата.

## Три вопроса, которые нельзя смешивать

При synthesis всегда разделять:

1. `Problem exists`
- есть ли повторяющаяся боль вообще.

2. `This is our wedge`
- совпадает ли эта боль с нашей product logic.

3. `This person will act`
- готов ли человек реально что-то сделать дальше.

Один и тот же кандидат может дать:
- сильный signal по боли;
- средний signal по wedge;
- слабый signal по готовности действовать.

Это нормально. Нельзя насильно превращать первое в третье.

## Как делать per-interview readout

### Шаг 1. Сначала сегментация

Ответить:
- это core PM, leadership, adjacent или gray zone;
- почему именно так.

Без этого нельзя интерпретировать остальной pain.

### Шаг 2. Потом mechanics

Нужно понять:
- как человек вообще выходит на рынок;
- где именно идёт поиск;
- это board-led, network-led, hidden-market или passive mode.

Нельзя сравнивать одинаково кандидата из публичного рынка и кандидата, который ищет почти только через людей.

### Шаг 3. Потом pain

Нужно выделить:
- одну главную боль;
- один подтверждающий эпизод;
- цену этой проблемы:
  - время;
  - неопределённость;
  - потерянные процессы;
  - плохой signal quality.

### Шаг 4. Потом concept read

Фиксировать отдельно:
- что звучит ценным;
- что вызывает недоверие;
- не принял ли кандидат твою формулировку только из вежливости.

### Шаг 5. Потом action read

Разделять:
- `verbal resonance`
- `behavioral readiness`

Сильный action signal:
- готов прислать профиль;
- готов тестировать shortlist;
- готов потратить время на следующий шаг.

Слабый action signal:
- `интересно звучит`
- `можно попробовать`
- `да, проблема есть`

## Как делать wave synthesis

Новый synthesis по серии интервью должен содержать только такие блоки:

1. `Scope`
- какие интервью вошли в волну;
- какой был текущий script/protocol.

2. `Cross-interview table`
- сегмент;
- search mode;
- pain severity;
- value resonance;
- action likelihood;
- recommendation.

3. `Reliable repeated findings`
- только повторяющиеся сигналы;
- желательно с явным указанием, в скольких интервью это звучало.

4. `Weak or contaminated findings`
- всё, что появилось после сильного framing;
- всё, что нельзя считать доказательством.

5. `What this changes`
- для ICP;
- для hypotheses;
- для script/protocol;
- для pilot flow.

## Правила повышения выводов по слоям Context

### В `10_meetings`

Пишем всегда:
- note;
- transcript, если он сохранён.

### В project evidence

Поднимать, если:
- появилась новая волна;
- появился новый synthesis;
- есть осмысленный delta относительно прошлой волны.

### В `working/hypotheses`

Поднимать только если:
- signal повторился;
- он влияет на wedge или pilot flow;
- он не опирается только на contaminated concept-test блок.

### В `canonical/current-state`

Поднимать только если:
- решение уже принято;
- сегментация или pilot shape реально изменились;
- это устойчивый, а не одноразовый readout.

## Чего нельзя делать

- Не считать интервью доказательством product-market fit.
- Не считать candidate pain автоматическим доказательством willingness to use.
- Не смешивать `core PM` и `head/CPO` в одну таблицу без отдельной пометки.
- Не строить выводы только из красивых цитат.
- Не поднимать в canonical всё, что звучит умно, но не повторяется.

## Минимальный output после каждой новой волны

После волны интервью должен появиться как минимум один новый артефакт:
- короткий synthesis note;
- или evidence session с readout;
- или update в `working/hypotheses`, если wave реально сдвинула гипотезы.

Если этого не произошло, значит интервью были проведены, но не превращены в usable project memory.
