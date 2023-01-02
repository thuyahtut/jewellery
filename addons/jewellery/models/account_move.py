from odoo import _, api, fields, models, tools

class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_starting_sequence(self):
        # EXTENDS account sequence.mixin
        self.ensure_one()
        is_payment = self.payment_id or self._context.get('is_payment')
        if self.journal_id.type in ['bank', 'cash']:
            starting_sequence = "%s/%04d/00000" % (self.journal_id.code, self.date.year)
        else:
            starting_sequence = "%s/%04d/%02d/0000" % (self.journal_id.code, self.date.year, self.date.month)
        
        if self.journal_id.type == "sale":
            # starting_sequence = "%s/%04d/00000" % (self.journal_id.code, self.date.year)
            seq = self.env['ir.sequence'].search([('code', '=', 'account.move')])
            if not seq:
                starting_sequence = "%s/%04d/00000" % (self.journal_id.code, self.date.year)
            else:
                starting_sequence = seq.get_next_char(seq.number_next_actual)
            

        if self.journal_id.refund_sequence and self.move_type in ('out_refund', 'in_refund'):
            starting_sequence = "R" + starting_sequence
        if self.journal_id.payment_sequence and is_payment:
            starting_sequence = "P" + starting_sequence
        return starting_sequence
