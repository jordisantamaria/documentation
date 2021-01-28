import os
import sys
from pathlib import Path

from pygments.lexers.web import PhpLexer
from sphinx.highlighting import lexers
from sphinx.util import logging

_logger = logging.getLogger(__name__)


# Add extensions directory to PYTHONPATH
extension_dir = Path('extensions')
sys.path.insert(0, str(extension_dir.absolute()))

# Search for the directory of odoo sources to know whether autodoc should be used on the dev doc
odoo_dir = Path('odoo')
if odoo_dir.exists() and odoo_dir.is_dir():
    sys.path.insert(0, str(odoo_dir.absolute()))
    odoo_dir_in_path = True
else:
    _logger.warning(
        f"Could not find Odoo sources directory at {odoo_dir.absolute()}.\n"
        "The 'Developer' documentation will be built but autodoc directives will be skipped.\n"
        "In order to fully build the 'Developer' documentation, clone the repository with "
        "`git clone https://github.com/odoo/odoo`."
    )
    odoo_dir_in_path = False

# Monkeypatch PHP lexer to not require <?php
lexers['php'] = PhpLexer(startinline=True)

#=== General configuration ===#

# The version info for the project you're documenting, acts as replacement for |version| and
# |release|, also used in various other places throughout the built documents.
version = '12.0'
# The full version, including alpha/beta/rc tags.
release = '12.0'

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '3.0.0'

# The Sphinx extensions to use, as module names.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*') or custom ones.
extensions = [
    # Parse Python docstrings (autodoc, automodule, autoattribute directives)
    'sphinx.ext.autodoc' if odoo_dir_in_path else 'autodoc_placeholder',

    # Link sources in other projects (used to build the reference doc)
    'sphinx.ext.intersphinx',

    # Support the specialized to-do directives
    'sphinx.ext.todo',

    # GitHub links generation
    'sphinx.ext.linkcode',
    'github_link',

    # Custom Odoo theme
    'odoo_theme',

    # Youtube and Vimeo videos integration (youtube, vimeo directives)
    'embedded_video',

    'exercise_admonition',

    # Build code from git patches
    'patchqueue',

    # Redirection generator
    'redirects',
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'odoo'
copyright = 'Odoo S.A.'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# List of patterns, relative to source directory, that match files and directories to ignore when
# looking for source files.
exclude_patterns = [
    'locale',
    'README.*',
    'bin', 'include', 'lib',
]

# The RST text role to use when the role is not specified. E.g.: `example`.
# We use 'literal' as default role for markdown compatibility: `foo` behaves like ``foo``.
# See https://docutils.sourceforge.io/docs/ref/rst/roles.html#standard-roles for other roles.
default_role = 'literal'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The specifications of redirect rules used by the redirects extension.
redirects_file = '../redirects.txt'

#=== Options for HTML output ===#

html_theme = 'odoo_theme'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'odoo'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['extensions']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None  TODO ANVFE remove?

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None  TODO ANVFE remove?

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None  TODO ANVFE remove?

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None  TODO ANVFE remove?

# Add any paths that contain custom static files (such as style sheets) here, relative to this
# directory. They are copied after the builtin static files, so a file named "default.css" will
# overwrite the builtin "default.css".
html_static_path = ['static']
html_add_permalinks = '¶'  # Sphinx < 3.5
html_permalinks = True  # Sphinx >= 3.5
html_js_files = [
    'js/atom.js',
    'js/accounts.js',
    'js/chart-of-accounts.js',
    'js/entries.js',
    'js/reconciliation.js',
    'js/misc.js',
    'js/inventory.js',
    'js/coa-valuation.js',
    'js/coa-valuation-continental.js',
    'js/coa-valuation-anglo-saxon.js',
]
html_css_files = [
    'css/accounting.css',
    'css/legal.css',
]

#=== Options for LaTeX output ===#

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'\usepackage{odoo}',
    'tableofcontents': '',  # no TOC

    # output manually in latex docs
    'releasename': '14.0',
}

latex_additional_files = ['static/latex/odoo.sty']

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('services/legal/terms/enterprise_tex', 'odoo_enterprise_agreement.tex',
     'Odoo Enterprise Subscription Agreement', '', 'howto'),
    ('services/legal/terms/partnership_tex',
        'odoo_partnership_agreement.tex', 'Odoo Partnership Agreement', '', 'howto'),
    ('services/legal/terms/terms_of_sale',
        'terms_of_sale.tex', 'Odoo Terms of Sale', '', 'howto'),

    ('services/legal/terms/i18n/enterprise_tex_fr', 'odoo_enterprise_agreement_fr.tex',
        'Odoo Enterprise Subscription Agreement (FR)', '', 'howto'),
    ('services/legal/terms/i18n/partnership_tex_fr',
        'odoo_partnership_agreement_fr.tex', 'Odoo Partnership Agreement (FR)', '', 'howto'),
    ('services/legal/terms/i18n/terms_of_sale_fr', 'terms_of_sale_fr.tex',
        u'Conditions Générales de Vente Odoo', '', 'howto'),

    ('services/legal/terms/i18n/enterprise_tex_nl', 'odoo_enterprise_agreement_nl.tex',
        'Odoo Enterprise Subscription Agreement (NL)', '', 'howto'),

    ('services/legal/terms/i18n/enterprise_tex_de', 'odoo_enterprise_agreement_de.tex',
        'Odoo Enterprise Subscription Agreement (DE)', '', 'howto'),

    ('services/legal/terms/i18n/enterprise_tex_es', 'odoo_enterprise_agreement_es.tex',
        'Odoo Enterprise Subscription Agreement (ES)', '', 'howto'),
    ('services/legal/terms/i18n/partnership_tex_es',
        'odoo_partnership_agreement_es.tex', 'Odoo Partnership Agreement (ES)', '', 'howto'),
]

