from odoo import models, fields

class TrainingTag(models.Model):
    _name = 'training.tag'
    _description = 'Training Tag'

    name = fields.Char(string='Tag Name', required=True)
    lecture_ids = fields.Many2many('training.lecture', string='Lectures') 