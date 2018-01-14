# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright MMM_Corp
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################
{
    'name': 'E-comerce, hide coins from frontend (if not)',

    'summary': 'hide coins in catalog and product page (if possible)',

    'description': 'E-comerce, hide coins from frontend (if not)',

    'author': 'MMM_Corp',
    'category': 'website_sale',
    'version': '0.0.1',

    'active': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        'views/nocoins_templates.xml'
    ],
}
