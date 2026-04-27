{
    'name': 'Academy Management',
    'description': 'Módulo para gestión de academias online',
    'version': '1.0',
    'author': 'Alumno',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/tutoring_views.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'application': False,
    'auto_install': False,
}