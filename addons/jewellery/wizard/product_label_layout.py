
from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError

class ProductLabelLayoutInherit(models.TransientModel):
    _inherit = 'product.label.layout'


    def process(self):
        self.ensure_one()
        xml_id, data = self._prepare_report_data()
        if not xml_id:
            raise UserError(_('Unable to find report template for %s format', self.print_format))
        report_action = self.env.ref(xml_id).report_action(None, data=data)
        report_action.update({'close_on_report_download': True})
        
        report_action['report_type'] = 'qweb-html'
        import json
        json_formatted_str = json.dumps(report_action, indent=2)
        print("report_action===>", json_formatted_str)
        return report_action