{
    'name': 'Training Syllabus Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Manage training programs and lectures',
    'description': """
        This module allows you to manage training programs and their lectures.
        Features:
        - Create training modules
        - Add lectures to modules
        - Tag lectures for better organization
        - Track lecture duration and materials
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/training_module_views.xml',
        'views/training_lecture_views.xml',
        'views/training_tag_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
} 