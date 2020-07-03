def setup(app):
    app.add_css_file('css/custom.css')


extensions = [
  'sphinx.ext.autosectionlabel', 'sphinx.ext.todo', 'sphinx_fontawesome'
  ]
source_suffix = '.rst'
master_doc = 'index'
project = u'SCS Contributor Guide'
copyright = u''
author = u''
version = u''
release = u''
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
html_show_sourcelink = False
html_show_copyright = False
htmlhelp_basename = 'contributor-guide'
html_theme_options = {
    'display_version': False,
    'canonical_url': 'https://docs.scs.community/contributors/',
    'style_external_links': True,
    'logo_only': True,
    'prev_next_buttons_location': None
}
html_context = {
    'display_github': True,
    'github_user': 'SovereignCloudStack',
    'github_repo': 'contributor-guide',
    'github_version': 'master',
    'conf_py_path': '/source/'
}
html_logo = 'images/logo.png'
html_static_path = [
    '_static'
]
latex_elements = {}
