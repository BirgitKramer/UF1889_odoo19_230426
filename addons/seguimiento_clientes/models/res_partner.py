# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression
import csv
import io
import base64
from datetime import datetime


class ResPartner(models.Model):
    _inherit = 'res.partner'

    seguimiento_count = fields.Integer(
        string='Nº Seguimientos',
        compute='_compute_seguimiento_count',
        store=True,
    )
    ultimo_seguimiento = fields.Datetime(
        string='Último Seguimiento',
        compute='_compute_ultimo_seguimiento',
        store=True,
    )

    @api.depends('activity_ids')
    def _compute_seguimiento_count(self):
        for partner in self:
            partner.seguimiento_count = len(partner.activity_ids)

    @api.depends('activity_ids.date_deadline')
    def _compute_ultimo_seguimiento(self):
        for partner in self:
            activities = partner.activity_ids.sorted('date_deadline', reverse=True)
            partner.ultimo_seguimiento = activities[0].date_deadline if activities else False

    def get_seguimientos_read_group(self):
        self.ensure_one()
        seguimientos = self.env['mail.activity'].read_group(
            domain=[
                ('res_model', '=', 'res.partner'),
                ('res_id', '=', self.id)
            ],
            fields=['res_id', 'activity_type_id', 'date_deadline', 'user_id'],
            groupby=['res_id']
        )
        return seguimientos

    def action_export_csv(self):
        self.ensure_one()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Cliente', 'Tipo Actividad', 'Fecha Límite', 'Usuario', 'Descripción'])

        for activity in self.activity_ids:
            writer.writerow([
                self.name,
                activity.activity_type_id.name or '',
                activity.date_deadline or '',
                activity.user_id.name or '',
                activity.summary or ''
            ])

        csv_data = base64.b64encode(output.getvalue().encode('utf-8'))
        self.env['ir.attachment'].create({
            'name': f'seguimientos_{self.id}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
            'type': 'binary',
            'datas': csv_data,
            'res_model': 'res.partner',
            'res_id': self.id,
        })

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Exportado',
                'message': 'CSV exportado correctamente',
                'type': 'success',
            }
        }

    def get_seguimientos_json(self):
        self.ensure_one()
        return {
            'cliente': {
                'id': self.id,
                'name': self.name,
                'email': self.email,
            },
            'seguimientos': [
                {
                    'id': activity.id,
                    'tipo': activity.activity_type_id.name,
                    'fecha_limite': activity.date_deadline.isoformat() if activity.date_deadline else None,
                    'usuario': activity.user_id.name,
                    'descripcion': activity.summary,
                    'estado': activity.state,
                }
                for activity in self.activity_ids
            ],
            'total_seguimientos': len(self.activity_ids),
            'exportado_en': datetime.now().isoformat(),
        }