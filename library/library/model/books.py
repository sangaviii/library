from odoo import models, fields

class Books(models.Model):
    _name = "books.books"

    image = fields.Image(string='Image')
    name = fields.Char(string='books Name')
    sales_price = fields.Char(string="Sales price")
    checkin_date = fields.Date(string='checkin Date')
    checkout_date = fields.Date(string='checkout Date')







