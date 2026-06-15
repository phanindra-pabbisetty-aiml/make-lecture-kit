# Changelog

All notable changes to **make-lecture-kit**. This kit is built to keep improving:
every upgrade bumps `VERSION`, adds an entry here, and must pass
`python3 scripts/selfcheck.py`. See `references/upgrading.md` for the loop.

Format follows *Keep a Changelog*; versions follow semantic versioning.

## [2.0.0] — 2026-06-15

### Fixed
- **Worked-example "Step N." labels no longer spill outside the callout box.** A
  dedicated `steps` list reserves enough label width; the old raw `enumerate`
  overflowed its label past the frame. The linter now hard-fails the old pattern.
- **Cross-platform compile.** `bbding` is now optional (falls back to pifont
  `\ding{43}/{46}`), so the PDF builds on minimal TeX installs. And `build_pdf.py`
  no longer passes `latexmk` an option it rejects — that bug silently produced no
  PDF whenever latexmk was the chosen engine.

### Added
- **`references/plain_language.md`** — one shared rulebook for easy English
  (sentence ceiling, plain-word swaps, banned hand-waving, reading-level target),
  enforced by both linters.
- **`scripts/lint_tex.py`** — a language + layout gate for the companion PDF (which
  had none); wired into `build_pdf.py`.
- **Rich figure helpers in `figstyle.py`** — `contour`, `surface3d`,
  `function_plot` (+ tangent), `gradient_descent`, `vectors2d`, `heatmap`, `flow`,
  `annotated_sequence`, `bars`, plus a house colormap.
- **A "when to draw a plot" criterion + concept→plot map** (`companion_style.md`
  §5) and a **figure-coverage** check in `lint_tex.py`.
- **Glossary + symbol cheat-sheet** as a standard closing section (`companion_style`
  §8 + template).
- **Interactive HTML "signature" layer** (`lecture_style.md` §12): per-band recall
  checks, copy buttons, an end-of-lecture synthesis interactive.
- **`scripts/selfcheck.py`**, **`references/upgrading.md`**, **`VERSION`**, and this
  changelog — a safe, repeatable way to keep upgrading the kit.

### Changed
- **`scripts/lint.py`** tightened: 22-word sentence ceiling, shared word lists,
  reading-level estimate.
- **Platform-agnostic** wording and packaging throughout (Claude Code, Claude
  Cowork, OpenAI Codex, Google Jules, Cursor, or any agentic coding assistant).

## [1.0.0]

- Initial kit: companion PDF + complete interactive HTML lecture, five colour-coded
  callout boxes, the quality rubric, `figstyle.py`, `build_pdf.py`, and `lint.py`.
