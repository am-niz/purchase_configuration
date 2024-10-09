from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    approve = fields.Boolean(string="Approve")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].set_param("approve", self.approve)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res["approve"] = self.env["ir.config_parameter"].get_param("approve")
        return res
