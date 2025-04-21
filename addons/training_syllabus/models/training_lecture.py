from odoo import models, fields, api

class TrainingLecture(models.Model):
    _name = 'training.lecture'
    _description = 'Training Lecture'

    name = fields.Char(string='Topic', required=True)
    duration = fields.Integer(string='Duration (minutes)', required=True)
    materials = fields.Text(string='Materials')
    module_id = fields.Many2one('training.module', string='Module', required=True)
    tag_ids = fields.Many2many('training.tag', string='Tags') 