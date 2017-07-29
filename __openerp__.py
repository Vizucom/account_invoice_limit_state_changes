# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html.
#
##############################################################################
{
    'name': 'State Change Limitations to Invoices',
    'summary': "Limits state updates to previous months' invoices",
    'version': '7.0.1.0.0',
    'category': 'Accounting',
    'website': 'http://www.vizucom.com',
    'author': 'Vizucom Oy',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'account',
    ],
    'description': """
State Change Limitations for Customer Invoices
==============================================
* Adds a system parameter for setting a date after which old invoices cannot be cancelled or validated
* Intended for situations where users update invoices after e.g. VAT reporting has already been done and sent out, when the correct procedure would be to do an appropriate refund invoice instead of editing an old one.
* See README for configuration
""",
    'data': [
        'data/ir_config_parameter.xml'
    ],
}