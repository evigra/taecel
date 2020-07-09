# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Taecel',
    'price' : '45.0',
    'currency' : 'EUR',
    'images': ['static/description/map_online.png'],    
    'author': "SolesGPS :: Eduardo Vizcaino",
    'category': 'fleet, GPS, Geolocation',
    'website' : 'https://solesgps.com',
    'summary' : 'Locate the satellite coordinates that your GPS devices throw. Save that information here and see it on the map.',
    'description' : """
Vehicle, leasing, insurances, cost
==================================
With this module, Odoo helps you managing all your vehicles, the
contracts associated to those vehicle as well as services, fuel log
entries, costs and many other features necessary to the management 
of your fleet of vehicle(s)

Main Features
-------------
* Add vehicles to your fleet
* Manage contracts for vehicles
* Reminder when a contract reach its expiration date
* Add services, fuel log entry, odometer values for all vehicles
* Show all costs associated to a vehicle or to a type of service
* Analysis graph for costs
""",
    'depends': [
        #'fleet',
    ],
    'data': [
        #'security/solesgpsmap_security.xml',
        #'security/ir.model.access.csv',
        'data/data.xml',
        #'views/solesgpsmap_menuitem.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
