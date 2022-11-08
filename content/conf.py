# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Python for Scientific Computing'
copyright = '2020, The contributors'
author = 'The contributors'
github_user = 'AaltoSciComp'
github_repo_name = 'python-for-scicomp'  # auto-detected from dirname if blank
github_version = 'master/content/' # with trailing slash


# -- General configuration ---------------------------------------------------

highlight_language = 'python3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_lesson',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_aaltoscicomp_branding',
    'sphinx_plausible',
    'sphinxext.opengraph',
]
#ogp_site_url = 'https://aaltoscicomp.github.io/python-for-scicomp/'

import os
plausible_domain = 'aaltoscicomp.github.io/python-for-scicomp'
plausible_enabled = (
    'GITHUB_ACTION' in os.environ
    and os.environ.get('GITHUB_REPOSITORY', '').lower() == 'aaltoscicomp/python-for-scicomp'
    and os.environ.get('GITHUB_REF') == 'refs/heads/master'
      )


# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', 'jupyter_execute']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# HTML context:
from os.path import dirname, realpath, basename
html_context = {'display_github': True,
                'github_user': github_user,
                # Auto-detect directory name.  This can break, but
                # useful as a default.
                'github_repo': github_repo_name or basename(dirname(realpath(__file__))),
                'github_version': github_version,
               }


intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    }
