from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    compliance_doc_required = fields.Boolean(
        string='Compliance Document Required',
        compute='_compute_compliance_doc_required',
        store=True,
        help='Computed from customer record (or parent company) and operation type.',
    )

    compliance_doc_confirmed = fields.Boolean(
        string='I confirm the compliance document is included in this shipment',
        default=False,
        copy=False,
        help='Must be ticked before this shipment can be validated.',
    )

    @api.depends(
        'partner_id', 'partner_id.compliance_doc_required',
        'partner_id.parent_id', 'partner_id.parent_id.compliance_doc_required',
        'picking_type_id', 'picking_type_id.compliance_doc_required',
    )
    def _compute_compliance_doc_required(self):
        for picking in self:
            partner = picking.partner_id
            partner_flag = (
                (partner.compliance_doc_required if partner else False)
                or (partner.parent_id.compliance_doc_required if partner and partner.parent_id else False)
            )
            op_type_flag = picking.picking_type_id.compliance_doc_required if picking.picking_type_id else False
            picking.compliance_doc_required = partner_flag or op_type_flag

    def button_validate(self):
        for picking in self:
            if (
                picking.compliance_doc_required
                and not picking.compliance_doc_confirmed
                and picking.state not in ('done', 'cancel')
            ):
                raise UserError(_(
                    'Compliance document confirmation required.\n\n'
                    'Please confirm that the required document is included by ticking '
                    'the compliance acknowledgment checkbox before validating.'
                ))
        return super().button_validate()

    def _action_done(self):
        result = super()._action_done()
        for picking in self.filtered(lambda p: p.compliance_doc_required and p.compliance_doc_confirmed):
            picking._post_compliance_notification()
        return result

    def _post_compliance_notification(self):
        self.ensure_one()
        template = self.env.ref('shipment_doc_compliance.mail_template_compliance_confirmed', raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=False)
        self.message_post(
            body=_('<b>Compliance Document Confirmed</b><br/>Shipment <b>%(name)s</b> validated with compliance confirmed by %(user)s.', name=self.name, user=self.env.user.name),
            message_type='comment',
            subtype_xmlid='mail.mt_note',
        )
