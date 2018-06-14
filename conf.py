from recommonmark.parser import CommonMarkParser
extensions = ['sphinx.ext.mathjax',
    'sphinx.ext.githubpages']
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_parsers = {
        '.md': CommonMarkParser,
        }
master_doc = 'index'
project = 'Tecnologia em Redes de Computadores'
copyright = '2018, IFRN'
author = 'IFRN'
version = '2012'
release = '2012'
language = 'pt_BR'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'tsup-redesdoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'tsup-redes.tex', 'Tecnologia em Redes de Computadores',
     'IFRN', 'manual'),
]
man_pages = [
    (master_doc, 'tcnicointegradoeminformtica', 'Técnico Subsequente em Redes de Computadores Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'ts-redes', 'Técnico Subsequente em Redes de Computadores Documentation',
     author, 'ts-redes', 'One line description of project.',
     'Miscellaneous'),
]
