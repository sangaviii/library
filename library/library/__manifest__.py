{
    'name': "Library",
    'author': "sangavi",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/payment_views.xml',
        'report/report_books_templete.xml',
        'views/customer_views.xml',
        'views/books_views.xml',
        'views/payment_views.xml',
        'views/payment_report.xml',
        'views/report_customer.xml',
        'views/library_report.xml',
        'views/librarian_views.xml',
        'views/manager_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
