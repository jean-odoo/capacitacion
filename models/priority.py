# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Priority(models.Model):
    _name = 'payall.task.priority'
    _description = 'Modelo para tener la referencia del prioridad en la tarea'

    name = fields.Char(
        string = "Prioridad"
    )

    value = fields.Integer(
        string = "Valor"
    )
