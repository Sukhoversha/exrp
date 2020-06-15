# -*- coding: utf-8 -*-

from odoo import models, fields, api


<<<<<<< HEAD
class nikolink(models.Model):
    _inherit = "account.move.line"
    
    tax_amount = fields.Float("Tax Amount")
#     _name = 'nikolink.nikolink'
#     _description = 'nikolink.nikolink'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
=======
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
>>>>>>> 0d783ab20298c9b07ac0c369fb93b01fabd7d76d
