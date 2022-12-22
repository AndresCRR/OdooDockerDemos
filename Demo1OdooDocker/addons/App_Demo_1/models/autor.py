from odoo import models, fields

#Crear un modelo (tabla de la base de datos) a partir de una clase
class Autor(models.Model):
    _name = 'autor' #Nombre de la tabla

    name= fields.Char(string="Nombre")