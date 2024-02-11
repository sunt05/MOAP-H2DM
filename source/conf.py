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
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime

# determine if in RTD environment
read_the_docs_build = os.environ.get("READTHEDOCS", None) == "True"


if read_the_docs_build:
    # normal build
    # update `today`
    dt_today = datetime.today()
else:
    # quick build for local testing
    dt_today = datetime(2023, 10, 7)
    # subprocess.call("doxygen", shell=True)
    pass


# -- Project information -----------------------------------------------------

project = "UCL MOAP-H2DM Colloquium Series"
author = 'Dr Ting Sun'
copyright = f"2023 – {dt_today.year}, {author}"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_theme_options = {
    "external_links": [
        (
            "MS Teams channel",
            "https://teams.microsoft.com/l/channel/19%3Ab8NiG86SHHDQHrjgH_pwXU7V6s0v5vzcadF5AUJd6_g1%40thread.tacv2/General?groupId=bf631c1a-91a2-4336-b122-f4a478a2e182&tenantId=1faf88fe-a998-4c5b-93c9-210a11d9a5c2",
        ),
        (
            "Sign up your talk!",
            "https://forms.office.com/e/cJy0zfNXcS",
        ),
    ]
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'press'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
