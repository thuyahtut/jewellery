# -*- coding: utf-8 -*-
# from odoo import http


# class Jewellery(http.Controller):
#     @http.route('/jewellery/jewellery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jewellery/jewellery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jewellery.listing', {
#             'root': '/jewellery/jewellery',
#             'objects': http.request.env['jewellery.jewellery'].search([]),
#         })

#     @http.route('/jewellery/jewellery/objects/<model("jewellery.jewellery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jewellery.object', {
#             'object': obj
#         })
