from odoo import api, fields, models


class CreateMessage(models.TransientModel):
    _name="partner.message"
    _description = "Compose a message to the partner"

    name = fields.Char(string="Person Number", required=True, tracking=True)

