# Status: LLM-first memory system для `Context`

## Current phase
`Balanced detail, path-aware retrieval and source-layer backfill are being added on top of the standalone report artifacts`

## Goal
Подготовить репозиторий `Context` как долгую память для LLM:
- с короткими командами на естественном языке;
- с актуальным слоем, логами, памятью о Никите и архивом;
- с retrieval-механикой, не требующей читать все подряд;
- с `balanced` уровнем детализации по умолчанию, явной source-lineage и точной адресацией по папкам.

## Done
- [x] Подтверждено, что репозиторий пустой и можно заложить архитектуру с нуля.
- [x] Зафиксированы ключевые требования пользователя:
  - основной потребитель — LLM;
  - команды на естественном языке;
  - `обновись` должен обновлять проект + session log + память о Никите при наличии новых паттернов;
  - активный проект определяется по диалогу;
  - при низкой уверенности допустим один уточняющий вопрос.
- [x] Сформирован плановый пакет в `docs/`.
- [x] Task-layer проверен не только через markdown retrieval, но и через отдельный live viewer, читающий `09_tasks/projects/*.md` напрямую из GitHub.
- [x] Для task-layer собран и задеплоен standalone preview service `context-viewer` вне продуктового приложения `referalka`.
- [x] HR-tech report-site вынесен из `referalka` и собран как отдельный static artifact внутри `Context`.
- [x] В `Context` добавлены `source/`, `build-report-data.mjs`, `report-data.json` и `index.html` для HR-tech report-site.
- [x] Системные протоколы и локальные skills переведены в `balanced detail by default` вместо lean-only retrieval.
- [x] Для `jjforrussia` добавлены folder indexes и venture source-layer с первыми source packs.
- [x] Для recruiting-domain добавлены локальные folder indexes, чтобы ходить точечно по папкам, а не только по top-level summary.
- [x] Добавлен system-level `skill-hub`, который зеркалит локальные skills внутрь `Context` и даёт cloud-readable skill index.
- [x] В `skill-hub` опубликован первый cloud skill `telegram-hiring-contact-sourcing`, а его каноническая версия удержана в безопасной `Telethon + own account` рамке.

## In progress
- [~] Следующий проход должен проверить реальное удобство retrieval на новых сессиях, а не только на seed-контенте.
- [~] Команда `обновись` уже прогнана на live-run и теперь покрывает system-level updates для самого `Context`.
- [~] Появился новый automation-use-case `обновись ко всем чатам`: локальные `.codex/sessions/*.jsonl` уже подходят как input для system-level synthesis, но под этот проход ещё не оформлен отдельный playbook с windowing и signal-threshold rules.
- [~] Добавлен общий task-layer; теперь нужно проверить, что task-команды работают так же стабильно, как project-команды.
- [~] Venture-memory разделена: старая `referalka` и новый `jjforrussia` больше не смешиваются в одном canonical state.
- [~] Добавлен отдельный meetings-layer и skill для записи встреч в Context.
- [~] Появился внешний UI-слой для задач; теперь нужно решить, останется ли он просто preview-инструментом или станет постоянной operator surface для `Context`.
- [~] Появился второй внешний UI-слой: отдельный HR-tech report-site по recruiting landscape.
- [~] Новый path-aware режим ещё нужно прогнать на живых query/update drills, чтобы проверить, что detail вырос без потери управляемости.
- [~] `skill-hub` теперь уже используется не только как зеркало локальных skills, но и как хранилище cloud-first skill truth; дальше нужно проверить, насколько удобно это работает в живых retrieval/update циклах.
- [~] В новых UI-задачах повторяется запрос на browser-connected, screen-by-screen workflow с быстрым утверждением конкретного вида и анимации; пока это ещё operator pattern, а не формализованный reusable skill.

## Next
- [x] На следующем проходе прогнать `обновись` на живом новом диалоге.
- [x] Прогнать live task query и визуально проверить task-layer на отдельном viewer.
- [ ] Прогнать retrieval drill `покажи контекст проекта по jjforrussia`.
- [ ] Прогнать retrieval drill `покажи контекст проекта в 02_ventures/jjforrussia/artifacts`.
- [ ] Прогнать retrieval drill `что изменилось в 03_domains/recruiting/hr-tech-report-site/source`.
- [ ] Прогнать update drill `обновись по jjforrussia` и `сохрани сессию в 02_ventures/jjforrussia/evidence/sources`.
- [ ] Добавить playbook для `архивируй проект`, когда появится первый завершенный venture.
- [ ] Добавить отдельный playbook для system-level updates внутри `Context`.
- [ ] Описать отдельный playbook для `обновись ко всем чатам`: какое окно локальных session logs читать, как фильтровать low-signal threads и когда делать cross-project synthesis вместо venture rewrite.
- [ ] Прогнать `поставить задачу` и `все задачи по проекту X` на живом запросе.
- [ ] Прогнать retrieval drill по `00_system/skill-hub` на живом skill-вопросе.
- [ ] Прогнать live use-case по `telegram-hiring-contact-sourcing` на собственном легитимном Telegram-аккаунте и проверить, хватает ли reference-layer без серых workaround-ов.
- [ ] Решить, нужен ли task viewer внутри самого `Context` repo как постоянный артефакт, а не только как внешний deploy.
- [ ] Завершить отдельный Vercel deploy для `03_domains/recruiting/hr-tech-report-site`.
- [ ] Решить, нужно ли под report-site заводить постоянный project / domain или оставить как preview-only artifact.
- [ ] Решить, оформлять ли browser-driven UI iteration как отдельный `live-screen-copy`-style skill или оставить это operator-only режимом.

