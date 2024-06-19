# {{ project_name }}

[![Actions Status][actions-badge]][actions-link]
[![PyPI version][pypi-version]][pypi-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

{{ project_short_description }}

## Installation

```bash
python -m pip install {{ python_name }}
```

From source:
{% if backend == "poetry" -%}
```bash
git clone {{ url }}
cd {{ project_name }}
poetry install
```
{% else -%}
```bash
git clone {{ url }}
cd {{ project_name }}
python -m pip install .
```
{%- endif %}

## Usage


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to contribute.

## License

Distributed under the terms of the [{{ license }} license](LICENSE).


<!-- prettier-ignore-start -->
[actions-badge]:            {{url}}/workflows/CI/badge.svg
[actions-link]:             {{url}}/actions
[pypi-link]:                https://pypi.org/project/{{project_name}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{project_name}}
[pypi-version]:             https://img.shields.io/pypi/v/{{project_name}}
<!-- prettier-ignore-end -->
