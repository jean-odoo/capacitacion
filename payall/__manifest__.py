# -*- coding: utf-8 -*-
{
    'name': "payall",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Payall",
    'license': 'GPL-3',
    'website': "https://payall.com.ve/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','timesheet_grid'],

    # always loaded
    'data': [
        'security/payall_security.xml',
        'security/ir.model.access.csv',
        'data/prioridad_data.xml',
        'data/tipo_registro.xml',
        'views/project_payall_task_priority.xml',
        'views/hr_timesheet_project_task_create_timesheet_inherit.xml',
        'views/project_task_create_timesheet_inherit.xml',
        'views/project_payall_task_peso.xml',
        'views/project_payall_task_type.xml',
        'views/account_analytic_line_inherit.xml',
        'views/project_task_view_graph_inherited.xml',
        'views/project_task_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
