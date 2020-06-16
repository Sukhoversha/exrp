# -*- coding: utf-8 -*-
# from odoo import http


# class Nikolink(http.Controller):
#     @http.route('/nikolink/nikolink/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nikolink/nikolink/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nikolink.listing', {
#             'root': '/nikolink/nikolink',
#             'objects': http.request.env['nikolink.nikolink'].search([]),
#         })

#     @http.route('/nikolink/nikolink/objects/<model("nikolink.nikolink"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nikolink.object', {
#             'object': obj
#         })
