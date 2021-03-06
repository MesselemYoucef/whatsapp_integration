# -*- coding: utf-8 -*-
{
    'name': 'Whatsapp Integration',
    'version': '1.0',
    'summary': 'Send quotation link of a customer via whatsapp link',
    'sequence': -104,
    'description': """Send quotation link of a customer via whatsapp link""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/sale_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}