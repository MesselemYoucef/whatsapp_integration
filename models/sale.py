from odoo import api, fields, models
from odoo.exceptions import ValidationError
import socket

# this is a class for the hospital patient


class SalesOrder(models.Model):
    _inherit = "sale.order"

    @api.constrains("partner_id.mobile")
    def action_url(self):
        "prepares the link for the customer preview url so he can check his sales order"
        hostname = socket.gethostname()
        domain_name = socket.gethostbyname(hostname)
        host = f"http://{domain_name}:8015/my/orders/"
        token = "?access_token="+self.access_token
        link = host + str(id) + token
        print(self.partner_id.mobile)
        message = "Dear%20Customer,%0aYour%20Invoice:%20"+self.name+"%20has%20been%20issued.%0aPlease,%20check%20your%20order%20on%20the%20link%20bellow:%0a"+link
        # You can replace the URL with the url of your DB
        for record in self:
            if not record.partner_id.mobile:
                raise ValidationError("This customer has no number on the system, please update his number before sending whatsapp")
        return{
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': "https://wa.me/"+self.partner_id.mobile+"?text="+message,
        }
