# Template for Python projects

This simple template is designed to help you get started with a new Python project. It includes:

- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata
- Linting + formatting via `ruff` and `pre-commit`
- `pytest` set up to run automatically on your commits through GitHub Actions
- Semi-automated releases to PyPI via GitHub tags + GitHub Actions
- Opt-in typing support via `mypy`

Based on the [Scientific Python project template](https://github.com/scientific-python/cookie).

## Sections in this README

- [Setting up a new project](#setting-up-a-new-project)
- [Using your new project](#using-your-new-project)
- [Migrating an existing project](#migrating-an-existing-project)
- [Python environment management](#python-environment-management)
- [Installing your package in editable mode](#installing-your-package-in-editable-mode)
- [Wrtiting code and running tests](#writing-code-and-running-tests)
- [Formatting and checking your code](#formatting-and-checking-your-code)
- [Publishing your package](#publishing-your-package)
- [Updating your project when the template changes](#updating-your-project-when-the-template-changes)
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
- `backend`: The backend to use for dependency management. Here, I've supported the main choices in our Research Engineering Group (`setuptools`/`poetry`), as well as `hatch`, which I've been using more recently.
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

Your new project will have been set up with the following structure:

```
my-package-name/
├── .github/
│   └── workflows/
│       └── ci.yml
│      └── cd.yml
├── .gitignore
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── my_package_name/
│       └── __init__.py
└── tests/
    └── __init__.py
```

Here's a brief overview of the files and directories that have been created:

- `.github/workflows/ci.yml`: A GitHub Actions workflow that runs your tests on every push to the repository.
- `.github/workflows/cd.yml`: A GitHub Actions workflow that publishes your package to PyPI on every new version tag made through the GitHub interface.
- `.gitignore`: A file that tells Git which files to ignore when committing changes.
- `.pre-commit-config.yaml`: A configuration file for the `pre-commit` tool, which runs code checks and formatting on every commit.
- `CONTRIBUTING.md`: A guide for people who want to contribute to your project, which has a lot of the same advice as this README.
- `CODE_OF_CONDUCT.md`: A code of conduct for your project, which sets out the standards of behaviour you expect from contributors. You will likely need to edit or extend this to suit your project.
- `LICENSE`: A copy of the license you chose for your project.
- `README.md`: An overview of your project, which comes with some badges (example: ![Badge](https://img.shields.io/badge/this_is-a_badge-blue)) for things like CI status, code coverage, and PyPI version.
- `pyproject.toml`: A TOML file that contains metadata about your project, including its name, version, description, and dependencies.
- `src/`: A directory that contains your Python package code.
- `tests/`: A directory that contains your tests.

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

Once you've set up your new project, you can start developing your package. There are some guidelines for development included in the [`CONTRIBUTING.md`](project_template/CONTRIBUTING.md) file generated in your project, but the main things are repeated below.


## Python environment management

_Note: I will not be covering Conda environments in this section. Conda is great when your project has dependencies outside of Python packages that you want to manage! If you're using Conda, you can still use this template – these are just recommendations for managing Python environments that don't affect the package itself._

Every project should have a Python environment set up to manage dependencies. `poetry` has its own virtual environment management (if you're not familiar with it, maybe don't use poetry!), but if you're using `setuptools` or `hatch`, you can use `venv` to create a new environment in the root of your project. To create an environment called `.venv`, run the following command in your terminal:

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

Your version of python should now point to the one in the `.venv` directory. You can check this by running: `which python`, which should return a path to the python executable in the `.venv` directory (e.g. `my-package-name/.venv/bin/python`).

Before installing your package to work on, I would also recommend upgrading `pip` and `setuptools` in your environment to the latest versions, which could potentially avoid issues with installing dependencies later on. You can do this by running the following command in your terminal while the environment is activated:

```
pip install --upgrade pip setuptools
```


### Aside: Using `uv` for environment management

There's also the environment manager [`uv`](https://astral.sh/uv), which has gained a lot of traction through being really fast, including some fun extras (e.g. [this one](https://twitter.com/HenrySchreiner3/status/1788801151686631584) that could save your old projects that no longer work with newer package versions).

To install `uv`, [follow the install instructions on the GitHub page](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started), then run the following command in your terminal from the root of your project:

```bash
uv venv --seed
```

This will create a new virtual environment in the `.venv` directory, with the `--seed` option upgrading `pip` and `setuptools` to the latest versions automatically.

Activating the environment is the same as with `venv`:

- On Windows:

  ```bash
  .venv\Scripts\activate
  ```

- On Unix or MacOS:
  ```bash
  source .venv/bin/activate
  ```

Then, to benefit from `uv`'s speed, you install your dependencies with:

```bash
uv pip install ...  # as you would with pip!
```

## Installing your package in editable mode

After your environment is set up, you can then install your project in editable mode (so that changes you make to the code are reflected in the installed package) by running:

```bash
pip install -e .  # or uv pip install -e . if you're using uv
```

This will install your package in editable mode, so you can import it in other Python code through `import my_package_name` and access methods as if it were any other package. The editable part means that if you make changes to the code in the `src` directory, they will be reflected in the installed package, so your changes will be immediately available to any code that uses your package that you're working on.

## Wrtiting code and running tests

You're now ready to start developing your package! Add code to the `src` directory, tests to the `tests` directory, and run your tests with the  `pytest` command to make sure everything is working as expected. Settings for `pytest` are included in the `pyproject.toml` file.

Additionally, the automated CI pipeline will run the tests for you, but it's a good idea to run them locally as well to catch any issues before you push your code.

## Formatting and checking your code

The tools for formatting and linting your code for errors are all bundled with [pre-commit](https://pre-commit.com/). Included are:
- [ruff](https://astral.sh/ruff) (linting + formatting)
- [mypy](https://mypy.readthedocs.io/en/stable/) (static type checking)
- various other small fixes and checks (see the [`.pre-commit-config.yaml`](project_template/.pre-commit-config.yaml) file for more information)

To have pre-commit check your files before you commit them, you can run the following command:

```bash
pre-commit install
```

This will set up pre-commit to run the checks automatically on your files before you commit them. It's possible that pre-commit will make changes to your files when it runs the checks, so you should add those changes to your commit before you commit your code. A typical workflow would look like this:

```bash
git add -u
git commit -m "My commit message"
# pre-commit will run the checks here; if it makes changes, you'll need to add them to your commit
git add -u
git commit -m "My commit message"
# changes should have all been made by now and the commit should pass if there are no other issues
# if your commit fails again here, you have to fix the issues manually (not everything can be fixed automatically).
```

One thing that is worth knowing is how to lint your files outside of the context of a commit. You can run the checks manually by running the following command:

```bash
pre-commit run --all-files
```

This will run the checks on all files in your git project, regardless of whether they're staged for commit or not.

## Publishing your package

If you're ready to publish your package to [PyPI](https://pypi.org/) (i.e. you want to be able to run `pip install my-package-name` from anywhere), the template includes a GitHub Actions workflow that will automatically publish your package to PyPI when you create a new release on GitHub. The workflow is defined in the [`.github/workflows/cd.yml`](project_template/.github/workflows/cd.yml) file within the `project_template` folder.

First, if you don't already have a PyPI account, we'll follow these first steps from the [python packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives):

>The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation. It’s great for things like this tutorial where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details, see Using TestPyPI.

Notice how the instructions mention TestPyPI, which is a testing environment for PyPI. This is a good place to start, since you can test publishing your package without affecting the real PyPI index. Once you're ready to publish to the real PyPI, you can follow the same steps again — just replace `https://test.pypi.org` with `https://pypi.org`.

We'll then need to set up trusted publishing, which allows us to publish to PyPI without the need for a username/password or API token. This template uses the [PyPA GitHub action for publishing to PyPI](https://github.com/pypa/gh-action-pypi-publish/tree/release/v1.9?tab=readme-ov-file), which gives us the following instructions:

> This action supports PyPI's [trusted publishing](https://docs.pypi.org/trusted-publishers/) implementation, which allows authentication to PyPI without a manually configured API token or username/password combination. To perform trusted publishing with this action, your project's publisher must already be [configured on PyPI](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

After following these steps, we're basically there! You can now create a new release on GitHub using the "Releases" tab on the right-hand side, and the GitHub Actions workflow will automatically publish your package to PyPI using the commit associated with the release. **Note: you'll need to update the version number in the `pyproject.toml` file before creating a new release, since PyPI won't allow you to publish the same version twice!**

Make sure to follow [semantic versioning](https://semver.org/) when updating the version number. If it's your first version of the package, I'd recommend starting at 0.1.0, with the major release 1.0.0 being the production-ready product. Use minor versions (0.X.0) for breaking changes, and patch versions (0.0.X) for backwards-compatible bug fixes.

If this was your first time publishing, you will then  be able to install your package from PyPI with `pip install my-package-name`. Yay!

## Updating your project when the template changes

Copier has [instructions on how to update a template to the latest version](https://copier.readthedocs.io/en/stable/updating/), which I'll repeat here for completeness.

If you want to update your project with the latest version of this template, you can run the following command (ensuring that your current project is committed and that you have no uncommitted changes, since the update will overwrite some files!):

```bash
copier update
```

Note that this is the purpose of the `.copier-answers.yml` file in the root of your project. This file is used by Copier to keep track of the answers you gave when you first created the project, allowing it to update the project correctly when you run `copier update`.


## Inspiration

This template heavily draws upon the [Scientific Python template](https://github.com/scientific-python/cookie) to motivate choices for default options for linters, backends etc. If you haven't worked with any of the tools in this repo (e.g. pre-commit, ruff, mypy, pytest) or want to know more about Python project setup in general, then you'll benefit from reading the fantastic [Scientific Python Development Guidelines](https://learn.scientific-python.org/development/).

It's worth noting that the original template also has support for many more backends, including the use of compiled extensions (e.g. in Rust or C++). The only reason this is not a fork is that I wanted to both simplify the options available, and make the hard switch to [copier](https://copier.readthedocs.io/en/stable/) instead of [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) as a templating engine, since it lets you [natively update your project in-place to the latest template](https://copier.readthedocs.io/en/stable/updating/), even after you've worked on it for a while.
