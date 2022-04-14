# -*- coding: utf-8 -*-
#################################################################################
# Author      : White Wind Ltd. (<https://wwind.ua/>)
# Copyright(c): 2022-White Wind Ltd.
# All Rights Reserved.
#################################################################################
{
    'name': "Product Dimensions",
    'summary': "Provide Product Dimensions Option for  products and product templates",

    'description': """
        Offer dimension attribute like product height, product length, product width
        for products.
    """,

    'author': "White Wind Ltd.",
    'website': "https://wwind.ua",
    'license': 'AGPL-3',

    'category': "Inventory",
    'version': '14.0.1.0.0',

    'depends': ['stock'],

    'data': [
        'views/product_product_views.xml',
    ],
    'installable': True,
    'application': True,
}
