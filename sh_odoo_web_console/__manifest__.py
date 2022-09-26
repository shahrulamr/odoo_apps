# -*- coding: utf-8 -*-
{
    'name': 'Odoo 14 Web Console',
    'version': '14.0.1.0.0',
    'category': 'Technical',
    'author': 'ShahrulAmr',
    'maintainer': 'ShahrulAmr',
    'website': 'https://www.linkedin.com/in/shahrul-amirudin',
    'summary': 'Odoo Web Console',
    'description': 'Run and compile python with Odoo environments',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/sh_odoo_web_console_views.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'demo': [],
    'qweb': [],
    'application': True,
    'installable': True,
    'auto_install': False
}
