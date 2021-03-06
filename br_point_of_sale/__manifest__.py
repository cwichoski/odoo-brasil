# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Point of Sale Brazil',
    'summary': """Module to adapt Odoo Point of Sale to Brazil""",
    'description': 'Point of Sale Brazil',
    'version': '12.0.1.0.0',
    'category': 'pos',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>'
    ],
    'depends': [
        'point_of_sale',
        'br_nfe',
    ],
    'external_dependencies': {
        'python': [
            'pytrustnfe',
        ],
    },
    'data': [
        'views/account_journal.xml',
        'views/pos_order.xml',
        'views/invoice_eletronic.xml',
        'views/pos_assets.xml',
    ],
    "qweb": [
        'static/src/xml/pos.xml',
    ],
    'application': True,
    'installable': True
}
