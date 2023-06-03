from odoo import _, models, fields, api


class Member(models.Model):
    _name = "member.member"

    first_name = fields.Char(string="first_Name")
    last_name = fields.Char(string="last_Name")
    member_name = fields.Char(string="Name")
    image = fields.Image(string='Image')
    status = fields.Selection([
        ('active', 'Active'),
        ('in_active', 'In-Active')],
        'Status',
        default='active')
    gender = fields.Selection([('male', 'Male'), ('female', "Female")], 'Gender')
    member_id = fields.Char(string='member_Id')
    age = fields.Integer(string="Age")
    phone_number = fields.Char(string="Phone_number")

    # member_ids = fields.One2many('librarian.librarian', 'librarian_id', string='Member')

    @api.onchange('first_name', 'last_name')
    def onchange_name(self):
        if self.first_name and self.last_name:
            self.member_name = '%s %s' % (self.first_name, self.last_name)
