from odoo import models, fields

class Tutoring(models.Model):
    _name = 'academy.tutoring'
    _description = ' Tutoring online academy'

    name = fields.Char(string='Titulo', required=True)
    date = fields.Date(string='Date')
    notes = fields.Text(string='Notes')
    student_id = fields.Many2one(
        comodel_name= 'academy.student', 
        string='Student', 
        required=True,
        ondelete='cascade'
    )
    course = fields.Char(string='Course')
    date = fields.Date(
        string='Date'
        required=True
    )
    duration= fields.Float(string='Duration(hours)')
    notes = fields.Text(string='Notes')