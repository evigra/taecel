# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

from urllib.parse import urlencode
import pycurl

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
    def create(self,vals):
        print('===========',vals)
        
        crl = pycurl.Curl()
        
        data_sesion = {
            'key':          self.env['ir.config_parameter'].get_param('taecel_key',''),
            'nip':          self.env['ir.config_parameter'].get_param('taecel_nip','')
        }

        data                =data_sesion
        crl.setopt(crl.URL, 'https://taecel.com/app/api/RequestTXN')
        data.producto       =vals["name"]
        data.referencia     =vals["referencia"]
        pf                  =urlencode(data)
        crl.setopt(crl.POSTFIELDS, pf)
        crl.perform()
        
        print("###########################################")
        print("DATA CURL",crl)
        print("DATA CURL",crl.getinfo(crl))    
        print("DATA CURL",crl.getinfo(crl.RESPONSE_CODE))



        crl.close()                

        #return super(taecel, self).create(vals)        
