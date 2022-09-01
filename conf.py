# BeagleBoard.org documentation build configuration file.
# 
# References: 
# https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/conf.py
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path
import re
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.append('.')
import sphinx_rtd_theme

BBDOCS_BASE = Path(__file__).resolve().parents[0]

# -- Project information -----------------------------------------------------

project = 'BeagleBoard Docs'
copyright = '2022, BeagleBoard.org Foundation'
author = 'BeagleBoard.org Foundation'


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinxcontrib.rsvgconverter",
    "sphinx_design"
]

templates_path = ['_templates']

source_suffix = '.rst'
numfig = True
navigation_with_keys = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    'prev_next_buttons_location': 'bottom',
}
html_title = "BeagleBoard Documentation"
html_logo = str(BBDOCS_BASE / "_static" / "images" / "logo.svg")
html_favicon = str(BBDOCS_BASE / "_static" / "images" / "favicon.ico")
html_static_path = [str(BBDOCS_BASE / "_static")]
html_last_updated_fmt = "%b %d, %Y"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_baseurl = 'docs.beagleboard.io'

# parse version from 'VERSION' file
with open(BBDOCS_BASE  / "VERSION") as f:
    m = re.match(
        (
            r"^VERSION_MAJOR\s*=\s*(\d+)$\n"
            + r"^VERSION_MINOR\s*=\s*(\d+)$\n"
            + r"^PATCHLEVEL\s*=\s*(\d+)$\n"
            + r"^VERSION_TWEAK\s*=\s*\d+$\n"
            + r"^EXTRAVERSION\s*=\s*(.*)$"
        ),
        f.read(),
        re.MULTILINE,
    )

    if not m:
        sys.stderr.write("Warning: Could not extract docs version\n")
        version = "Unknown"
    else:
        major, minor, patch, extra = m.groups(1)
        version = ".".join((major, minor, patch))
        if extra:
            version += "-" + extra

release = version

# parse pages details from 'PAGES' file
with open(BBDOCS_BASE  / "PAGES") as f:
    m = re.match(
        (
            r"^PAGES_URL\s*=\s*(\S+)$\n"
            + r"^PAGES_SLUG\s*=\s*(\S+)$\n"
        ),
        f.read(),
        re.MULTILINE,
    )

    if not m:
        sys.stderr.write("Warning: Could not extract pages information\n")
        pages_url = "Unknown"
        pages_slug = "Unknown"
    else:
        url, slug = m.groups(1)
        pages_url = url
        pages_slug = slug
        if slug == "main":
            docs_url = "/".join((url, "latest"))
        else:
            docs_url = "/".join((url, slug))

html_context = {
    "display_gitlab": True,
    "gitlab_host": "git.beagleboard.org",
    "gitlab_user": "docs",
    "gitlab_repo": "docs.beagleboard.io",
    "gitlab_version": "main",
    "conf_py_path": "/",
    "show_license": True,
    "pages_url": pages_url,
    "pages_slug": pages_slug,
    "docs_url": docs_url,
    "current_version": version
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    "papersize": "a4paper",
    "maketitle": open(BBDOCS_BASE / "_static" / "latex" / "title.tex").read(),
    "preamble": open(BBDOCS_BASE / "_static" / "latex" / "preamble.tex").read(),
    "fontpkg": r"\usepackage{charter}",
    "sphinxsetup": ",".join(
        (
            "verbatimwithframe=false",
            "VerbatimColor={HTML}{f0f2f4}",
            "InnerLinkColor={HTML}{2980b9}",
            "warningBgColor={HTML}{e9a499}",
            "warningborder=0pt",
            r"HeaderFamily=\rmfamily\bfseries",
        )
    ),
}
latex_logo = str(BBDOCS_BASE / "_static" / "images" / "logo-latex.pdf")
latex_documents = [
    ("index-tex", "beagleboard-docs.tex", "BeagleBoard Docs", author, "manual"),
]

def setup(app):
    # theme customizations
    app.add_css_file("css/custom.css")
