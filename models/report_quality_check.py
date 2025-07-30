# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class ReportMultipleQualityCheck(models.AbstractModel):
    _name = 'report.report_print_custom2.report_multiple_quality_check'
    _description = 'Multiple Quality Check Report'

    def _get_report_values(self, docids, data=None):
        if not data:
            data = {}

        # Always include details and group by product
        data['include_details'] = True
        data['group_by_product'] = True

        docs = self.env['quality.check'].browse(data.get('quality_check_ids', docids))
        return {
            'doc_ids': docids,
            'doc_model': 'quality.check',
            'docs': docs,
            'data': data,
        }