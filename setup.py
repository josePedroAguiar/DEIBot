# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['main']
install_requires = \
['discord>=1.0.1,<2.0.0', 'flask>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'main',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
