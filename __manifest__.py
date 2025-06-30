# -*- coding: utf-8 -*-
{
    'name': 'Product Extended',
    'version': '18.0.1.3.1',
    'category': 'Inventory/Inventory',
    'summary': 'Extended product features for multi-company and manufacturer details',
    'author': 'RB5820',
    'website': "https://www.attiesatelier.be",
    'license': 'LGPL-3',
    'description': """
Product Extended
===============

This module extends the product functionality with:

* Multi-company support for products (both allowed and disallowed companies)
* Manufacturer and supplier details
* Physical dimensions and specifications
* European Waste Code (EWC) integration for regulatory compliance
* IEC 62443 industrial security capability compliance tracking
* Serial number tracking for asset management
* Enhanced tracking and activity features

Key Features:
------------
* Link products to multiple companies
* Track manufacturer details (country of origin, part numbers)
* Record detailed product dimensions
* Supplier information tracking
* European Waste Classification integration
* IEC 62443 security capability levels for industrial systems
* Serial number inventory tracking for asset management
""",
    'depends': [
        'base',
        'product',
        'mail',
        'stock',
    ],
    'data': [
        'security/product_extended_security.xml',
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_template_multi_company_views.xml',
        'data/product_extended_data.xml',
    ],
    'demo': [
        'data/product_extended_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
