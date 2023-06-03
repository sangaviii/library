from odoo import models, fields


class PaymentWizard(models.Model):
    _name = 'payment.payment'
    _description = 'Payment'

    amount = fields.Float(string='Amount')
    membership_no = fields.Integer(string="Membership No")
    payment_method = fields.Selection([
       ('phone_pe', 'Phone pe'),
       ('upi', 'UPI'),
       ('account_transfer', 'Account Transfer')], 'Payment Method')
    book_code = fields.Integer(string='Book code')
    date = fields.Date(string='Date')
    books_ids = fields.Many2many('books.books',string='Book')
    checkin_date = fields.Date(string='checkin_Date')
    checkout_date = fields.Date(string='checkout_Date')

    # def print_report(self):
    #     data = {
    #         'checkin_date': self.checkin_date,
    #         'checkout_date': self.checkout_date,
    #     }
    #     print('ssssss',data)
    #     return self.env.ref('library.action_report_books').report_action(self, data=data)

    
    def print_book(self):
        data = {
            'books_ids': self.books_ids.ids,
            'checkin_date': self.checkin_date,
            'checkout_date': self.checkout_date,
        }
        return self.env.ref('library.action_report_books').report_action(self, data=data)

    def create_payments(self):
        customer_id = self.env.context.get('active_id')
        print('sssssss', customer_id)
        payment = self.env['payment.details'].create({
            'membership_no': self.membership_no,
            'amount': self.amount,
            'payment_method':self.payment_method,
            'book_code':self.book_code,
            'date':self.date,
        })



    # def print_report(self):
    #     data = {
    #         'model':'payment.details',
    #         'from':self.read()[0]
    #     }
    #     return self.env.ref('library_report').report.action(self,data=data)
