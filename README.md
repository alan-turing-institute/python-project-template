# Python Project Template

A uv-native, opinionated template for Python projects at the Alan Turing Institute.

## Features

- **uv-native workflow** — `uv sync`, `uv run`, `uv build` everywhere
- **uv_build backend** — modern PEP 517 build backend from Astral
- **PEP 735 dependency groups** — composable dev, test, lint, and docs groups
- **ty type checking** — fast type checking via `uvx ty check`
- **ruff** — linting and formatting in one tool
- **pre-commit** — with Astral's official hooks and `uv-lock`
- **GitHub Actions CI** — parallel lint, typecheck, and test jobs
- **MkDocs Material** — optional documentation scaffolding
- **QoL files** — EditorConfig, Dependabot, issue/PR templates

Based on the [Scientific Python project template](https://github.com/scientific-python/cookie).

## Quick start

Install [copier](https://copier.readthedocs.io/) and [uv](https://docs.astral.sh/uv/):

```bash
pip install copier
```

Create a new project:

```bash
copier copy gh:alan-turing-institute/python-project-template my-package
```

You will be prompted for:

| Variable | Description | Default |
|---|---|---|
| `project_name` | Project name | (required) |
| `project_short_description` | One-line description | "A Python project" |
| `python_name` | Python import name | derived from project_name |
| `full_name` | Author name | (required) |
| `email` | Author email | (required) |
| `license` | MIT, BSD-3-Clause, Apache-2.0, GPL-3.0-or-later | MIT |
| `min_python_version` | 3.11, 3.12, or 3.13 | 3.11 |
| `include_docs` | Include MkDocs Material scaffolding | true |
| `org` | GitHub org or username | alan-turing-institute |

After generation, the template automatically runs `git init`, `uv sync`, and
`uv run pre-commit install`.

## Generated project structure

```
my-package/
├── .editorconfig
├── .github/
│   ├── dependabot.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── pull_request_template.md
│   └── workflows/
│       ├── cd.yml
│       └── ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs/              (if include_docs)
│   ├── index.md
│   └── reference.md
├── mkdocs.yml         (if include_docs)
├── pyproject.toml
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── py.typed
└── uv.lock
```

## Development workflow

```bash
uv sync                    # install all dev dependencies
uv run pytest              # run tests
uv run ruff check .        # lint
uv run ruff format .       # format
uvx ty check               # type check
uv run pre-commit run -a   # run all pre-commit hooks
```

## Updating an existing project

```bash
copier update
```

## Publishing to PyPI

Create a release on GitHub — the CD workflow will build and publish to PyPI
using trusted publishing. See the generated `CONTRIBUTING.md` for details.
