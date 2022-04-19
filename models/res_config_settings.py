from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ww_product_dimensions_uom_category = fields.Many2one('uom.category',
                                                         string='Product dimensions UOM category',
                                                         config_parameter='ww_product_dimensions.uom_category'
                                                         )
    ww_product_dimensions_uom = fields.Many2one('uom.uom',
                                                string='Product dimensions UOM',
                                                config_parameter='ww_product_dimensions.uom'
                                                )
