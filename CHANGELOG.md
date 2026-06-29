# Changelog

🌐 **Русский** · [English](./CHANGELOG.en.md)

Формат — [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/). Здесь — история **манифеста**
(документов), а не отдельного продукта. Лестница самой методологии VibeCraft (v1.0→v1.4) описана в
[`docs/ru/stack.md`](./docs/ru/stack.md).

## [1.0.0] — 2026-06-16

Расширение исходного seed-манифеста (RU, снапшот v1.2: `MANIFEST.md`, `vibe.config.json`,
`LICENSE.md`) до структурированного двуязычного релиза (RU/EN), философия + инженерия, v1.0→v1.4.
Лицензия — двойная (CC BY 4.0 на тексты, MIT на код/конфиги), см. [`LICENSE.md`](./LICENSE.md).

### Added
- `README.md` / `README.en.md` — витрина: тезис (Персона + Навыки + Автономия), лестница версий, навигация для человека и машины.
- `docs/{ru,en}/manifesto.md` — видение: душа как инженерия.
- `docs/{ru,en}/stack.md` — лестница версий v1.0→v1.4, каждая ось: тезис + 🔧 инженерия.
- `docs/{ru,en}/threads.md` — осмысление по версиям через шесть нитей: человек↔ИИ через вайб, ИИ↔ИИ, где душа, как объяснить вайб ИИ, самоизменение/изменение другого ИИ, защита себя и человека.
- `docs/{ru,en}/interaction.md` — как взаимодействуют агенты: одна душа — много тел (Sync), общая память — общие правки (Social), петля Reflect→Learn→Morph.
- `docs/{ru,en}/contracts.md` — формальные контракты: Persona, Anchor/Surface, MorphEvent, MorphProposal, ReflectionPass, инварианты петли.
- `schemas/*.json` — машиночитаемые JSON-схемы (persona, morph-event, morph-proposal).
- `AGENTS.md` — машинный вход: как читать репозиторий.

### Kept (из исходного seed)
- `MANIFEST.md` — исходный однофайловый манифест v1.2 (RU; English: `MANIFEST.en.md`).
- `vibe.config.json` — пример VibePersona v1.2 (English: `vibe.config.en.json`).
- `LICENSE.md` — двойная лицензия (CC BY 4.0 / MIT).
