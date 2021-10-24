from odoo import api, fields, models

# this is a class for the hospital patient


class SalesOrder(models.Model):
    _inherit = "sale.order"

    def action_url(self):
        "prepares the link for the customer preview url so he can check his sales order"
        host = "http://localhost:8015/my/orders/"
        id = self.id
        token = "?access_token="+self.access_token
        link = host + str(id) + token
        message = "Dear%20Customer,%0aYour%20Invoice:%20"+self.name+"%20has%20been%20issued.%0aPlease,%20check%20your%20order%20on%20the%20link%20bellow:%0a"+link
        # You can replace the URL with the url of your DB
        return{
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': "https://wa.me/+971528412896?text="+message,
        }
