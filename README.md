# Template for Python projects

For enhancing your current/next Python project with

- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata
- Linting + formatting via `ruff` and `pre-commit`
- `pytest` set up to run automatically on your commits through GitHub Actions
- Semi-automated releases to PyPI via GitHub tags + GitHub Actions (you just need to make a new tag on GitHub!)
- Opt-in typing support via `mypy`

Based on the [Scientific Python project template](https://github.com/scientific-python/cookie).

## Sections in this README

- [Setting up a new project](#setting-up-a-new-project)
- [Using your new project](#using-your-new-project)
- [Migrating an existing project](#migrating-an-existing-project)
- [Inspiration](#inspiration)

## Setting up a new project

To use, install `copier` in your Python environment:

```
python -m pip install copier
```

Then, run the following command to start the template configuration (but replace `my-package-name` with the name of your package):

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
- `python_version_range`: The range of Python versions to support. This will be used to set the `python_requires` field in `pyproject.toml`. Defaults to `>=3.10`.

Great! Copier will have now created a new project in the directory you specified by replacing `my-package-name`, and customized it based on the information you provided.

### Migrating an existing project

If you're taking code you've already written and want to use this template, you'll need to perform the following steps:

- Start by moving your library code into the `src/{{ python_name }}` directory.
  - By library code, I mean the code that you want to be importable by other Python code. If you have things like experiments, scripts, or notebooks, you should keep them in the root directory under a different name (e.g. `examples`, `notebooks` etc.)
- Copy over any tests you have into the `tests` directory.
- Go through the `pyproject.toml` file and make sure that the metadata is correct. This includes the `name`, `description`, `version`, `authors`, `license`, and `classifiers` fields.
- Add your dependencies to the relevant section of the `pyproject.toml` file.
  - If you're using `setuptools` or `hatch`, you'll need to add them to the `install_requires` field. Dependencies are formatted like this:
    ```
    [project]
    install_requires = [
        "numpy >= 1.20",
        "pandas == 1.2.3",
        "scipy",
    ]
    ```
    where the first part is the package name, and the second part is the version specifier. You can find more information on version specifiers [here](https://www.python.org/dev/peps/pep-0440/#version-specifiers) to help you write these.
  - If you're using `poetry`, you'll need to add them to the `dependencies` field under the `tool.poetry` section.

## Using your new project

Once you've set up your new project, you can start developing your package. There are some guidelines for development included in the [`CONTRIBUTING.md`](project_template/CONTRIBUTING.md) file generated in your project, but the main things are repeated here for completeness.

### Python environment

Every project should have a Python environment set up to manage dependencies. `poetry` has its own virtual environment management, but if you're using `setuptools` or `hatch`, you can use `venv` to create a new environment (called .venv by default) in the root of your project. To do this, run the following command in your terminal from the root of your project:

```
python -m venv .venv
```

Then, activate the environment:

- On Windows:

  ```
  .venv\Scripts\activate
  ```

- On Unix or MacOS:
  ```
  source .venv/bin/activate
  ```

I would also recommend upgrading `pip` and `setuptools` in your environment to the latest versions:

```
pip install --upgrade pip setuptools
```

There's also the environment manager [`uv`](https://astral.sh/uv), which has gained a lot of traction through being really fast, including some fun extras (e.g. [this one](https://twitter.com/HenrySchreiner3/status/1788801151686631584) that could save your old projects that no longer work with newer package versions).

The workflow for this template will look something like this:

- Make changes to your code in the `src/{{ python_name }}` directory.

## Inspiration

This template heavily draws upon the [Scientific Python template](https://github.com/scientific-python/cookie) to motivate choices for default options for linters, backends etc. If you haven't worked with any of the tools in this repo (e.g. pre-commit, ruff, mypy, pytest) or want to know more about Python project setup in general, then you'll benefit from reading the fantastic [Scientific Python Development Guidelines](https://learn.scientific-python.org/development/).

It's worth noting that the original template also has support for many more backends, including the use of compiled extensions (e.g. in Rust or C++). The only reason this is not a fork is that I wanted to both simplify the options available, and make the hard switch to [copier](https://copier.readthedocs.io/en/stable/) instead of [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) as a templating engine, since it lets you [natively update your project in-place to the latest template](https://copier.readthedocs.io/en/stable/updating/), even after you've worked on it for a while.
