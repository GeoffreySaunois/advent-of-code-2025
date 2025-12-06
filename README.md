# Advent of Code 2025 🎄💫

This is my advent of code project!

## CLI commands

```bash
uv run setup --day X
```

- Creates `DayXX/` directory for day X
- Inside it creates `dayXX.py` from `template.py` and an empty `test`
- Runs `aoc download` in `DayXX/` to download input and puzzle text (see [aoc-cli](https://github.com/scarvalhojr/aoc-cli))
- Idempotent: if `DayXX` already exists, it exits without changes

## Requirements:

- `aoc` tool already installed and added to PATH (see [aoc-cli](https://github.com/scarvalhojr/aoc-cli))
