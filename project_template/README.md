# {{ project_name }}

[![CI]({{ url }}/actions/workflows/ci.yml/badge.svg)]({{ url }}/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/{{ project_name }})](https://pypi.org/project/{{ project_name }}/)
[![Python versions](https://img.shields.io/pypi/pyversions/{{ project_name }})](https://pypi.org/project/{{ project_name }}/)
{%- if license == "MIT" %}
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
{%- elif license == "BSD" %}
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](LICENSE)
{%- elif license == "Apache" %}
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
{%- elif license == "GPL" %}
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
{%- endif %}

{{ project_short_description }}

## Installation

```bash
pip install {{ project_name }}
```

## Quickstart

<!-- TODO: Add a usage example for your project. -->

```python
import {{ python_name }}
```

## Development

```bash
git clone {{ url }}
cd {{ project_name }}
uv sync
```

```bash
uv run pytest              # run tests
uv run ruff check .        # lint
uv run ruff format .       # format
uvx ty check               # type check
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full development instructions.

## License

Distributed under the terms of the [{{ license }} license](LICENSE).
