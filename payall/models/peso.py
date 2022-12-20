# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Peso(models.Model):
    _name = 'payall.task.peso'
    _description = 'Modelo para tener la referencia del peso de la tarea'

    name = fields.Char(
        string = "Peso"
    )
    
    @api.onchange('name')
    def _check_duplicates_peso(self):
        for record in self:
            name = self.env['payall.task.peso'].search([('name', '=', record.name)])
            if name:
                raise UserError('El valor de peso ya está registrado')
