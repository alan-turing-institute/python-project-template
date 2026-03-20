# Contributing to {{ project_name }}

See the [Scientific Python Developer Guide][spc-dev-intro] for a detailed
description of best practices for developing scientific packages.

[spc-dev-intro]: https://learn.scientific-python.org/development/

## Prerequisites

Install [uv](https://docs.astral.sh/uv/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

```bash
git clone {{ url }}
cd {{ project_name }}
uv sync
```

This installs the package in editable mode along with all dev dependencies, and
creates a `uv.lock` lockfile for reproducible installs.

## Pre-commit

Pre-commit runs the following checks on each commit:

- Code quality checks (trailing whitespace, merge conflicts, large files, etc.)
- Linting and auto-fixing with [ruff](https://docs.astral.sh/ruff/)
- Code formatting with [ruff format](https://docs.astral.sh/ruff/formatter/)

Install the pre-commit hooks so these run automatically on each commit:

```bash
uv run pre-commit install
```

You can also run them manually:

```bash
uv run pre-commit run --all-files
```

## Testing

```bash
uv run pytest
```

With coverage:

```bash
uv run pytest --cov={{ python_name }}
```

## Type checking

```bash
uv run ty check
```

## Building

To verify the package builds correctly:

```bash
uv build
```

## Adding dependencies

- Runtime: `uv add <package>`
- Dev: `uv add --group dev <package>`
- Test: `uv add --group test <package>`
- Lint: `uv add --group lint <package>`

## About `uv.lock`

The `uv.lock` file is committed to the repository to ensure reproducible
installs. CI uses `uv sync --locked` to verify the lockfile is up to date. If
you change dependencies, run `uv lock` to update it.
