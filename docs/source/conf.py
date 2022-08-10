# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../../pyavtech'))

# -- Project information -----------------------------------------------------

project = 'PyAvr'
copyright = '2022, UL_Solutions'
author = 'Laurent Bonnet'

# The full version, including alpha/beta/rc tags
version = "0.4.0"
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {}

# UL Logo
html_logo = './_images/UL_Solutions.png'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

autodoc_mock_imports = ["pyvisa"]

# -- Options for Latex output -------------------------------------------------
# today = 'March 2, 2021'
today_fmt = "Generated on %b %d, %Y"

latex_engine = 'xelatex'
latex_logo = './_images/Ul_Red.png'

latex_elements = {
    'fontenc': '\\usepackage{fontspec}',
    'fontpkg': '''\
                \\setmainfont{DejaVu Serif}
                \\setsansfont{DejaVu Sans}
                \\setmonofont{DejaVu Sans Mono}''',
    'geometry': '\\usepackage[vmargin=2.5cm, hmargin=3cm]{geometry}',
    'preamble': '''\
                \\usepackage[titles]{tocloft}
                \\cftsetpnumwidth {1.25cm}\\cftsetrmarg{1.5cm}
                \\setlength{\\cftchapnumwidth}{0.75cm}
                \\setlength{\\cftsecindent}{\\cftchapnumwidth}
                \\setlength{\\cftsecnumwidth}{1.25cm}''',
    'fncychap': '\\usepackage[Sonny]{fncychap}',
    'printindex': '\\footnotesize\\raggedright\\printindex',
    'classoptions': ',oneside',
}

