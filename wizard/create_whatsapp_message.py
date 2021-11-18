from odoo import api, fields, models


class CreateMessageWizard(models.TransientModel):
    _name = "partner.message.wizard"
    _description = "Compose a message to the partner"

    phone_number = fields.Char(string="Phone Number", required=True)

