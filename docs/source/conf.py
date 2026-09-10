# Configuration file for the Sphinx documentation builder.
#
# For a full list of options see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "INCHEM-Py"
copyright = "2019-2024, David Shaw and Nicola Carslaw"
author = "David Shaw and Nicola Carslaw"

# The version documented by this build.
version = "1.3"
release = "1.3"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.mathjax",       # render the model equations
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",        # copy button on code blocks
    "myst_parser",              # allow Markdown alongside reStructuredText
]

# Give autosectionlabel a document prefix so identically named subsections
# (e.g. "settings.py" appears under both Model set-up and Outputs) do not clash.
autosectionlabel_prefix_document = True

templates_path = ["_templates"]
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/images/INCHEMPY_logo.png"
html_title = "INCHEM-Py v1.3 documentation"

html_theme_options = {
    "logo_only": True,
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
}

# -- Options for the LaTeX / PDF output --------------------------------------

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
}