## Decisions
- Репозиторий строится как `LLM-first memory system`, а не как проектная папка.
- Команды задаются обычными фразами, без слэшей.
- Долгая память о Никите выделяется в отдельный слой и обновляется не всегда, а только при устойчивых новых сигналах.
- Команда `обновись` должна уметь обновлять не только venture, но и system-level контекст самого `Context`.
- У задач должен быть отдельный общий слой, а не размазанность по `status`, `sessions` и `open edges`.
- Смешанные project memories нужно при необходимости разделять на отдельные venture, а не пытаться хранить все под одним именем.
- Внешние интерфейсы поверх `Context` лучше держать как standalone сервисы, не смешивая их с продуктовым runtime и его env-зависимостями.
- HR-tech market report должен жить отдельно от `referalka`; `Context` — правильное место для кода и snapshot-данных этого артефакта.
- Default retrieval mode должен быть `balanced`, а не максимально lean.
- Addressable folders должны иметь локальный `README.md`, а source-heavy claims должны получать reusable source packs.
- Skills, нужные cloud-агенту, лучше хранить как реальные repo-копии внутри `Context`, а не как ссылки на локальную ФС.

## Assumptions
- Пустой репозиторий не содержит ограничений по существующей структуре.
- Основной рабочий язык документов — русский; имена файлов и часть метаданных могут быть на английском.
- На первой итерации достаточно markdown + index files, без внешних систем поиска.

## Blockers
- Нет технических блокеров.
- Остаётся методологическая проверка: не расползётся ли новый detail mode в raw dump без достаточной маршрутизации.

## Commands
- Inspect repo:
  - `cd /Users/NIKITA/.codex/context/Context && git status --short --branch`
  - `cd /Users/NIKITA/.codex/context/Context && find . -maxdepth 2 | sort`
- Read plan:
  - `cd /Users/NIKITA/.codex/context/Context && sed -n '1,260p' docs/plans.md`
- Read test plan:
  - `cd /Users/NIKITA/.codex/context/Context && sed -n '1,260p' docs/test-plan.md`

## Audit log
- 2026-04-08: cloned `NPtow/Context`; repository is empty.
- 2026-04-08: clarified target behavior for `обновись`, retrieval, project inference, and founder-memory updates.
- 2026-04-08: drafted execution plan, status file, and test plan.
- 2026-04-08: created root memory architecture, command protocol, retrieval guide, founder-memory seed, referalka seed, domain notes, and decision log.
- 2026-04-08: verified index-first retrieval path through `context-map.md`.
- 2026-04-08: committed and pushed initial version to `NPtow/Context`.
- 2026-04-08: executed first live `обновись` run and clarified system-level update behavior.
- 2026-04-08: added a global task layer with project-specific task files and task commands.
- 2026-04-08: split old `referalka` from the new AI-recruiting line and created separate venture `jjforrussia`.
- 2026-04-08: added `10_meetings` layer and local Deepgram-based meeting transcription skill.
- 2026-04-08: built standalone `context-viewer` service for `09_tasks`, validated live GitHub fetch, and deployed a Vercel preview.
- 2026-04-08: moved the HR-tech report surface out of `referalka`, created standalone site code in `Context`, and prepared it for separate Vercel deployment.
- 2026-04-08: switched system protocols and local skills from lean retrieval defaults to balanced, path-aware, source-backed retrieval and update behavior.
- 2026-04-08: added folder indexes and the first venture source packs for `jjforrussia`.
- 2026-04-10: added `00_system/skill-hub` with a sync script, mirrored local skills, and a machine-readable registry for cloud access.
- 2026-04-11: added the first cloud-published skill `telegram-hiring-contact-sourcing`, a Telegram setup/troubleshooting source pack, and aligned the canonical skill back to a safe own-account Telethon workflow.
- 2026-04-17: audited local Codex sessions for `2026-04-16 ... 2026-04-17`, added a system-level daily synthesis for `обновись ко всем чатам`, and recorded new operator signals around browser-driven UI iteration and all-chat synthesis.

## Smoke / demo checks for next run
- Показать дерево структуры после Milestone 1.
- Показать пример того, какие файлы прочитает LLM при запросе `что мы решили по рефералке`.
- Показать пример того, что обновит команда `обновись`.
- Показать разницу между venture update и system-level update.
