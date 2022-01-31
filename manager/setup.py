# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['knot_resolver_manager',
 'knot_resolver_manager.client',
 'knot_resolver_manager.compat',
 'knot_resolver_manager.datamodel',
 'knot_resolver_manager.datamodel.types',
 'knot_resolver_manager.kresd_controller',
 'knot_resolver_manager.kresd_controller.supervisord',
 'knot_resolver_manager.kresd_controller.systemd',
 'knot_resolver_manager.utils']

package_data = \
{'': ['*'],
 'knot_resolver_manager.datamodel': ['templates/*', 'templates/macros/*']}

install_requires = \
['Jinja2>=2.11.3',
 'PyGObject>=3.38.0',
 'PyYAML>=5.4.1',
 'aiohttp>=3.6.12',
 'click>=7.1.2',
 'pydbus>=0.6.0',
 'requests>=2.25.1',
 'typing-extensions>=3.7.2']

setup_kwargs = {
    'name': 'knot-resolver-manager',
    'version': '0.1.0',
    'description': 'A central management tool for multiple instances of Knot Resolver',
    'long_description': None,
    'author': 'Václav Šraier',
    'author_email': 'vaclav.sraier@nic.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.8,<4.0.0',
}


setup(**setup_kwargs)


# This setup.py was autogenerated using Poetry for backward compatibility with setuptools.