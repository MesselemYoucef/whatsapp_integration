from odoo import api, fields, models


class PartnerWhatsapp(models.Model):
    _inherit = "res.partner"

    def _action_clicked(self):

        print("The button has been clicked")
        return {}
