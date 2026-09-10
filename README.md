# INCHEM-Py documentation

Source for the [INCHEM-Py](https://github.com/DrDaveShaw/INCHEM-Py)
documentation, built with [Sphinx](https://www.sphinx-doc.org/) and hosted on
[Read the Docs](https://readthedocs.org/). This set documents **version 1.3**.

## Layout

```
.
├── .readthedocs.yaml        # Read the Docs build configuration
└── docs/
    ├── requirements.txt     # build dependencies
    └── source/
        ├── conf.py          # Sphinx configuration
        ├── index.rst        # landing page / table of contents
        ├── *.rst            # documentation pages
        └── _static/images/  # figures and logo
```

## Building locally

```bash
pip install -r docs/requirements.txt
sphinx-build -b html docs/source docs/_build/html
```

Then open `docs/_build/html/index.html` in a browser.

To build the PDF (requires a LaTeX toolchain):

```bash
sphinx-build -b latex docs/source docs/_build/latex
make -C docs/_build/latex
```

## Hosting on Read the Docs

1. Push this directory to a GitHub repository (it can live in the main
   INCHEM-Py repo, e.g. under `docs/`, or in a separate repo).
2. Import the repository at https://readthedocs.org/.
3. Read the Docs picks up `.readthedocs.yaml` automatically and builds on
   every push. No further configuration is needed.

If the docs live inside the main INCHEM-Py repository rather than at the repo
root, move `.readthedocs.yaml` to that repo's root and adjust the
`sphinx.configuration` path accordingly.

## Editing

Each page is a reStructuredText (`.rst`) file under `docs/source/`. Markdown
(`.md`) is also enabled via MyST if you prefer it for new pages. The
navigation is controlled by the `toctree` directives in `index.rst`.

Changes specific to version 1.3 are collected in `whats_new.rst` and flagged
inline throughout with `.. versionadded:: 1.3` / `.. versionchanged:: 1.3`
directives.
