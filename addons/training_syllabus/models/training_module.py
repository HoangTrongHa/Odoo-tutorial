from odoo import models, fields, api

class TrainingModule(models.Model):
    _name = 'training.module'
    _description = 'Training Module'

    name = fields.Char(string='Module Name', required=True)
    description = fields.Text(string='Description')
    lecture_ids = fields.One2many('training.lecture', 'module_id', string='Lectures')
    total_lectures = fields.Integer(string='Total Lectures', compute='_compute_total_lectures', store=True)

    @api.depends('lecture_ids')
    def _compute_total_lectures(self):
        for module in self:
            module.total_lectures = len(module.lecture_ids) 