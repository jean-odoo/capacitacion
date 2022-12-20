# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import models, fields, api
import datetime

class AccountAnalyticLine( models.Model):
    _inherit = 'account.analytic.line'

    line_type = fields.Many2one(
        string = "Tipo de Tarea",
        comodel_name = "payall.task.type",
        help = "Seleccione la opción que describe con mayor precisión la actividad ejecutada"
    ) 

    def convert_float_to_timestamp(self, unit_amount):
        hours, minutes = divmod(unit_amount, 60)
        return "%02d:%02d"%(hours,minutes)
    
    


    def write(self, vals):

        userMessage = ""
        dateMessage = ""
        employeeMessage = ""
        taskTypeMessage = ""
        unitMessage = ""

        result = super( AccountAnalyticLine, self).write(vals)
        if 'name' in vals and vals['name'] and result:
            userMessage = "<b>User</b> → " + self.name + "<br/>";
        if 'date' in vals and vals['date'] and result:
            dateMessage = "<b>Date</b> → " + str(self.date) + "<br/>"
        if 'employee_id' in vals and vals['employee_id'] and result:
            employeeMessage = "<b>Employee</b> → " + self.employee_id.name + "<br/>";
        if 'line_type' in vals and vals['line_type'] and result:
            taskTypeMessage = "<b>Tipo de Tarea</b> → " + str(self.line_type.name) + "<br/>";
        if 'unit_amount' in vals and vals['unit_amount'] and result:
            unitMessage = "<b>Horas</b> → " + str(self.convert_float_to_timestamp(self.unit_amount)) + "h",

        self.sudo().task_id.message_post( body = 
        userMessage + dateMessage +  employeeMessage + taskTypeMessage + str(unitMessage),
            message_type = "comment"
        )