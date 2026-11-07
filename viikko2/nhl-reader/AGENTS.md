# Agent notes

- Use Python 3.14 (`.python-version`); dependencies are managed with `uv` and pinned in `uv.lock`. Set up with `uv sync`.
- Run the CLI from the repository root with `uv run python src/main.py`. It fetches live NHL statistics from `studies.cs.helsinki.fi`, so execution needs network access.
- `src/player.py` contains the API reader, player model, and statistics; `src/main.py` is the interactive Rich CLI entry point.
- Run tests offline with `uv run pytest`; tests live in `src/tests` and use a dummy `PlayerReader` so they never hit the NHL API.
- Lint with `uv run pylint src`; `.pylintrc` sets a 120-character line limit and ignores `src/tests`.
