from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    compliance_doc_required = fields.Boolean(
        string='Compliance Document Required',
        help='When enabled, all outgoing shipments for this customer will require '
             'an explicit compliance document acknowledgment before validation. '
             'If set on a parent company, all child contacts inherit this requirement.',
        default=False,
    )
