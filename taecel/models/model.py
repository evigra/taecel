# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

from urllib.parse import urlencode
import pycurl
import json

class taecel(models.Model):
    _name = "taecel"
    _description = 'TAECEL'
    _order = "time DESC"
    name                                        = fields.Char('Producto', size=15)
    referencia                                  = fields.Char('referencia', size=150)
    mensaje1                                    = fields.Char('mensaje1', size=150)
    transID                                     = fields.Char('transID', size=50)
    folio                                       = fields.Char('folio', size=50)
    mensaje2                                    = fields.Char('mensaje2', size=150)
    status                                      = fields.Char('status', size=150)
    time                                        = fields.Datetime('Time')

    def create(self,vals):
        data_taecel                 ={
    		"name":         vals["name"],
        	"referencia":   vals["referencia"],
            "status":       "Error"
        }

        data_sesion = {
            'key':          self.env['ir.config_parameter'].get_param('taecel_key',''),
            'nip':          self.env['ir.config_parameter'].get_param('taecel_nip','')
        }
                
        url                         = 'https://taecel.com/app/api/RequestTXN'
        data_post                   =data_sesion
        data_post["producto"]       =vals["name"]
        data_post["referencia"]     =vals["referencia"]

        data_requests               = requests.post(url, data = data_post)
        data_requests.raise_for_status()
        data_json1                  = data_requests.json()
        
        if("data" in data_json1):
            data_taecel["mensaje1"]     =data_json1["message"]
        
            url                         = 'https://taecel.com/app/api/StatusTXN'
            data_post                   =data_sesion
            data                        =data_json1["data"]
            if("transID" in data):        
                data_post["transID"]        =data["transID"]
                data_requests               = requests.post(url, data = data_post)
                data_requests.raise_for_status()
                data_json2                  = data_requests.json()
                if("data" in data_json2):        
                    data                        =data_json2["data"]
                    if("Status" in data):
                        data_taecel["transID"]      =data_post["transID"]		   
                        data_taecel["folio"]        =data["Folio"]
                        data_taecel["mensaje2"]     =data_json2["message"]
                        data_taecel["status"]       =data["Status"]
                    
        return super(taecel, self).create(data_taecel)                    
                                
