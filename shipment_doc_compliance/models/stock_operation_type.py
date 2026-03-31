from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    compliance_doc_required = fields.Boolean(
        string='Compliance Document Required',
        help='When enabled, ALL outgoing shipments of this operation type will require '
             'a compliance document acknowledgment before validation, regardless of '
             'the customer setting. Use this to enforce compliance on all shipments '
             'of a given type (e.g., all Delivery Orders).',
        default=False,
    )
