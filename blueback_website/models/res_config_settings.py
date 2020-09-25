# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.depends("website_id")
    def has_pixel_code(self):
        self.has_pixel_code = bool(self.pixel_code)

    def inverse_has_pixel_code(self):
        if not self.has_pixel_code:
            self.pixel_code = False

    has_pixel_code = fields.Boolean("Facebook Pixel", compute=has_pixel_code, inverse=inverse_has_pixel_code)
    pixel_code = fields.Char("Facebook Pixel Code", related='website_id.pixel_code', readonly=False)

