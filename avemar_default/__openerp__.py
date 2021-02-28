# -*- coding: utf-8 -*-

{
    'name': 'avemar',
    'version': '9.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización avemar',
    'author': 'Ing. Gabriela Rivero',
    'depends': [],

    'data': [],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'regaby', 'repo': 'cl-avemar', 'branch': '9.0'},
        #{'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '9.0'},
        #{'usr': 'Vauxoo', 'repo': 'addons-vauxoo', 'branch': '9.0'},
        #        {'usr': 'JayVora-SerpentCS', 'repo': 'SerpentCS_Contributions', 'branch': '9.0'},

    ],
    'docker': [
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'}
    ]
}
