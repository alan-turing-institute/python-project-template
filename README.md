# Template for Python projects

To use, install `copier` in your Python environment:

```
pip install copier
```

Then, run the following command to start the template configuration:

```
copier copy gh:phinate/python-template-REG /path/to/your/project
```

You will be prompted for the following information:

- `project_name`: The name of your project. This will be used to name the
  project directory, the Python package, and the GitHub repository.
- `project_short_description`: A short description of your project.
- `pip_name`: The name of your project on PyPI. This should be a valid Python
  package name.
- `backend`: The backend to use for dependency management. Here, I've supported the main choices in REG (`setuptools`/`poetry`), as well as `hatch`, which I've been using more recently.
  - [`setuptools`](https://setuptools.readthedocs.io/en/latest/): The default Python packaging tool, configured with `pyproject.toml`.
  - [`hatch`](https://hatch.pypa.io/latest/): An alternative to `setuptools` that's gaining traction in my circles. Almost identical to `setuptools` in terms of config, but with a few extra features.
  - [`poetry`](https://python-poetry.org/): An all-in-one tool for dependency management, packaging, and publishing, with a high learning curve. Use if you know what you're doing -- otherwise, I'd stick with `setuptools` or `hatch`.
- `license`: The license to use for your project -- PRs for other choices are welcome! The current supported options include:
  - `MIT`
  - `BSD-3-Clause`
  - `Apache-2.0`
  - `GPL-3.0`
- `pip_name`: The name of your project when you do `import name` or `pip install name`. This should be a valid Python package name (use underscores instead of hyphens, for example).

Once you've answered all the questions, Copier will generate a new project in the directory you specified. If you're migrating existing code, you should move all your code into the `{{ pip_name }}` directory, and delete the `template` directory.