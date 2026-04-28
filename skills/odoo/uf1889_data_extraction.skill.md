# Skill: UF1889 - Extraccion de datos ERP (Odoo 19)

## Objectivo

Realizar la extraccion y procesamiento de los datos
- numero de seguimiento por clientes
- uso del ORM
- campo calculado
- exportacion CSV
- simulacion API JSON

## Modelos implicados

- res.partner -> clientes
- mail.activity ->seguimientos

## Paso 1: Identficacion

El cliente es el modelo principal.
El seguimiento es la actividad asociada.

Relacion:
- Un cliente tiene muchos seguimientos

## Paso 2: Consulta ORM
Usar `read_group` para optimizar:
```python
  seguimiento = self,env[`mail.activity'].read_group(
    domain=[('res_model', '=', 'res.partner')],
    fields=['res_id'],
    groupby=['res.id']
)
```


