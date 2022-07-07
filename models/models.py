# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rma(models.Model):
    _inherit = 'repair.order'

    @api.model
    def create(self, values):
        correlativo=self.env['ir.sequence'].next_by_code('repair.order')
        secuencia=self.env['ir.sequence'].search([('code','=','repair.order')],limit=1)
        number_actual=secuencia['number_next_actual']
        largo=secuencia['padding']
        rma=self.search([],order="name desc",limit=1).name
        ultimo_correlativo=rma[-largo:]
        ultimo_correlativo="00000"+str((int(ultimo_correlativo)+1))
        ultimo_correlativo=ultimo_correlativo[-5:]
        ultimo_correlativo=secuencia['prefix']+ultimo_correlativo
        values['name'] = ultimo_correlativo
        print(values)
        return super(Rma, self).create(values)