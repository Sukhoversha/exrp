# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    tax_amount = fields.Float("Tax Amount", compute="_calculate_tax_amount")
    
    def _calculate_tax_amount(self):
        for record in self:
          if record.price_subtotal > 0:
            total_tax_amount = 0
            for tax in record.tax_ids:
              total_tax_amount += tax.amount * record.price_subtotal
            record.x_studio_tax_amount = total_tax_amount