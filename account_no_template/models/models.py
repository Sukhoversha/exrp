# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class account_no_template(models.Model):
#     _name = 'account_no_template.account_no_template'
#     _description = 'account_no_template.account_no_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
