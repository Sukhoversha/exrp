# -*- coding: utf-8 -*-
# from odoo import http


# class AccountNoTemplate(http.Controller):
#     @http.route('/account_no_template/account_no_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_no_template/account_no_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_no_template.listing', {
#             'root': '/account_no_template/account_no_template',
#             'objects': http.request.env['account_no_template.account_no_template'].search([]),
#         })

#     @http.route('/account_no_template/account_no_template/objects/<model("account_no_template.account_no_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_no_template.object', {
#             'object': obj
#         })
