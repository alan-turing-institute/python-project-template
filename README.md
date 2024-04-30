# Template for Python projects

For enhancing your current/next Python project with
- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata
- Linting + formatting via `ruff` and `pre-commit`
- `pytest` set up to run automatically on your commits through GitHub Actions
- Semi-automated releases to PyPI via GitHub tags + GitHub Actions (you just need to make a new tag on GitHub!)
- Opt-in typing support via `mypy`

Based on the [Scientific Python project template](https://github.com/scientific-python/cookie).

## Setting up a new project

To use, install `copier` in your Python environment:

```
python -m pip install copier
```

Then, run the following command to start the template configuration:

```
copier copy gh:alan-turing-institute/python-project-template my-package-name
```

The output will be created in a folder called `my-package-name`, and will be created if it doesn't exist.

You will be prompted for the following information:

- `project_name`: The name of your project. This will be used to name the
  project directory, the Python package, and the GitHub repository.
- `project_short_description`: A short description of your project.
- `backend`: The backend to use for dependency management. Here, I've supported the main choices in REG (`setuptools`/`poetry`), as well as `hatch`, which I've been using more recently.
  - [`setuptools`](https://setuptools.readthedocs.io/en/latest/): The default Python packaging tool, configured with `pyproject.toml`.
  - [`hatch`](https://hatch.pypa.io/latest/): Almost identical to `setuptools` in terms of config, but with a few extra features.
  - [`poetry`](https://python-poetry.org/): An all-in-one tool for dependency management, packaging, and publishing, with a high learning curve. Use if you know what you're doing -- otherwise, I'd stick with `setuptools` or `hatch`.
- `license`: The license to use for your project — PRs for other choices are welcome! The current supported options include:
  - `MIT`
  - `BSD-3-Clause`
  - `Apache-2.0`
  - `GPL-3.0`
- `python_name`: The name of your project when you do `import name` (and potentially `pip install name`). This should be a valid Python package name (use underscores instead of hyphens, for example).
- `typing`: Whether to use `mypy` for type checking. If you're not sure, I'd recommend basic checks (second option).
- `python_version_range`: The range of Python versions to support. This will be used to set the `python_requires` field in `pyproject.toml`. Defaults to `>=3.8`.

Once you've answered all the questions, Copier will generate a new project in the directory you specified. If you're migrating existing code, you should move all your code into the `src/{{ python_name }}` directory, and delete the `template` directory.


## Inspiration

This template heavily draws upon the [Scientific Python template](https://github.com/scientific-python/cookie) to motivate choices for default options for linters, backends etc. If you haven't worked with any of the tools in this repo (e.g. pre-commit, ruff, mypy, pytest) or want to know more about Python project setup in general, then you'll benefit from reading the fantastic [Scientific Python Development Guidelines](https://learn.scientific-python.org/development/).

It's worth noting that the original template also has support for many more backends, including the use of compiled extensions (e.g. in Rust or C++). The only reason this is not a fork is that I wanted to both simplify the options available, and make the hard switch to [copier](https://copier.readthedocs.io/en/stable/) instead of [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) as a templating engine, since it lets you [natively update your project in-place to the latest template](https://copier.readthedocs.io/en/stable/updating/), even after you've worked on it for a while.
