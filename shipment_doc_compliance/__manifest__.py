{
    'name': 'Pre-Shipment Document Compliance',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Warehouse',
    'summary': 'Enforce document compliance on outgoing shipments before validation.',
    'description': """
Pre-Shipment Document Compliance for Odoo
==========================================

Prevents warehouse staff from validating an outgoing shipment without explicitly
confirming that required compliance documents (invoices, certifications, customs
declarations, SDS sheets, etc.) are included.

Three enforcement layers:
1. Visual alert banner on the Ship transfer form
2. Mandatory acknowledgment checkbox that blocks Validate
3. Automated post-validation notification (chatter + email) for audit trail

Configurable per operation type or per customer/contact.
Parent company flag inheritance supported.

For Odoo.sh and self-hosted Odoo 18 only.
    """,
    'author': 'AMADIO',
    'website': 'https://amadio.io',
    'license': 'LGPL-3',
    'depends': [
        'stock',
        'sale_stock',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template_data.xml',
        'views/stock_picking_views.xml',
        'views/res_partner_views.xml',
        'views/stock_operation_type_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 73.00,
    'currency': 'EUR',
}
