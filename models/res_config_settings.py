from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ww_product_length_uom_category = fields.Many2one('uom.category',
                                                     string='Product length UoM category',
                                                     config_parameter='ww_product_dimensions.length_uom_category'
                                                     )
    ww_product_length_uom = fields.Many2one('uom.uom',
                                            string='Product length UoM',
                                            config_parameter='ww_product_dimensions.length_uom',
                                            )
    ww_product_area_uom_category = fields.Many2one('uom.category',
                                                   string='Product area UoM category',
                                                   config_parameter='ww_product_dimensions.area_uom_category'
                                                   )
    ww_product_area_uom = fields.Many2one('uom.uom',
                                          string='Product area UoM',
                                          config_parameter='ww_product_dimensions.area_uom',
                                          )
