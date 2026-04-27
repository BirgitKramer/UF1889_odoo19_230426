from odoo import models, fields

class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
    ], string='State', default='draft')

    tutoring_ids = fields.One2many('academy.tutoring', 'student_id', string='Tutorings')


class Tutoring(models.Model):
    _name = 'academy.tutoring'
    _description = 'Tutoring'

    name = fields.Char(string='Subject', required=True)
    date = fields.Date(string='Date')
    notes = fields.Text(string='Notes')
    student_id = fields.Many2one('academy.student', string='Student', required=True)