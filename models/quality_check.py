# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class QualityCheck(models.Model):
    _inherit = 'quality.check'

    def action_open_multi_print_wizard(self):
        """Open wizard for printing multiple quality checks"""
        active_ids = self.env.context.get('active_ids', [])
        if not active_ids:
            raise UserError(_('Please select at least one quality check record.'))

        return {
            'type': 'ir.actions.act_window',
            'name': _('Print Multiple Quality Checks'),
            'res_model': 'quality.check.multi.print.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_quality_check_ids': [(6, 0, active_ids)],
                'active_ids': active_ids,
                'active_model': 'quality.check',
            }
        }