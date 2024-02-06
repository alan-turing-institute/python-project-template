See the [Scientific Python Developer Guide][spc-dev-intro] for a detailed
description of best practices for developing scientific packages.

[spc-dev-intro]: https://scientific-python-cookie.readthedocs.io/guide/intro

# Setting up a development environment manually

You can set up a development environment by running:

{%- if backend == "poetry" %}
```zsh
poetry install
```
{%- else %}

```zsh
python3 -m venv venv          # create a virtualenv called venv
source ./venv/bin/activate   # now `python` points to the virtualenv python
pip install -v -e ".[dev]"    # -v for verbose, -e for editable, [dev] for dev dependencies
```
{%- endif %}

# Post setup

You should prepare pre-commit, which will help you by checking that commits pass
required checks:

```bash
pip install pre-commit # or brew install pre-commit on macOS
pre-commit install # this will install a pre-commit hook into the git repo
```

You can also/alternatively run `pre-commit run` (changes only) or
`pre-commit run --all-files` to check even without installing the hook.

# Testing

Use pytest to run the unit checks:

```bash
pytest
```

# Coverage

Use pytest-cov to generate coverage reports:

```bash
pytest --cov={{ python_name }}
```

# Pre-commit

This project uses pre-commit for all style checking. Install pre-commit and run:

```bash
pre-commit run -a
```

to check all files.
