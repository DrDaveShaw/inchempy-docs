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
