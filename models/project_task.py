# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTask( models.Model):
    _inherit = 'project.task'

    line_type = fields.Many2one(
        string = "Tipo de Tarea",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    )

    sprint = fields.Integer(
        string = "Sprint",
        help = "Indique el número del sprint en el que está incluido el ítem"
    )

    priority_payall = fields.Many2one(
        string = "Prioridad",
        comodel_name = "payall.task.priority",
        help = "Clasifique el ítem de trabajo según su importancia"
    )

    peso = fields.Many2one(
        string = "Peso",
        comodel_name = "payall.task.peso",
        help = "Clasifique el ítem según la magnitud del trabajo requerido"
    )

    message_ids = fields.One2many(readonly=True)
    activity_ids = fields.One2many(readonly=True)
    peso_computed = fields.Integer(string='Peso', store=True)
    prioridad_computed = fields.Integer(string='Prioridad', store=True)


    def write(self, vals):

        result = super( ProjectTask, self).write(vals)
        if 'peso' in vals and vals['peso'] and result:
            self.sudo().message_post( body = 
                "El usuario " + self.env.user.display_name + " ha modificado el peso a  " + self.peso.name,
                message_type = "comment"
            )
    
    @api.onchange('peso')
    def _getPesoComputed(self):
        for record in self:
            peso_comp = self.env['payall.task.peso'].search([('name', '=', record.peso.name)])
            record.peso_computed = peso_comp.name
    
    #@api.onchange('priority_payall')
    #def _getPrioridadComputed(self):
    #    for record in self:
    #        prioridad_comp = self.env['payall.task.priority'].search([('id', '=', record.priority_payall.id)])
    #        record.prioridad_computed =  prioridad_comp.id