# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json
from datetime import datetime


class SeguimientoClienteController(http.Controller):

    @http.route('/api/seguimientos/cliente/<int:partner_id>', 
                type='http', auth='public', methods=['GET'], csrf=False)
    def get_seguimientos_cliente(self, partner_id):
        partner = request.env['res.partner'].browse(partner_id)
        if not partner.exists():
            return request.make_response(
                json.dumps({'error': 'Cliente no encontrado'}),
                status=404,
                headers=[('Content-Type', 'application/json')]
            )

        data = partner.get_seguimientos_json()
        return request.make_response(
            json.dumps(data, indent=2),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/api/seguimientos/cliente/<int:partner_id>/csv',
                type='http', auth='public', methods=['GET'], csrf=False)
    def download_seguimientos_csv(self, partner_id):
        partner = request.env['res.partner'].browse(partner_id)
        if not partner.exists():
            return request.make_response(
                json.dumps({'error': 'Cliente no encontrado'}),
                status=404,
                headers=[('Content-Type', 'application/json')]
            )

        import csv
        import io
        import base64

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Tipo Actividad', 'Fecha Límite', 'Usuario', 'Descripción', 'Estado'])

        for activity in partner.activity_ids:
            writer.writerow([
                activity.activity_type_id.name or '',
                activity.date_deadline or '',
                activity.user_id.name or '',
                activity.summary or '',
                activity.state or ''
            ])

        csv_data = output.getvalue()
        return request.make_response(
            csv_data,
            headers=[
                ('Content-Type', 'text/csv'),
                ('Content-Disposition', f'attachment; filename=seguimientos_{partner_id}.csv')
            ]
        )

    @http.route('/api/seguimientos/todos',
                type='http', auth='public', methods=['GET'], csrf=False)
    def get_todos_seguimientos(self):
        domain = [('res_model', '=', 'res.partner')]
        activities = request.env['mail.activity'].search(domain)

        result = []
        for activity in activities:
            partner = request.env['res.partner'].browse(activity.res_id)
            result.append({
                'cliente': {
                    'id': partner.id,
                    'name': partner.name,
                },
                'seguimiento': {
                    'id': activity.id,
                    'tipo': activity.activity_type_id.name,
                    'fecha_limite': activity.date_deadline.isoformat() if activity.date_deadline else None,
                    'usuario': activity.user_id.name,
                    'descripcion': activity.summary,
                    'estado': activity.state,
                }
            })

        return request.make_response(
            json.dumps({'seguimientos': result, 'total': len(result)}, indent=2),
            headers=[('Content-Type', 'application/json')]
        )