from odoo import models, fields, api

class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student online academy'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
    ], string='State', default='draft')
    active = fields.Boolean(string='Active', default=True)
    
    tutoring_count = fields.Integer(
        string='Tutoring Count',
        compute='_compute_tutoring_count',
        store=True
    )
    last_tutoring_date = fields.Date(
        string='Last Tutoring Date',
        compute='_compute_last_tutoring_date',
        store=True
    )
    
    tutoring_ids = fields.One2many(
        'academy.tutoring',
        'student_id',
        string='Tutorings'
    )

    @api.depends('tutoring_ids')
    def _compute_tutoring_count(self):
        for record in self:
            record.tutoring_count = len(record.tutoring_ids)

    @api.depends('tutoring_ids.date')
    def _compute_last_tutoring_date(self):
        for record in self:
            if record.tutoring_ids:
                dates = record.tutoring_ids.mapped('date')
                record.last_tutoring_date = max(f for f in dates if f) if dates else False
            else:
                record.last_tutoring_date = False