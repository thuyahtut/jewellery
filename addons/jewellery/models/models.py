# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.fields import Command

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

    default_code = fields.Text(string='Internal Reference')
    

class SaleAdvancePaymentInvInherit(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    def _prepare_down_payment_product_values(self):
        self.ensure_one()
        data =  {
            'name': _('Down payment'),
            'type': 'service',
            'invoice_policy': 'order',
            'company_id': False,
            'uom_id': self.env.ref('uom.product_uom_unit').id,
            'uom_po_id': self.env.ref('uom.product_uom_unit').id,
            'property_account_income_id': self.deposit_account_id.id,
            'taxes_id': [Command.set(self.deposit_taxes_id.ids)],
        }
        return data








