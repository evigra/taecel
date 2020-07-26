# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

from urllib.parse import urlencode
import pycurl

class product_template(models.Model):
    _inherit = "product.template"

    def getProducts(self):
        crl = pycurl.Curl()
        crl.setopt(crl.URL, 'https://taecel.com/app/api/getProducts')

        crl.perform()

        print("#######",c.getinfo(pycurl))

        

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
        taecel_key                              =self.env['ir.config_parameter'].get_param('taecel_key','')
        taecel_nip                              =self.env['ir.config_parameter'].get_param('taecel_nip','')
        
        crl = pycurl.Curl()
        crl.setopt(crl.URL, 'https://taecel.com/app/api/RequestTXN')
        data = {
            'key':          taecel_key,
            'nip':          taecel_nip,
            'producto':     vals["name"],
            'referencia':   vals["referencia"],
        }
        pf = urlencode(data)


        """
        crl.setopt(crl.POSTFIELDS, pf)
        crl.perform()

        print("#######",c.getinfo(pycurl))
            
        c = pycurl.Curl()
        c.setopt(pycurl.OPT_CERTINFO, 1)
        
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.perform()
        print(c.getinfo(pycurl.HTTP_CODE))
        print(c.getinfo(pycurl.EFFECTIVE_URL))
        
        certinfo = c.getinfo(pycurl.INFO_CERTINFO)
        print(certinfo)        
        
        """
        
                
        
        
        crl.close()                
        
        

        return super(taecel, self).create(vals)
        
