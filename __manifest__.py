# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Multiple Quality Check Report",
    'version': '18.0.0.1',
    'category': 'Quality Control',
    'summary': "Nara Coco Land - Generate single PDF report for multiple selected quality check items",
    'description': """
        This module extends the quality check functionality to allow users to:
        - Select multiple quality check items from the list view
        - Generate a single consolidated PDF report for all selected items
        - View detailed quality check information in a professional format
    """,
    'author': "Miyuru Mihilanga",
    'depends': ['base', 'quality_control', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/quality_check_views.xml',
        'report/multiple_quality_check_report.xml',
        'wizard/quality_check_multi_print_wizard_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'license': 'LGPL-3',
}