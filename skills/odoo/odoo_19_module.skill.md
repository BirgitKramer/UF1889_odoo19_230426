# Skill: Desarollo de modulo Odoo 19

## Objectivo

Ayudar a crear, revisar y explicar modulos personalizados para Odoo 19, usando buenas practicas de desarollo, ORM, vistas XML, seguridad, datos demo y documentacion.

## Contexto del proyecto

-   ERP/CRM:Odoo 19
-   Base de datos: PostgreSQL
-   Entorno: Ubuntu Serv er en maquina virtual
-   IDE: Kiro
-   Control de versiones: Git
-   Desarollo local en carpeta `addons/`


## Reglas generales

1. Usar siempre ODM de Odoo cuando sea posible.
2. Evitar SQL directo que se justifique .
3. Explicar cada archivo creado.
4. Separa modelos, vistas, seguridad y datos.
5. Mantener nombres tecnicos en `snake_case`.
6. Usar modelos con nombres tipo:
    - `academy.student`
    - `academy.tutoring`
    - `clinic.patient`
    - `clinic.appointment`

## Estructura minima de un modulo

Cuando se cree un modulo Odoo, genera esta esructura:
```text
nombre_modulo/
|-- __init__.py
|-- __manifest__.py
|-- models/
|   |-- __init__.py
|   |-- modelo.py
|-- views/
    |--modelo_views.xml
|-- seccurity/
    |ir.model.access.csv
|-- README.md

```


