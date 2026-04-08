# Status: LLM-first memory system для `Context`

## Current phase
`Initialized and pushed`

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
- [~] Следующий проход должен проверить реальное удобство retrieval на новых сессиях, а не только на seed-контенте.
- [~] Команда `обновись` уже прогнана на live-run и теперь покрывает system-level updates для самого `Context`.
- [~] Добавлен общий task-layer; теперь нужно проверить, что task-команды работают так же стабильно, как project-команды.

## Next
- [x] На следующем проходе прогнать `обновись` на живом новом диалоге.
- [ ] Проверить, не нужно ли ужать founder-memory или project seed для экономии токенов.
- [ ] Добавить playbook для `архивируй проект`, когда появится первый завершенный venture.
- [ ] Добавить отдельный playbook для system-level updates внутри `Context`.
- [ ] Прогнать `поставить задачу` и `все задачи по проекту X` на живом запросе.

## Decisions
- Репозиторий строится как `LLM-first memory system`, а не как проектная папка.
- Команды задаются обычными фразами, без слэшей.
- Долгая память о Никите выделяется в отдельный слой и обновляется не всегда, а только при устойчивых новых сигналах.
- Команда `обновись` должна уметь обновлять не только venture, но и system-level контекст самого `Context`.
- У задач должен быть отдельный общий слой, а не размазанность по `status`, `sessions` и `open edges`.

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
- 2026-04-08: committed and pushed initial version to `NPtow/Context`.
- 2026-04-08: executed first live `обновись` run and clarified system-level update behavior.
- 2026-04-08: added a global task layer with project-specific task files and task commands.

## Smoke / demo checks for next run
- Показать дерево структуры после Milestone 1.
- Показать пример того, какие файлы прочитает LLM при запросе `что мы решили по рефералке`.
- Показать пример того, что обновит команда `обновись`.
- Показать разницу между venture update и system-level update.
