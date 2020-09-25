# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Website(models.Model):
    _inherit = 'website'
    
    pixel_code = fields.Char(string="Facebook Pixel Code")
