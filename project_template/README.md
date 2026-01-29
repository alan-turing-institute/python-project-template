# {{ project_name }}

[![Actions Status][actions-badge]][actions-link]
{% if pypi == "yes_pypi" -%}
[![PyPI version][pypi-version]][pypi-link]
[![PyPI platforms][pypi-platforms]][pypi-link]
{%- endif %}
{% if codecov -%}
[![Codecov][codecov-badge]][codecov-link]
{%- endif %}
{{ project_short_description }}

## Installation

{% if pypi == "yes_pypi" -%}
```bash
python -m pip install {{ python_name }}
```
{%- endif %}

From source:

```bash
git clone {{ url }}
cd {{ project_name }}
python -m pip install .
```
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
[codecov-badge]:            https://codecov.io/gh/{{org}}/{{project_name}}/branch/main/graph/badge.svg
[codecov-link]:             https://codecov.io/gh/{{org}}/{{project_name}}
<!-- prettier-ignore-end -->
