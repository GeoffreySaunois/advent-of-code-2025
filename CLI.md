This is my advent of code project!

I'm using uv, a .venv is already setup.

CLI usage (Typer):
- `uv run setup --day X` scaffolds `DayXX/` (zero-padded) at repo root
- Inside it creates `dayXX.py` from `template.py` and an empty `test`
- Runs `aoc download` in `DayXX/` to fetch input (`input`) and puzzle text (`puzzle.md`)
- Idempotent: if `DayXX` already exists, it exits without changes
- Requires `aoc` on PATH and configured; Typer is already a dependency
