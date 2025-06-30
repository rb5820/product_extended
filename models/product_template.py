# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    # Computed field for displaying all dimensions together
    dimensions = fields.Char(
        string='Dimensions (L × W × H)',
        compute='_compute_dimensions',
        help="Displays the product dimensions in format Length × Width × Height (mm)"
    )
    
    @api.depends('length', 'width', 'height')
    def _compute_dimensions(self):
        """Compute a formatted string with all dimensions"""
        for record in self:
            dims = []
            if record.length:
                dims.append(f"{record.length:.1f}")
            else:
                dims.append("?")
                
            if record.width:
                dims.append(f"{record.width:.1f}")
            else:
                dims.append("?")
                
            if record.height:
                dims.append(f"{record.height:.1f}")
            else:
                dims.append("?")
                
            record.dimensions = f"{dims[0]} × {dims[1]} × {dims[2]} mm"