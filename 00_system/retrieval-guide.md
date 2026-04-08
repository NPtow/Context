---
title: Retrieval Guide
type: protocol
status: active
updated_at: 2026-04-08
---

# Цель
Дать LLM минимальный путь чтения для разных типов вопросов.

# Routing

## 1. Вопрос про текущий проект
Начать с:
1. [context-map.md](/tmp/Context/context-map.md)
2. `02_ventures/<active>/README.md`
3. `02_ventures/<active>/canonical/current-state.md`

Если нужно больше:
4. `02_ventures/<active>/working/hypotheses.md`
5. последний project session log

Не читать по умолчанию:
- архив
- founder-memory
- другие ventures

## 2. Вопрос про Никиту
Начать с:
1. `01_founder/working-with-nikita.md`
2. `01_founder/preferences.md`

Если нужно больше:
3. `01_founder/profile.md`
4. свежий session log

## 3. Вопрос про домен или рынок
Начать с:
1. релевантный файл из `03_domains/`
2. активный project `current-state.md`, если вопрос связан с конкретным проектом

## 4. Вопрос "что изменилось"
Начать с:
1. `06_decisions/decision-log.md`
2. последний `07_sessions/...`
3. последний project session log

## 5. Вопрос "что было раньше"
Начать с:
1. текущий `canonical/current-state.md`
2. `decision-log`
3. прошлые sessions
4. при необходимости `08_archive/`

## 6. Вопрос про задачи
Начать с:
1. `09_tasks/active-index.md`

Если вопрос про конкретный проект:
2. `09_tasks/projects/<project>.md`

Если вопрос про формат или добавление:
3. `09_tasks/task-schema.md`

# Token budget rules

- Сначала читать максимум 3 файла.
- Расширять чтение только если ответа недостаточно.
- Предпочитать summary и canonical-файлы.
- Session logs читать только как evidence.

# Если проект неочевиден
- Использовать ближайший контекст диалога.
- Если уверенность низкая, задать один короткий вопрос.
