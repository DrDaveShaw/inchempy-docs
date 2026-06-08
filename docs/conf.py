# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'INCHEM-Py'
copyright = '2019-2023, David Shaw & Nicola Carslaw'
author = 'David Shaw, Nicola Carslaw'
release = 'v1.2.1'

extensions = [
    'sphinx.ext.mathjax',  # for LaTeX math rendering
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = '_static/images/INCHEMPY_logo.png'
html_theme_options = {
    'logo_only': False,
    'navigation_depth': 3,
}

# MathJax for equations
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
