# -*- coding: utf-8 -*-
{
    'name': "App_Demo_1",

    'summary': """
        App Demo para pruebas de Odoo y Docker""",

    'author': "Andres C Ramirez",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/menu_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'views/libros_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}
