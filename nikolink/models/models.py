# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    tax_amount = fields.Float("Tax Amount", compute="_calculate_amount")
    net_price = fields.Float("Net Price", compute="_calculate_amount")
    net_amount = fields.Float("Net Amount", compute="_calculate_amount")
    
    def _calculate_amount(self):
        for record in self:
          if record.price_subtotal > 0:
            total_tax_amount = 0
            for tax in record.tax_ids:
              total_tax_amount += tax.amount * record.price_subtotal / 100
            record.tax_amount = total_tax_amount
            record.net_price = record.price_unit - total_tax_amount / record.quantity
            record.net_amount = record.net_price * record.quantity
