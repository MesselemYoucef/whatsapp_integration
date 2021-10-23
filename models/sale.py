from odoo import api, fields, models

# this is a class for the hospital patient


class SalesOrder(models.Model):
    _inherit = "sale.order"

    def action_url(self):

        print("Button_pushed")
        return{
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': "https://www.google.com",
        }
