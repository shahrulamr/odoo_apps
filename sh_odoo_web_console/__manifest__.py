# -*- coding: utf-8 -*-
{
    'name': 'Odoo Web Console',
    'version': '14.0.1.0.0',
    'category': 'Technical',
    'author': 'ShahrulAmr',
    'maintainer': 'ShahrulAmr',
    'website': 'https://github.com/shahrulamr',
    'summary': 'Odoo Web Console',
    'description': 'Run and compile python with Odoo environments',
    'license': 'LGPL-3',
    'depends': ['base','web'],
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
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'sh_odoo_web_console/static/src/css/style.css',
            'sh_odoo_web_console/static/src/js/sh_odoo_web_console.js',
        ],
    }
}
