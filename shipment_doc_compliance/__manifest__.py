{
    'name': 'Pre-Shipment Document Compliance',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Warehouse',
    'summary': 'Block outgoing shipment validation until required compliance documents are confirmed. Enforces customs declarations, SDS sheets, invoices, and certifications with a mandatory acknowledgment checkpoint and full audit trail.',
    'description': """
Pre-Shipment Document Compliance for Odoo 18
=============================================

Stop non-compliant shipments before they leave your warehouse.

This module enforces a mandatory document compliance checkpoint on all outgoing
stock pickings (or specific operation types) before warehouse staff can validate
a delivery. Used by exporters, chemical distributors, medical device companies,
B2B wholesalers, and 3PLs who must ensure required documents accompany every shipment.

Key Features
------------
- Visual compliance alert banner on the stock picking form
- Mandatory acknowledgment checkbox that hard-blocks the Validate button
- Automated post-validation chatter note + email notification for audit trail
- Per-operation-type configuration (apply only where needed)
- Per-customer/contact compliance flag with parent company inheritance
- Zero schema overhaul -- installs in under 2 minutes

Document Types Supported
------------------------
Commercial invoices, customs declarations, certificates of origin,
SDS (Safety Data Sheets), hazmat declarations, quality certificates,
packing lists, inspection reports, and any other shipment documentation.

Use Cases
---------
- Export compliance and customs documentation control
- Hazardous goods (WHMIS / GHS) SDS sheet enforcement
- Pharmaceutical and medical device shipment documentation
- B2B key account special document requirements
- ISO/regulatory audit trail for outbound logistics
- 3PL client-specific documentation workflows

Technical
---------
Odoo 18.0 | On-Premise and Odoo.sh | LGPL-3
Depends: stock, sale_stock, mail
148 lines of code | Non-invasive installation
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
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 73.00,
    'currency': 'EUR',
}
