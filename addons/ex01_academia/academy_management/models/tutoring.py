from odoo import models, fields

class Tutoring(models.Model):
    _name = 'academy.tutoring'
    _description = 'Tutoring'

    name = fields.Char(string='Subject', required=True)
    date = fields.Date(string='Date')
    notes = fields.Text(string='Notes')
    student_id = fields.Many2one('academy.student', string='Student', required=True)