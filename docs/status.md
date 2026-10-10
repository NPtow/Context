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
- [~] Automation-use-case `обновись ко всем чатам` теперь имеет отдельный playbook с windowing и signal-threshold rules; следующий риск - правильно роутить новые non-JJFR проекты вроде DSA, не смешивая их с active venture.
- [~] Последний all-chat run за 2026-09-21...2026-09-25 был low-signal: product/venture deltas нет, но найден workspace hygiene issue в standup automation для `referalocka`.
- [~] Последний all-chat run за 2026-09-25...2026-09-26 сохранил operational references для DSA, Kaplya и локального Codex model catalog; изменений venture canonical нет.
- [~] Последний all-chat run за 2026-09-28...2026-09-29 выделил два самостоятельных кандидата на routing: «Связность» (развёрнутый прототип карты зависимостей идей) и Proteus (vision/PDF); они не смешаны с `jjforrussia`.
- [~] Последний all-chat run за 2026-09-29...2026-09-30 уточнил Proteus как общий проактивный слой для sales, поддержки, онбординга и автоматизации; «Капля» осталась дизайн-эскизом, оба направления пока session-level.
- [~] Последний all-chat run за 2026-09-30...2026-10-01 зафиксировал HR Vision как отдельную рабочую линию: первая волна из 200 сообщений запланирована на 5 октября, но готовность воронки, аккаунтов, панелей и маршрутов кандидата пока не проверена. DSA-перезапуск, партнерская дека и исследование бизнес-школы остались session-level.
- [~] Последний all-chat run за 2026-10-01...2026-10-02 сохранил выбранный материал локального desktop-прототипа Proteus, интерактивную карту HR Vision и data-integrity риски связки DSA «Прайсы → КП Хаб». Все новые линии остаются session-level до отдельного routing decision.
- [~] Последний all-chat run за 2026-10-02...2026-10-03 подтвердил серверную выкладку DSA для импорта версий прайсов и печати КП, рабочие desktop-итерации Proteus и опубликованный демонстрационный пакет HR Vision. Все линии остаются session-level: у DSA и HR Vision нет отдельного project path, а у Proteus не подтверждена product-ready сборка.
- [~] Последний all-chat run за 2026-10-03...2026-10-04 сохранил короткую внешнюю деку и закрытый видеопоказ HR Vision, а также диагностированные пробелы capture-loop/recovery в Proteus и контрактные расхождения сайта DSA с КП Хабом. Это подтвержденные session-level результаты: исправление Proteus, production-playback и end-to-end сверка КП не выполнены.
- [~] Последний all-chat run за 2026-10-04...2026-10-05 выделил trigger-блок Proteus как v2-кандидат, сохранив его исследовательские и UI-материалы отдельно от live execution; для HR Vision добавлены evidence-границы вокруг формы оценки кандидатов. Новые линии остаются session-level.
- [~] Последний all-chat run за 2026-10-05...2026-10-06 сохранил узкую очистку диагностических логов DSA, блокирующее C4-ревью локальных правок КП Хаба, инвентаризацию TG-конвейера, read-only мост Proteus Building и корень macOS memory warning. Все линии остаются session-level до отдельного routing или release decision.
- [~] Последний all-chat run за 2026-10-06...2026-10-07 подтвердил production-релиз КП Хаба и прайсов после ограниченного gate, локальную сборку DSA Sales, обновление DSA-распределителя и подготовленный HR Vision workflow. Все линии остаются session-level: live-сценарии КП, UX-семантика метрик и сквозное голосовое интервью требуют отдельных проверок.
- [~] Последний all-chat run за 2026-10-07...2026-10-08 сохранил конфигурацию DSA SEO/GEO-мониторинга и локальный исследовательский пакет Proteus по памяти. Первый замер, подтверждение домена в аналитике и продуктовая интеграция материалов не выполнены; линии остаются session-level.
- [~] Последний all-chat run за 2026-10-08...2026-10-09 подтвердил доступность DSA-распределителя на уровне systemd и endpoint, но не сквозной сценарий Bitrix: `Access denied` для вспомогательного поля зафиксирован, а видимая UI-ошибка не воспроизведена. Линия остается session-level до проверки в контексте портала.
- [~] Последний all-chat run за 2026-10-09...2026-10-10 сохранил локальный контур резервного копирования YC, подготовленную 10-слайдовую DSA-деку и HR Vision research-пакет о сигналах компаний. Резервные копии были свежими на последней проверке; исследование не означает запуск коллекторов, платных API или работу с реальными компаниями. Все линии остаются session-level до отдельного routing или внедрения.
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
- [x] Описать отдельный playbook для `обновись ко всем чатам`: какое окно локальных session logs читать, как фильтровать low-signal threads и когда делать cross-project synthesis вместо venture rewrite.
- [ ] Решить, заводить ли `DSA` как отдельный venture/domain в `Context` после появления большого sales-ops сигнала.
- [ ] Починить или перенастроить standup automation workspace для `referalocka`: сохраненный путь ведет к broken symlink в `/Users/NIKITA/Downloads/referalocka`, рабочий checkout найден в `/Users/NIKITA/Projects/referalocka`.
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
- 2026-08-24: audited local Codex sessions for `2026-08-23T06:16:29Z ... 2026-08-24T10:24:11+03:00`, added all-chat synthesis session, created the all-chat synthesis playbook, and recorded DSA sales-ops as a non-JJFR signal pending routing decision.
- 2026-09-25: audited local Codex sessions for `2026-09-21T07:38:05.866Z ... 2026-09-25T16:57:00+03:00`; added a compact low-signal all-chat synthesis and recorded the `referalocka` standup workspace symlink issue.
- 2026-09-26: audited local Codex sessions for `2026-09-25T13:55:52.294Z ... 2026-09-26T11:21:00+03:00`; added a session-level synthesis for DSA candidate-panel, Kaplya repository and Codex model-catalog operational facts without changing venture truth.
- 2026-09-29: audited three user-root Codex threads for `2026-09-28T06:08:08.385Z ... 2026-09-29T14:14:00+03:00`; recorded «Связность», a DSA ROP Granola note and the Proteus desktop-vision artifact at session layer without changing venture truth.
- 2026-10-01: audited user-root Codex threads for `2026-09-30T06:01:55.910Z ... 2026-10-01T09:01:00+03:00`; recorded HR Vision's planned first outreach wave, DSA execution/partner artifacts, and the bounded evidence for a business-school proposal without changing venture truth.
- 2026-10-02: audited user-root Codex threads for `2026-10-01T06:01:00.539Z ... 2026-10-02T12:00:00+03:00`; recorded the selected Proteus desktop material, HR Vision's connected agency prototype, DSA price-to-proposal audit and preliminary beta-protection constraints without changing venture truth.
- 2026-10-03: audited user-root Codex threads for `2026-10-02T06:00:28.220Z ... 2026-10-03T09:01:15+03:00`; recorded DSA's verified production refresh and document-layout work, Proteus desktop/core direction, and HR Vision's published jobs/CJM prototype without changing venture truth.
- 2026-10-04: audited user-root Codex threads for `2026-10-03T06:01:14.262Z ... 2026-10-04T09:01:52+03:00`; recorded HR Vision's audience-safe deck and bounded video-demo evidence, Proteus capture reliability diagnostics, and the DSA website/KP Hub source-contract audit without changing venture truth.
- 2026-10-05: audited user-root Codex threads for `2026-10-04T06:01:52.494Z ... 2026-10-05T09:02:06+03:00`; recorded Proteus trigger-block research and local interaction mockups plus HR Vision's evidence-backed assessment-form guidance without changing venture truth.
- 2026-10-06: audited user-root Codex threads for `2026-10-05T06:02:06.043Z ... 2026-10-06T09:01:17+03:00`; recorded verified DSA diagnostic-log cleanup, blocked KP Hub local release findings, TG-conveyor integration gaps, a proposed read-only Proteus inspection bridge and the macOS swap-space root cause without changing venture truth.
- 2026-10-07: audited user-root Codex threads for `2026-10-06T06:01:15.722Z ... 2026-10-07T09:38:57+03:00`; recorded the limited-gate production release of KP Hub/prices, a local DSA Sales build, DSA distributor change, bounded HR Vision interview-workflow artifacts and a temporary thread-vault indexer stop without changing venture truth.
- 2026-10-08: audited user-root Codex threads for `2026-10-07T06:35:48.919Z ... 2026-10-08T09:59:42+03:00`; recorded the configured-but-unmeasured DSA Topvisor SEO/GEO baseline and Proteus memory-reading source package without changing venture truth.
- 2026-10-09: audited completed user-root and automation Codex threads for `2026-10-08T06:10:15.571Z ... 2026-10-09T09:02:17+03:00`; recorded DSA route process/endpoint health with Bitrix workflow still unverified, without changing venture truth.
- 2026-10-10: audited completed user-root and automation Codex threads for `2026-10-09T06:02:17.525Z ... 2026-10-10T09:10:00+03:00`; recorded healthy local YC backup monitoring, a local DSA management-deck artifact, and the HR Vision signal-landscape research package without changing venture truth.

## Smoke / demo checks for next run
- Показать дерево структуры после Milestone 1.
- Показать пример того, какие файлы прочитает LLM при запросе `что мы решили по рефералке`.
- Показать пример того, что обновит команда `обновись`.
- Показать разницу между venture update и system-level update.
