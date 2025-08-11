# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Anton's Mindstorms Docs"
copyright = "2023, Anton, Ste7an"
author = "Anton, Ste7an"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ["sphinx.ext.autodoc", 'sphinx_sitemap', 'sphinx.ext.napoleon']
extensions = ["sphinx.ext.autodoc", 'sphinx.ext.napoleon', 'sphinx.ext.autosummary']
autodoc_mock_imports = ["utime","uos","machine","busio","board","pybricks"]
highlight_language = 'python3'

templates_path = ["_templates"]
exclude_patterns = []

# Import location for autodoc
import os, sys
sys.path.insert(0, os.path.abspath("Software/mpy-robot-tools"))
sys.path.insert(0, os.path.abspath("Software/PyHuskyLens/Library"))
sys.path.insert(0, os.path.abspath("Software/PUPRemote/src"))
sys.path.insert(0, os.path.abspath("Software/SerialTalk/"))
sys.path.insert(0, os.path.abspath("Software/micropup/library/"))

# Options for sitemap
html_baseurl = 'https://docs.antonsmindstorms.com/'
html_extra_path = ['robots.txt']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "images/logo_small.png"
html_favicon = "images/favicon.ico"
html_theme_options = {
    "logo_only": True,
    "display_version": False,
}
