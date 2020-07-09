# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

class taecel(models.Model):
    _name = "taecel"
    _description = 'TAECEL'
    _order = "time DESC"
    name                                        = fields.Char('Producto', size=15)
    referencia                                  = fields.Char('referencia', size=150)
    mensaje1                                    = fields.Char('mensaje1', size=150)
    transID                                     = fields.Integer('transID')
    folio                                       = fields.Integer('folio')
    mensaje2                                    = fields.Char('mensaje2', size=150)
    status                                      = fields.Char('status', size=150)
    time                                        = fields.Datetime('Time')
    def get_system_para(self):
        para_value                              =self.env['ir.config_parameter'].get_param('solesgps_map_key','')
        return para_value
