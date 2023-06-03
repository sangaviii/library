from odoo import models, fields, api
from odoo.exceptions import UserError


class Customer(models.Model):
    _name = "customer.customer"

    first_name = fields.Char(string="first_Name")
    last_name = fields.Char(string="last_Name")
    name = fields.Char(string="Name")
    image = fields.Image(string='Image')
    status = fields.Selection([
        ('active', 'Active'),
        ('in_active', 'In-Active')],
        'Status',
        default='active')
    gender = fields.Selection([('male', 'Male'), ('female', "Female")], 'Gender')
    customer_id = fields.Char(string='customer_Id')
    age = fields.Integer(string='Age')
    phone_number = fields.Char(string='Phone_number')
    manager_ids = fields.One2many('manager.manager', 'customer_id', string='Manager')

    _sql_constraints = [
        ('customer_id_uniq', 'unique (customer_id)', 'The Customer id must be unique !')
    ]
    dob = fields.Date(string="Date of Birth")
    #
    # def set_dob_cron(self):
    #     if self.dob:
    #         current_date = date.today()
    #         current_year = current_date.year
    #         date_of_birth_year = self.dob.year
    #         # self.search([]).write({'dob': today})
    #         self.age = current_year - date_of_birth_year


    @api.onchange('first_name', 'last_name')
    def onchange_name(self):
        if self.first_name and self.last_name:
            self.name = '%s %s' % (self.first_name, self.last_name)

    @api.constrains('age')
    def _constraints_age(self):
        for record in self:
            if record.age < 18:
                raise UserError("Customer Age must be above 18!")

    def action_books_books(self):
        print('Test')


class ManagerInfo(models.Model):
    _name = 'manager.manager'

    customer_id = fields.Many2one('customer.customer', string='Customer')
    name = fields.Char('Name')
    books_ids = fields.Many2many('books.books', string="Books")
    product_category = fields.Selection([
        ('health', 'Health'),
        ('personal development', 'Personal Development'),
        ('kindle store', 'Kindle Store')],
        'Product_category')
