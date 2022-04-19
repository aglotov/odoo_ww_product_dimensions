from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    ww_length = fields.Char(string='Length')
    ww_width = fields.Char(string='Width')
    ww_height = fields.Char(string='Height')
    ww_dimensions_uom_name = fields.Char(string='Dimensions unit of measure label',
                                         compute='_compute_ww_dimension_uom_name')

    @api.model
    def _get_dimensions_uom_name_from_ir_config_parameter(self):
        uom_id = self.env['ir.config_parameter'].sudo().get_param('ww_product_dimensions.uom')
        return self.env['uom.uom'].browse(int(uom_id)).display_name

    def _compute_ww_dimension_uom_name(self):
        self.ww_dimensions_uom_name = self._get_dimensions_uom_name_from_ir_config_parameter()
