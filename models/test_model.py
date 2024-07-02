# models/test_model.py

from odoo import models, fields


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Test Model'

    name = fields.Char(string='Name', required=True)
