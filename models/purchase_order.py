from odoo import fields, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_approve_permit = fields.Boolean()
    state = fields.Selection(
        selection_add=[
            ("waiting_approval", "Waiting Approval"),
            ("approved", "Approved"),
            ("rejected", "Rejected")
        ], default="draft"
    )

    def action_approval_rqst(self):
        for rec in self:
            rec.state = "waiting_approval"
            is_approve = rec.env["ir.config_parameter"].get_param("approve")
            if is_approve:
                rec.is_approve_permit = True
            else:
                rec.is_approve_permit = False

    def action_approve(self):
        for rec in self:
            rec.state = "approved"

    def action_reject(self):
        for rec in self:
            rec.state = "rejected"
            # raise UserError("Request is Rejected")

