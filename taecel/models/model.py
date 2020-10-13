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
        

        url                         = 'https://taecel.com/app/api/StatusTXN'
        data_post                   =data_sesion
        #data_post["transID"]        =data_json1["data"]["transID"]

        #data_requests               = requests.post(url, data = data_post)
        #data_requests.raise_for_status()
        #data_json2                  = data_requests.json()
        print("data_json1=",data_json1)

        data_taecel                 ={
    		"name":         vals["name"],
	    	"referencia":   vals["referencia"],
		    "mensaje1":     data_json1["message"],
		    "transID":      data_json1["data"]["transID"],
		    #"folio":        data_json2["data"]["Folio"],
		    #"mensaje2":     data_json2["message"],
		    #"status":       data_json2["data"]["Status"]
        }

        if(data_taecel["transID"]!=""):    
        #if(data_taecel["transID"]!="" and data_taecel["mensaje2"]=="Recarga Exitosa" and data_taecel["status"]=="Exitosa"):
            print("transID==",data_taecel["transID"])
            return super(taecel, self).create(data_taecel)        
