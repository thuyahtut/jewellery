# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JewelPieces(models.Model):
    _name = 'jewel.pieces'
    _description = 'The records for pieces of jewel.'

    name = fields.Char(string='Name')
    quantity = fields.Float(string='Quantity', digits='Product Unit of Measure')
    template_id = fields.Many2one('product.template',string='Template ID')



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    total_weight = fields.Float(string='Total Weight', digits='Product Unit of Measure')
    diamond_weight = fields.Float(string='Diamond Weight', digits='Product Unit of Measure')
    jewel_pieces_ids = fields.One2many('jewel.pieces', 'template_id', string='Jewel Pieces')
    

