# -*- coding: utf-8 -*-
from odoo import http

# class MethodRmaCorrelativo(http.Controller):
#     @http.route('/method_rma_correlativo/method_rma_correlativo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_rma_correlativo/method_rma_correlativo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_rma_correlativo.listing', {
#             'root': '/method_rma_correlativo/method_rma_correlativo',
#             'objects': http.request.env['method_rma_correlativo.method_rma_correlativo'].search([]),
#         })

#     @http.route('/method_rma_correlativo/method_rma_correlativo/objects/<model("method_rma_correlativo.method_rma_correlativo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_rma_correlativo.object', {
#             'object': obj
#         })