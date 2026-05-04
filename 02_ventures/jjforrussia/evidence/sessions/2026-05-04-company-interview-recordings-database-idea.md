---
title: Company Interview Recordings Database Idea
type: evidence-session
venture: jjforrussia
status: active
date: 2026-05-04
source: conversation
---

# Summary

Никита добавил новую интересную идею для `jjforrussia`: сейчас, вероятно, большое количество компаний записывает интервью кандидатов, которые проходят через их hiring funnel. Эти записи потенциально можно использовать, чтобы выстраивать отдельную базу данных под каждую компанию.

Идея пока не считается подтверждённой рыночной truth. Это рабочая гипотеза, которую нужно проверять через employer discovery и юридико-операционные ограничения.

# Raw idea, normalized

Многие компании могут уже иметь записи candidate interviews. Если компания готова дать легальный и операционно удобный доступ к этим материалам, JJFR может превращать интервью-записи в company-specific hiring memory:
- какие роли компания реально нанимает;
- какие вопросы задают интервьюеры;
- какие признаки кандидата считаются сильными;
- какие риски повторяются;
- почему кандидаты проходят или не проходят дальше;
- как выглядит фактический hiring bar конкретной команды.

# Product interpretation

Это может стать employer-side data layer поверх текущей механики `матрица роли × матрица кандидата`.

Вместо того чтобы строить матрицу роли только из описания вакансии и разговора с hiring manager'ом, можно использовать исторические интервью компании как evidence:
- extract skills and indicators;
- detect interviewer probing patterns;
- infer company-specific decision criteria;
- map candidate answers to accepted / rejected patterns;
- build a reusable company-specific evidence database.

# Why it matters

Потенциальная ценность:
- более точная матрица роли и hiring bar;
- меньше зависимости от формального job description;
- возможность объяснять работодателю, почему кандидат похож или не похож на тех, кто раньше проходил;
- база для future shortlist quality и company-specific candidate evidence pack;
- более сильный employer-side moat, если данные доступны регулярно.

# Key risks

- `Data access`: неясно, сколько компаний реально записывают интервью и готовы делиться ими.
- `Consent / personal data`: интервью-записи содержат персональные данные кандидатов и требуют явного правового режима.
- `Outcome labels`: без информации о результате интервью база будет гораздо слабее.
- `Enterprise friction`: сбор и обработка исторических интервью может оказаться слишком тяжёлым шагом для первой сделки.
- `Trust`: работодателю нужно понимать, что система не "судит" кандидата автоматически, а структурирует evidence для человека.

# Validation questions

- У каких target-компаний interview recording уже является нормальной практикой?
- В каких инструментах хранятся записи: Zoom, Teams, Google Meet, ATS, internal storage?
- Можно ли получить consent-based доступ к 10-20 интервью и outcome labels?
- Достаточно ли такого объёма, чтобы построить useful company-specific role / hiring matrix?
- Что работодатель ценит больше: быстрое закрытие роли или накопление company-specific hiring intelligence?
- Можно ли предложить это как lightweight add-on к discovery / role intake, а не как отдельный тяжёлый внедренческий продукт?

# Links

- [Hypotheses](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/working/hypotheses.md)
- [Skill-based matching mechanism session](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/evidence/sessions/2026-04-25-skill-based-matching-mechanism.md)
- [Skill-based matching mechanism artifact](/Users/NIKITA/.codex/context/Context/02_ventures/jjforrussia/artifacts/skill-based-matching-mechanism-v0.md)
