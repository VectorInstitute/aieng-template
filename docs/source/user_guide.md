(user_guide)=

# User Guide

## pyproject.toml file and dependency management

If your project doesn't have a pyproject.toml file, simply copy the one from the
template and update file according to your project.

For managing dependencies, [Poetry](https://python-poetry.org/) is the recommended tool
for our team. Hence, install Poetry to setup the development virtual environment. Poetry
supports [optional dependency groups](https://python-poetry.org/docs/managing-dependencies/#optional-groups)
which help manage dependencies for different parts of development such as `documentation`,
`testing`, etc. The core dependencies are installed using the command:

```bash
python3 -m poetry install
```

Additional dependency groups can be installed using the `--with` flag. For example:

```bash
python3 -m poetry install --with docs,test
```

## documentation

If your project doesn't have documentation, copy the directory named `docs` to the root
directory of your repository. The provided source files use [Furo](https://pradyunsg.me/furo/),
a clean and customisable Sphinx documentation theme.

In order to build the documentation, install the documentation dependencies as mentioned
in the previous section, navigate to the `docs` folder and run the command:

```bash
make html
```

You can configure the documentation by updating the `docs/source/conf.py`. The markdown
files in `docs/source` can be updated to reflect the project's documentation.
