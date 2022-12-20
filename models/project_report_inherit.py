# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools


class ReportProjectTaskUserInherit(models.Model):
    _inherit = 'report.project.task.user'

    sprint = fields.Integer(
        string = "Sprint",
        help = "Indique el número del sprint en el que está incluido el ítem"
    )

    priority_payall = fields.Many2one(
        string="Prioridad",
        comodel_name="payall.task.priority",
        help="Clasifique el ítem de trabajo según su importancia"
    )

    peso_computed = fields.Integer(string='Peso', store=True)
    #prioridad_computed = fields.Integer(string='Prioridad', store=True)
   
    def _select(self):
        select_str = """
             SELECT
                    (select 1 ) AS nbr,
                    t.id as id,
                    t.id as task_id,
                    t.create_date as create_date,
                    t.date_assign as date_assign,
                    t.date_end as date_end,
                    t.date_last_stage_update as date_last_stage_update,
                    t.date_deadline as date_deadline,
                    t.project_id,
                    t.priority,
                    t.name as name,
                    t.company_id,
                    t.partner_id,
                    t.stage_id as stage_id,
                    t.kanban_state as state,
                    NULLIF(t.rating_last_value, 0) as rating_last_value,
                    t.working_days_close as working_days_close,
                    t.working_days_open  as working_days_open,
                    t.working_hours_open as working_hours_open,
                    t.working_hours_close as working_hours_close,
                    t.sprint,
                    t.peso_computed,
                    t.priority_payall,
                    (extract('epoch' from (t.date_deadline-(now() at time zone 'UTC'))))/(3600*24)  as delay_endings_days
        """
        return select_str

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE view %s as
              %s
              FROM project_task t
              LEFT JOIN project_task_user_rel tu on t.id=tu.task_id
                WHERE t.active = 'true'
                AND t.project_id IS NOT NULL
                %s
        """ % (self._table, self._select(), self._group_by()))
