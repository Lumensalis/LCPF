# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LCPF'
copyright = '2025, James Fowler'
author = 'James Fowler'
release = '0.0.1'

import sys
from pathlib import Path

sys.path.insert(0, str(Path('..', 'lumensaliscplib', 'lib').resolve()))
#sys.path.insert(0, str(Path('..', 'CircuitPyDependencies', 'lib').resolve()))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'sphinx.ext.autodoc',
    'autodoc2',
    'sphinx_markdown_builder'
    #'sphinx_starlight_builder'
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_mock_imports = ["board", "digitalio","wifi",
                        "adafruit_requests", "adafruit_esp32spi", "adafruit_esp32spi_wifimanager", "adafruit_esp32spi_socketpool", "adafruit_esp32spi.adafruit_esp32spi_socketpool",
                        "displayio"
                       ]


autodoc2_packages = [
    {
        "path": "../lumensaliscplib/lib/LumensalisCP",
        "auto_mode": True,
    },
]
autodoc2_hidden_regexes =   [
    r"^.*HTML_TEMPLATE_.*$",
]

markdown_uri_doc_suffix = ".mdx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
