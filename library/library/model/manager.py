from odoo import models, fields

class Salesmanager(models.Model):
    _name = "sales.manager"

    image = fields.Image(string='Image')
    name = fields.Char(string='Name')
    phone = fields.Char(string='phone')
