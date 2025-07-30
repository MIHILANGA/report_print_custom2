# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class QualityCheckMultiPrintWizard(models.TransientModel):
    _name = 'quality.check.multi.print.wizard'
    _description = 'Quality Check Multi Print Wizard'

    quality_check_ids = fields.Many2many(
        'quality.check',
        string='Quality Checks',
        required=True
    )
    report_title = fields.Char(
        string='Report Title',
        default='Multiple Quality Check Report',
        required=True
    )

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        active_ids = self.env.context.get('active_ids', [])
        if active_ids and 'quality_check_ids' in fields_list:
            defaults['quality_check_ids'] = [(6, 0, active_ids)]
        return defaults

    def action_print_report(self):
        if not self.quality_check_ids:
            raise UserError(_('Please select at least one quality check to print.'))

        data = {
            'quality_check_ids': self.quality_check_ids.ids,
            'report_title': self.report_title,
            'include_details': True,
            'group_by_product': True,
        }

        return self.env.ref('report_print_custom2.action_report_multiple_quality_check').report_action(
            self.quality_check_ids, data=data
        )