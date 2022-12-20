# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTaskCreateTimesheet( models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    line_type = fields.Many2one(
        string = "Tipo Registro",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    ) 