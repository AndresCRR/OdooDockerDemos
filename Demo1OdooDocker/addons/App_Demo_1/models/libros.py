from odoo import models, fields

#Crear un modelo (tabla de la base de datos) a partir de una clase
class Libros(models.Model):
    _name = 'libros' #Nombre de la tabla

    name = fields.Char(string='Nombre del libro', required=True)
    editorial = fields.Char(string='Editorial', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    autor_id = fields.Many2one(comodel_name='autor', string='Autor', required=True)
    image = fields.Binary(string="Image")
