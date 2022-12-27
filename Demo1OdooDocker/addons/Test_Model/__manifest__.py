# -*- coding: utf-8 -*-
{
    'name': "Test_Model",

    'summary': """
        Módulo open academy de odoo""",

    'description': """
        Módulo open academy de odoo realizado en base a la documentación de odoo
    """,

    'author': "Andres C Ramirez",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/test_menu.xml',
        'views/estate_menu.xml',
        #'reports/visit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}