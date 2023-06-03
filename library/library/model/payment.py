from odoo import models, fields


class Payment(models.Model):
    _name = 'payment.details'

    membership_no = fields.Integer(string="Membership No")
    book_code = fields.Integer(string='Book code')
    date = fields.Date(string='Date')
    amount = fields.Float(string='Amount')

    payment_method = fields.Selection([
        ('phone_pe', 'Phone pe'),
        ('upi', 'UPI'),
        ('account_transfer', 'Account Transfer')], 'Payment Method'
    )
