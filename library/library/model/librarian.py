from odoo import models, fields

class Librarian(models.Model):
    _name = "librarian.librarian"

    image = fields.Image(string='Image')
    name = fields.Char(string='Name')
    phone = fields.Char(string='phone')
    user_id = fields.Integer(string="User_Id")