# The name of an image file (relative to this directory) to place at the top of the title page.
latex_logo = 'static/img/odoo_logo.png'

# If true, show URL addresses after external links.
latex_show_urls = "True"

#=== Extensions options ===#

todo_include_todos = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'werkzeug': ('https://werkzeug.palletsprojects.com/en/1.0.x/', None),
}

github_user = 'odoo'
github_project = 'documentation-user'

locale_dirs = ['locale/']

LANGUAGES = {
    'de': 'German',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'hr': 'Croatian',
    'nl': 'Dutch',
    'pt_BR': 'Portuguese (BR)',
    'uk': 'Ukrainian',
    'zh_CN': 'Chinese',
}

def setup(app):
    app.connect('html-page-context', canonicalize)
    # VFE TODO remove default before merge
    app.add_config_value('canonical_root', os.path.dirname(os.path.realpath(__file__)), 'env')
    app.add_config_value('canonical_branch', 'master', 'env')

    app.connect('html-page-context', versionize)
    # VFE TODO before merge, remove the default value put for testing
    test_versions = ['12.0', '13.0', '14.0']  # TODO if not provided, use 'local'
    app.add_config_value('versions', ",".join(test_versions), 'env')

    app.connect('html-page-context', localize)
    # VFE TODO before merge remove the default value put for testing
    test_languages = ['fr', 'en', 'es']
    app.add_config_value('languages', ",".join(test_languages), 'env')

    app.connect('doctree-resolved', tag_toctrees)  # TODO ANVFE not used + typo


def export_collapse_menu_option(app, pagename, templatename, context, doctree):
    context['collapse_menu'] = app.config.collapse_menu


def versionize(app, pagename, templatename, context, doctree):
    """ Adds a version switcher below the menu, requires ``canonical_root``
    and ``versions`` (an ordered, space-separated lists of all possible
    versions).
    """
    if not (app.config.canonical_root and app.config.versions):
        return

    context['versions'] = [
        (vs, _build_url(app.config.canonical_root, vs, pagename))
        for vs in app.config.versions.split(',')
        if vs != app.config.version
    ]

def tag_toctrees(app, doctree, docname):
    """Add a 'is-toc-page' metadata entry to all documents containing only a toctree node"""
    # document
    #   section
    #     title
    #     compound@toctree-wrapper
    #     ....
    if not len(doctree.children) == 1:
        return
    section = doctree.children[0]
    if len(section.children) < 2:
        return
    compound = section.children[1]
    if 'toctree-wrapper' not in compound['classes']:
        return

    app.env.metadata[docname]['has_only_toc'] = True

def localize(app, pagename, templatename, context, doctree):
    """ Adds a language switcher below the menu, requires ``canonical_root``
    and ``languages`` (an ordered, space-separated lists of all possible
    languages).
    """
    if not (app.config.canonical_root and app.config.languages):
        return

    current_lang = app.config.language or 'en'
    context['language'] = LANGUAGES.get(current_lang, current_lang.upper())
    context['languages'] = [
        (LANGUAGES.get(la, la.upper()), _build_url(
            app.config.canonical_root, (la != 'en' and la or ''), pagename))
        for la in app.config.languages.split(',')
        if la != current_lang
    ]
    context['language_codes'] = [
        (la.split('_')[0] if la != 'en' else 'x-default',
         _build_url(app.config.canonical_root, (la != 'en' and la or ''), pagename))
        for la in app.config.languages.split(',')
    ]

def canonicalize(app, pagename, templatename, context, doctree):
    """ Adds a 'canonical' URL for the current document in the rendering
    context. Requires the ``canonical_root`` setting being set. The canonical
    branch is ``master`` but can be overridden using ``canonical_branch``.
    /documentation/user/12.0/sale.html -> /documentation/user/13.0/sale.html
    /documentation/user/11.0/fr/website.html -> /documentation/user/13.0/fr/website.html
    """
    if not app.config.canonical_root:
        return

    lang = app.config.language or 'en'

    context['canonical'] = _build_url(
        app.config.canonical_root, app.config.canonical_branch, pagename, lang)


def _build_url(root, branch, pagename, lang='en'):
    return "{canonical_url}{canonical_branch}{lang}/{canonical_page}".format(
        canonical_url=root,
        canonical_branch=branch,
        lang=lang != 'en' and lang or '',
        canonical_page=(pagename + '.html').replace('index.html', '')
                                           .replace('index/', ''),
    )
