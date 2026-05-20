# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'killMS'
copyright = '2026, Cyril Tasse'
author = 'Cyril Tasse'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# do below to add current project to syspath as absolute path
import sys
from pathlib import Path

sys.path.insert(0,str(Path('~/Wirtinger',).resolve()))



extensions = ["sphinx.ext.intersphinx",
              "sphinx.ext.autodoc",
              "sphinx.ext.autosummary",
              "sphinx.ext.napoleon",
              "sphinx.ext.viewcode",
              "sphinx.ext.inheritance_diagram"]

autodoc_mock_imports = ['pytest',
                        'numpy',
                        'astropy',
                        'matplotlib',
                        'regions',
                        'DDFacet',
                        'SharedArray',
                        'ephem',
                        'pycuda']

autodoc_typehints = "description"
autosummary_generate = True

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
