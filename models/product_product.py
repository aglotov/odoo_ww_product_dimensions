from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    ww_length = fields.Char(string='Length')
    ww_width = fields.Char(string='Width')
    ww_height = fields.Char(string='Height')
    ww_area = fields.Char(string='Area')
    ww_length_uom_name = fields.Char(string='Length unit of measure label',
                                     compute='_compute_ww_length_uom_name')
    ww_area_uom_name = fields.Char(string='Area unit of measure label',
                                   compute='_compute_ww_area_uom_name')

    @api.model
    def _get_length_uom_name_from_ir_config_parameter(self):
        uom_id = self.env['ir.config_parameter'].sudo().get_param('ww_product_dimensions.length_uom')
        return self.env['uom.uom'].browse(int(uom_id)).display_name

    @api.model
    def _get_area_uom_name_from_ir_config_parameter(self):
        uom_id = self.env['ir.config_parameter'].sudo().get_param('ww_product_dimensions.area_uom')
        return self.env['uom.uom'].browse(int(uom_id)).display_name

    def _compute_ww_length_uom_name(self):
        self.ww_length_uom_name = self._get_length_uom_name_from_ir_config_parameter()

    def _compute_ww_area_uom_name(self):
        self.ww_area_uom_name = self._get_area_uom_name_from_ir_config_parameter()
