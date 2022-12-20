# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaskLineType( models.Model):
    _name = 'payall.task.type'
    _description = 'Modelo para tener clasificado del tipo de actividad en cada registro'

    name = fields.Char(
        string = "Tipo Registro",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    )

    

