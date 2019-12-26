{
    'name': 'Export Stock Excel Report',
    'version': '11.0.1.0.0',
    'category': 'Warehouse',
    'license': "AGPL-3",
    'summary': "Current Stock Report for all Products in each Warehouse",
    'author': 'Itech Resources',
    'company': 'Itech Resources',
    'depends': [
                'base',
                'stock',
                'sale',
                'purchase',
                'report_xlsx'
                ],
    'data': [
            'views/wizard_view.xml',
            'views/wh_location.xml',
            ],
    'installable': True,
    'price':'10.0',
    'currency': 'EUR',
    'auto_install': False,
}
