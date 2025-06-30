# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductMultiCompany(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template with Multi-Company Support'

    # Adding a Many2Many field to link products to multiple companies
    # This allows each product to be associated with multiple companies,
    # enabling better management of products across different company contexts.

    allowed_company_ids = fields.Many2many(
        'res.company',
        'product_company_rel',
        'product_id',
        'company_id',
        string='Allowed Companies',
        help="Select the companies that are allowed to view this product."
    )
    
    disallowed_company_ids = fields.Many2many(
        'res.company',
        'product_company_disallowed_rel',
        'product_id',
        'company_id',
        string='Disallowed Companies',
        help="Select the companies that are explicitly NOT allowed to view or use this product."
    )
    
    @api.constrains('allowed_company_ids', 'disallowed_company_ids')
    def _check_company_conflicts(self):
        """Ensure a company cannot be both allowed and disallowed for the same product"""
        for record in self:
            conflicts = set(record.allowed_company_ids.ids) & set(record.disallowed_company_ids.ids)
            if conflicts:
                conflicting_companies = self.env['res.company'].browse(list(conflicts))
                company_names = ', '.join(conflicting_companies.mapped('name'))
                raise models.ValidationError(
                    f"The following companies cannot be both allowed and disallowed: {company_names}"
                )