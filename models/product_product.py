from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    length = fields.Char(string='Length')
    width = fields.Char(string='Width')
    height = fields.Char(string='Height')
