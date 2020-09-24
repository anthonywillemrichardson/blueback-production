# -*- coding: utf-8 -*-
{
    'name': 'Blueback: Facebook Pixel Integration',
    'summary': 'Integrating facebook pixel on the website',
    'sequence': 100,
    'license': 'OEEL-1',
    'website': 'https://www.odoo.com',
    'version': '1.1',
    'author': 'Odoo Inc',
    'description': """
        Task ID: 2329017
    """,
    'category': 'Custom Development',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/res_config_settings_views.xml',
        'templates/website_layout.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}