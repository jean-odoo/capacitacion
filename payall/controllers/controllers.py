# -*- coding: utf-8 -*-
# from odoo import http


# class Formato-factura(http.Controller):
#     @http.route('/formato-factura/formato-factura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formato-factura/formato-factura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formato-factura.listing', {
#             'root': '/formato-factura/formato-factura',
#             'objects': http.request.env['formato-factura.formato-factura'].search([]),
#         })

#     @http.route('/formato-factura/formato-factura/objects/<model("formato-factura.formato-factura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formato-factura.object', {
#             'object': obj
#         })
