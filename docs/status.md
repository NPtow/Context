# Status: LLM-first memory system для `Context`

## Current phase
`Execution complete / ready to push`

## Goal
Подготовить репозиторий `Context` как долгую память для LLM:
- с короткими командами на естественном языке;
- с актуальным слоем, логами, памятью о Никите и архивом;
- с retrieval-механикой, не требующей читать все подряд.

## Done
- [x] Подтверждено, что репозиторий пустой и можно заложить архитектуру с нуля.
- [x] Зафиксированы ключевые требования пользователя:
  - основной потребитель — LLM;
  - команды на естественном языке;
  - `обновись` должен обновлять проект + session log + память о Никите при наличии новых паттернов;
  - активный проект определяется по диалогу;
  - при низкой уверенности допустим один уточняющий вопрос.
- [x] Сформирован плановый пакет в `docs/`.

## In progress
- [~] Финальная проверка перед git commit и push.

## Next
- [ ] Закоммитить структуру, seed-контент и протоколы.
- [ ] Запушить initial version в `NPtow/Context`.
- [ ] На следующем проходе сократить возможные retrieval-paths, если появится лишнее чтение.

## Decisions
- Репозиторий строится как `LLM-first memory system`, а не как проектная папка.
- Команды задаются обычными фразами, без слэшей.
- Долгая память о Никите выделяется в отдельный слой и обновляется не всегда, а только при устойчивых новых сигналах.

## Assumptions
- Пустой репозиторий не содержит ограничений по существующей структуре.
- Основной рабочий язык документов — русский; имена файлов и часть метаданных могут быть на английском.
- На первой итерации достаточно markdown + index files, без внешних систем поиска.

## Blockers
- Нет технических блокеров.
- Есть продуктовая точка согласования: подтверждение на исполнение структуры и seed-контента.

## Commands
- Inspect repo:
  - `cd /tmp/Context && git status --short --branch`
  - `cd /tmp/Context && find . -maxdepth 2 | sort`
- Read plan:
  - `cd /tmp/Context && sed -n '1,260p' docs/plans.md`
- Read test plan:
  - `cd /tmp/Context && sed -n '1,260p' docs/test-plan.md`

## Audit log
- 2026-04-08: cloned `NPtow/Context`; repository is empty.
- 2026-04-08: clarified target behavior for `обновись`, retrieval, project inference, and founder-memory updates.
- 2026-04-08: drafted execution plan, status file, and test plan.
- 2026-04-08: created root memory architecture, command protocol, retrieval guide, founder-memory seed, referalka seed, domain notes, and decision log.
- 2026-04-08: verified index-first retrieval path through `context-map.md`.

## Smoke / demo checks for next run
- Показать дерево структуры после Milestone 1.
- Показать пример того, какие файлы прочитает LLM при запросе `что мы решили по рефералке`.
- Показать пример того, что обновит команда `обновись`.
