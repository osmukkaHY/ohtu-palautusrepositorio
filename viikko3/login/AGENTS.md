# Login app

- This directory is a standalone Python/Flask project (Python >=3.14); its dependencies and Robot Framework test dependencies are in `pyproject.toml`. There is no lockfile or configured lint/typecheck command.
- From this directory, install dependencies with `uv sync`. Start the app with `uv run python src/index.py` (serves on port 5001), then run browser tests in another terminal with `uv run robot src/tests/login.robot`.
- Robot tests need the app running at `localhost:5001`; the suite resets its in-memory user repository through `/tests/reset` and creates test users via the registration endpoint. Browser is configured for visible Chromium (`${HEADLESS}` in `src/tests/resource.robot`); if its browser binaries are unavailable, initialize with `uv run rfbrowser init`.
- App entrypoint is `src/index.py`; Flask routes/templates are in `src/app.py` and `src/templates/`. Keep Robot test resources and `AppLibrary.py` paths relative to `src/tests/` as currently referenced.
- App is launched with `uv run flask src/index.py`. 
- User validation happens in src/services/user\_service.py
