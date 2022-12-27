
from dateutil.relativedelta import relativedelta
from odoo import models, fields

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())


class estate_property(models.Model):
    _name = 'estate_property.model'
    _description = 'ejercicio de odoo'

    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From',default=lambda self: fields.Date.today()+ relativedelta(months=3))
    expected_price = fields.Float(string='Expected price',required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection([('N','North'),('S','South'),('E','East'),('W','West')], string='Garden Orientation')
    state = fields.Selection([('n','New'),('OfA','Offert Acepted'),('OfR','Offert Recived'),('S','Sold'),('C','Canceled')], string='Status')
    active = fields.Boolean(string='Active')


