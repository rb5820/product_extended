# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductManufacturer(models.Model):
    _inherit = 'product.template'
    _name = 'product.template'
    _description = 'Product Template with Manufacturer Details'

    country_of_origin = fields.Many2one(
        'res.country',
        string='Country of Origin',
        #domain="[('supplier_rank', '>', 0)]",
        ondelete='restrict',
        tracking=True,
        help="Select the country of origin of the product. Only supplier companies are selectable."
    )

    
    # - **Manufacturer** → `manufacturer_id`
    manufacturer = fields.Many2one(
        'res.partner',
        string='Manufacturer',
        #domain="[('supplier_rank', '>', 0)]",
        tracking=True,
        ondelete='restrict',
        help="Select the manufacturer of the product. Only supplier companies are selectable."
    )
    
    # - **Weight [kg]** → `weight`
    weight = fields.Float(
        string='Weight [kg]',
        tracking=True,
        readonly=False,
        help="Enter the weight of the product in kilograms."
    )
        
    # - **Length [mm]**, 
    length = fields.Float(
        string='Length [mm]',
        readonly=False,
        tracking=True,
        help="Enter the length of the product in millimeters."
    )
    
    #   **Width [mm]**, 
    width = fields.Float(
        string='Width [mm]',
        readonly=False,
        tracking=True,
        help="Enter the width of the product in millimeters."
    )

    #   **Height [mm]**
    height = fields.Float(
        string='Height [mm]',
        readonly=False,
        tracking=True,
        help="Enter the height of the product in millimeters."
    )

    #   → `dimensions`




    manufacturer_model_number = fields.Char(
        string='Manufacturer Model Number',
        tracking=True,
        help="Enter the model number assigned by the manufacturer for this product.",
        readonly=False
    )

    manufacturer_part_number = fields.Char(
        string='Manufacturer Part Number',
        tracking=True,
        help="Enter the part number assigned by the manufacturer for this product.",
        readonly=False
    )

    supplier=fields.Many2one(
        'res.partner',
        string='Suppliers',
        #domain="[('supplier_rank', '>', 0)]",
        tracking=True,
        help="Select the suppliers of the product. Only supplier companies are selectable."
    )   

    supplier_article_number = fields.Char(
        string='Supplier Article Number',
        help="Enter the article number assigned by the supplier for this product.",
        tracking=True,
        readonly=False
    )   

    supplier_model_number = fields.Char(
        string='Supplier Model Number',
        help="Enter the model number assigned by the supplier for this product.",
        tracking=True,
        readonly=False
    )

