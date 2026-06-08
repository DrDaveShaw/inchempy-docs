INCHEM-Py Documentation
=======================

This repository contains the Read the Docs documentation for INCHEM-Py v1.2.1.

Building locally
----------------

Install dependencies::

    pip install sphinx sphinx-rtd-theme

Build the docs::

    sphinx-build -b html docs docs/_build/html

Then open ``docs/_build/html/index.html`` in your browser.

Hosting on Read the Docs
------------------------

1. Push this repository to GitHub
2. Sign up at https://app.readthedocs.org
3. Click "Import a Project" and select this repository
4. Read the Docs will auto-detect ``.readthedocs.yaml`` and build automatically
