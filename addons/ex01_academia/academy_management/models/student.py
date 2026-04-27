from odoo import models, fields

class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student online academy'

    name = fields.Char(
        string='Name', 
        required=True)

    email = fields.Char(
        string='Email')

    phone = fields.Char(
        string='Phone')

    state = fields.Selection(
        [
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ], 
        string='State', 
        default='draft'
    )
    active = fields.Boolean(
        string='Active', 
        default=True)

    tutoring_ids = fields.One2many 'academy_tutoring','student_id',(
        string='Tutorings')