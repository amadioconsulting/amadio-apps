import os

MODULES = {
    "inventory_location_validation": {
        "name": "Real-Time Inventory Location Validation",
        "tagline": "Prevent stock from landing in the wrong bin — enforce location rules before the warehouse error becomes an inventory crisis.",
        "badges": ["Warn or Block Mode", "Category-Based Rules", "Override Wizard", "Zero Training Required"],
        "problems": [
            ("Misrouted Products", "Cold-chain items land in ambient storage. Hazardous materials go to the wrong zone. Valuable stock ends up in a bulk bin. Odoo's default validation says nothing."),
            ("Phantom Inventory Discrepancies", "Products placed in wrong locations create cycle-count nightmares — stock that exists but can't be found where the system says it is."),
            ("Reactive Firefighting", "Warehouse managers discover errors hours or days later. By then, the product has been picked, packed, or further moved — compounding the original mistake.")
        ],
        "features": [
            ("📍", "Category-Based Location Rules", "Define which product categories are permitted in which storage locations. Rules are checked at the moment of shipment validation — before any error is committed."),
            ("⚠️", "Warn or Block Mode", "Choose per-rule: warn the warehouse operator with a pop-up (they can proceed) or hard-block validation entirely until the location is corrected."),
            ("🧙", "Override Wizard", "Authorized managers can override a blocked validation with a reason code. Every override is logged for audit purposes."),
            ("📦", "Works on All Picking Types", "Receipts, internal transfers, delivery orders, and manufacturing moves — any stock.picking operation can have location rules applied."),
            ("🔧", "Zero Training Required", "Rules are enforced automatically. Warehouse staff see clear, plain-language messages. No manual checklist, no supervisor required."),
            ("📊", "Violation Log", "Every blocked or warned validation is recorded with timestamp, user, product, and intended location — giving you a clean audit trail.")
        ],
        "steps": [
            ("Configure Rules", "Navigate to Inventory → Configuration → Location Rules. Create rules linking product categories to permitted locations. Set warn or block mode per rule."),
            ("Business as Usual", "Warehouse staff process transfers normally. The system checks rules in the background at the moment of validation — no extra steps required."),
            ("Instant Feedback", "When a violation is detected, the operator sees a clear message identifying the product and correct location. Managers can override with a reason if needed.")
        ],
        "use_cases": [
            ("🏭", "Cold-Chain Warehouses", "Ensure refrigerated products never land in ambient zones. Enforce temperature-zone rules automatically across all receiving operations."),
            ("⚗️", "Hazmat Distributors", "Keep dangerous goods in compliant storage areas. Prevent accidental placement in general-population bins — critical for regulatory audits."),
            ("🏪", "Multi-Category 3PLs", "Third-party logistics providers managing client inventory can enforce client-specific storage rules without staff needing to memorize them.")
        ],
        "accent": "#e67e22"
    },
    "shipment_doc_compliance": {
        "name": "Pre-Shipment Document Compliance Checker",
        "tagline": "Ensure every shipment leaves with the right paperwork — BOL, packing list, COA, and more — before your dock doors open.",
        "badges": ["Per-Category Requirements", "Red/Green Status", "Blocks Validation", "Audit Ready"],
        "problems": [
            ("Missing Documents at Dispatch", "A shipment leaves without its Certificate of Analysis. The customer receives product they cannot accept. Returns, claims, and relationship damage follow."),
            ("Manual Checklist Fatigue", "Shipping coordinators maintain paper checklists that get skipped when it's busy. Documents are assumed to be attached — until they aren't."),
            ("Regulatory Exposure", "Cross-border shipments missing customs documentation can be seized. Food and pharma shipments without COAs violate compliance requirements.")
        ],
        "features": [
            ("📋", "Per-Category Document Requirements", "Define which document types are required for each product category — Bill of Lading for all, COA only for food-grade, MSDS for chemicals."),
            ("🔴", "Red/Green Compliance Status", "The picking form shows a live compliance indicator: green when all required documents are attached, red with specific missing items listed."),
            ("🚫", "Validation Blocking", "Configure the system to hard-block shipment validation until all required documents are present. No more partial compliance."),
            ("📎", "Native Attachment Integration", "Works with Odoo's built-in attachment system. Staff attach documents the way they already do — the checker verifies they're present and correctly tagged."),
            ("📁", "Document Type Taxonomy", "Maintain a clean taxonomy of document types (BOL, Packing List, COA, MSDS, Invoice, Certificate of Origin) reused across all rules."),
            ("🗒️", "Compliance Audit Log", "Every shipment's compliance status at validation is recorded — which documents were present, who validated, and when.")
        ],
        "steps": [
            ("Define Document Rules", "Go to Inventory → Configuration → Document Requirements. Create rules per product category specifying which document types are mandatory."),
            ("Attach Documents to Picks", "Shipping staff attach documents to the picking record as they normally would — PDF, scan, or generated document — tagged with the document type."),
            ("Validate with Confidence", "The compliance checker runs automatically at validation. Missing documents are listed. Validation is blocked (or warned) until the shipment is complete.")
        ],
        "use_cases": [
            ("🌍", "International Freight", "Exporters and freight forwarders ensure every cross-border shipment carries the documentation required by customs at origin and destination."),
            ("🧪", "Food & Pharma Distribution", "COAs, lot traceability documents, and temperature records are mandatory before product leaves the facility — enforced automatically."),
            ("🏗️", "Industrial Suppliers", "Heavy equipment and specialized components require safety data sheets and installation manuals. Ensure they're never shipped without them.")
        ],
        "accent": "#2ecc71"
    },
    "bank_deposit_prep": {
        "name": "Bank Deposit Preparation & Slip Generator",
        "tagline": "Aggregate cheques, cash, and EFT receipts into a single bank deposit record — then print a professional deposit slip in one click.",
        "badges": ["Sequential References", "PDF Deposit Slip", "Links to Payments", "Multi-Tender"],
        "problems": [
            ("Manual Deposit Reconciliation", "Accounting staff manually tally cheques, cash, and EFT receipts into a spreadsheet before going to the bank. Errors are common and reconciliation takes hours."),
            ("No Audit Trail", "Without a formal deposit record, it's impossible to quickly answer: which payments went in which deposit, who prepared it, and when was it confirmed by the bank."),
            ("Paper-Based Slip Creation", "Deposit slips are handwritten or typed in Word. They're inconsistent, unprofessional, and don't link back to the source payments in Odoo.")
        ],
        "features": [
            ("🏦", "Deposit Record with Sequential Reference", "Each deposit gets a unique reference (DEP/YYYY/#####) with date, journal, preparer, and state (Draft → Prepared → Deposited → Confirmed)."),
            ("💵", "Multi-Tender Line Items", "Add cheque, cash, EFT, and other payment types as individual lines with payer name, cheque number, and amount. Totals compute automatically."),
            ("🔗", "Link to Existing Payments", "Import outstanding account.payment records directly into the deposit with one click — no duplicate data entry."),
            ("📄", "Professional PDF Slip", "Print a formatted deposit slip with all lines, totals by tender type, bank details, and signature lines — ready to hand to the teller."),
            ("🏢", "Company Bank Details", "Configure your institution name, transit number, and account number in company settings. They appear on every deposit slip automatically."),
            ("✅", "Duplicate Safeguard", "The system prevents the same payment from being included in two different deposits — protecting deposit integrity automatically.")
        ],
        "steps": [
            ("Create a New Deposit", "Go to Accounting → Bank Deposits → New. Set the date and journal. Import outstanding payments or add lines manually for walk-in receipts."),
            ("Review and Prepare", "Verify all lines — cheques, cash, EFTs. The system calculates totals by tender type. Click Prepare to lock the deposit."),
            ("Print and Go", "Click Print Deposit Slip for a PDF formatted for your bank. Take it to the teller. Mark as Deposited when done, then Confirmed when it clears.")
        ],
        "use_cases": [
            ("⛪", "Nonprofits & Churches", "Organizations receiving weekly cash collections and cheque donations can prepare structured deposits with a full audit trail per deposit event."),
            ("🏥", "Healthcare Practices", "Medical offices collecting co-pays, insurance cheques, and cash payments need a clean deposit record linking each receipt to the correct payment."),
            ("🏪", "Retail & Service Businesses", "Any business with daily or weekly bank runs benefits from structured deposit preparation that links directly to Odoo's accounting module.")
        ],
        "accent": "#3498db"
    },
    "smart_mail_template": {
        "name": "Smart Email Template Selector",
        "tagline": "Surface the right email template at the right moment — the Odoo mail composer now surfaces your top 5 most relevant templates, ranked by context.",
        "badges": ["Context-Aware Ranking", "Usage Learning", "Stage-Sensitive", "Works Everywhere"],
        "problems": [
            ("Template Overload", "Organizations with dozens of email templates find staff scrolling through an unordered list every time they compose. The right template gets buried under noise."),
            ("Wrong Templates Sent", "Without context-aware surfacing, users grab the nearest template that looks right — leading to wrong salutations, wrong products, wrong calls to action."),
            ("No Learning from Usage", "Standard Odoo doesn't track which templates work best in which contexts. Every user starts from scratch each time.")
        ],
        "features": [
            ("🧠", "Context-Aware Ranking", "When opening the mail composer, the system evaluates the current model (sale.order, crm.lead, etc.) and stage to rank templates by relevance."),
            ("📈", "Usage Learning Engine", "Each time a template is selected, the usage count updates. Popular templates in each context automatically rise to the top over time."),
            ("🎯", "Stage-Sensitive Suggestions", "A template rule can specify that certain templates only surface when a record is at a particular stage — e.g., follow-up templates only appear when a lead is in 'Qualified'."),
            ("⚡", "One-Click Selection", "Top 5 relevant templates appear immediately when the composer opens — no searching, no scrolling. Click to apply."),
            ("🔧", "Admin-Configurable Rules", "IT or power users can create smart.mail.template.rule records to fine-tune which templates surface for which models and stages."),
            ("📧", "Works Across All Models", "Sales orders, CRM leads, purchase orders, invoices, helpdesk tickets — any model that uses the Odoo mail composer benefits automatically.")
        ],
        "steps": [
            ("Configure Template Rules", "In Email → Smart Template Rules, define which templates are relevant for which models and stages. Set a priority weight for initial ranking."),
            ("Compose as Normal", "Open the mail composer on any record. Your top 5 relevant templates appear instantly in the suggestion panel — no searching required."),
            ("System Learns Over Time", "As users select templates, the usage tracking updates. The most-used templates in each context automatically rank higher for the whole team.")
        ],
        "use_cases": [
            ("💼", "Sales Teams", "Reps composing outreach, follow-up, and proposal emails always see the right template for the deal stage — without hunting through a library of 50+ templates."),
            ("🎧", "Customer Support", "Support agents see templates relevant to the ticket type and current status — resolution templates, escalation notices, and satisfaction surveys surface at the right moment."),
            ("📦", "Operations Teams", "Purchasing, logistics, and AR teams sending supplier confirmations, shipping notices, and overdue payment reminders always get the right starting point.")
        ],
        "accent": "#9b59b6"
    },
    "warehouse_pick_optimizer": {
        "name": "Warehouse Pick Path Optimizer",
        "tagline": "Reorder pick lines by physical bin sequence and print an optimized pick list — cut picker travel distance by 30–50% with zero process change.",
        "badges": ["Bin-Sequence Ordering", "Optimized PDF Pick List", "One-Click Optimize", "No WMS Required"],
        "problems": [
            ("Zigzag Pick Routes", "Odoo generates pick lists in sales order sequence — not warehouse geography. Pickers travel back and forth across the warehouse, wasting 20–40% of their time."),
            ("No Pick List Printing", "Standard Odoo has no formatted pick list document. Staff read off screens or print unformatted system reports."),
            ("WMS Cost Barrier", "Full warehouse management systems with path optimization cost tens of thousands of dollars. Mid-market warehouses need this capability without the price tag.")
        ],
        "features": [
            ("🗺️", "Bin Sequence Ordering", "Assign a pick_sequence number to each stock location. The optimizer reorders pick lines by this sequence — creating a logical aisle-by-aisle route."),
            ("🖨️", "Professional Pick List PDF", "Print a formatted pick list sorted by bin sequence, with product name, reference, lot/serial if applicable, and quantity — designed for actual warehouse use."),
            ("⚡", "One-Click Optimization", "An Optimize button on the picking form reorders all move lines by bin sequence in a single click. No configuration required per pick."),
            ("📍", "Location-Level Configuration", "Bin sequences are set once on the stock.location record. Every pick that includes that location automatically benefits — nothing to configure per order."),
            ("🔄", "Works with Existing Operations", "No change to receiving, putaway, or validation workflow. The optimizer is additive — add it to any existing operation type."),
            ("📊", "Multi-Product Batch Ready", "Works with batch transfers and cluster picks. Optimize an entire batch by bin sequence to minimize picker travel across multiple orders simultaneously.")
        ],
        "steps": [
            ("Set Bin Sequences", "Go to Inventory → Configuration → Locations. Set the pick_sequence field on each storage location (e.g., Aisle 1 Bin A = 10, Aisle 1 Bin B = 20, Aisle 2 = 100)."),
            ("Confirm Your Picking", "Process pickings as normal. When ready to pick, click the Optimize Pick Order button to reorder all lines by bin sequence in one click."),
            ("Print and Pick", "Click Print Pick List for a professional, bin-sequenced PDF. Hand it to the picker. They walk a logical route — no backtracking, no wasted steps.")
        ],
        "use_cases": [
            ("🏭", "E-Commerce Fulfillment", "Warehouse operations fulfilling hundreds of daily orders gain massive efficiency from optimized pick paths — without implementing a full WMS."),
            ("🛒", "Wholesale Distributors", "Distributors picking multi-line orders for B2B customers reduce labor costs and improve same-day shipping rates with optimized pick sequences."),
            ("🏗️", "Manufacturing Stores", "Production stores picking components for work orders reduce walk time and ensure the right parts arrive at the right workstation at the right time.")
        ],
        "accent": "#1abc9c"
    },
    "budget_line_alert": {
        "name": "Analytic Budget Alert & Variance Monitor",
        "tagline": "Set spend limits on analytic accounts and receive automatic alerts before budgets are breached — with hard blocks when you need them.",
        "badges": ["Warn & Block Thresholds", "Email Alerts", "Live Variance", "Per-Account Config"],
        "problems": [
            ("Surprise Budget Overruns", "Finance teams discover budget overruns at month-end when reconciling — too late to course-correct. The spending happened weeks ago."),
            ("No Granular Controls", "Standard Odoo budget features apply broadly. Organizations need per-project, per-department, or per-cost-center budget controls that trigger in real time."),
            ("Manual Monitoring", "Budget managers export reports and compare to budgets manually. By the time they flag an issue, the next overspending entry has already posted.")
        ],
        "features": [
            ("⚠️", "Configurable Warn Threshold", "Set a percentage (default 80%) at which an email alert fires to designated stakeholders — early warning before the budget is actually exceeded."),
            ("🚫", "Hard Block Threshold", "Set a block percentage (default 100%) at which journal entry posting is refused. Accounting cannot post entries that would breach the configured limit."),
            ("📊", "Live Variance Dashboard", "Each analytic account shows real-time budget spent, remaining, and percentage consumed — directly on the account form, no report required."),
            ("📧", "Stakeholder Email Alerts", "Configure any number of internal contacts to receive budget alert emails. Emails include account name, current spend, budget limit, and percentage consumed."),
            ("📅", "Flexible Budget Periods", "Set budgets by month, quarter, year, or custom date range. The system resets automatically at the start of each period."),
            ("🔧", "Per-Account Configuration", "Every analytic account can have its own budget amount, warn threshold, block threshold, and alert contacts — independent of other accounts.")
        ],
        "steps": [
            ("Configure Your Budget", "On any analytic account, enable the budget feature, set the budget amount, choose the period, and configure your warn and block percentages."),
            ("Post Journal Entries Normally", "Accounting staff post journal entries as they normally would. The system monitors cumulative spend against the budget in real time."),
            ("Alerts Fire Automatically", "When spend crosses the warn threshold, designated stakeholders receive an email. At the block threshold, posting is refused with a clear explanation.")
        ],
        "use_cases": [
            ("🏗️", "Project Accounting", "Project managers set per-project budgets on analytic accounts. Cost overruns are flagged before they happen — not discovered at project close."),
            ("🏥", "Department Budget Control", "Finance teams assign budgets to departmental analytic accounts. Procurement and AP are blocked from posting beyond approved limits."),
            ("🤝", "Grant Management", "Nonprofits and grant-funded organizations enforce spend limits per grant or funding source — with alerts to grant managers before any threshold is breached.")
        ],
        "accent": "#e74c3c"
    },
    "document_version_control": {
        "name": "Document Version Control",
        "tagline": "Track every version of every document on any Odoo record — with approval workflows, revision history, and supersession management.",
        "badges": ["Full Version Lifecycle", "Approval Workflow", "Any Odoo Model", "Complete Audit Trail"],
        "problems": [
            ("Version Confusion", "Teams share documents via attachments with names like 'Contract_v3_FINAL_revised.pdf'. There's no system record of which version is current or who approved it."),
            ("No Approval Enforcement", "Important documents — contracts, SOPs, specs — are updated without any review process. Unapproved versions go live accidentally."),
            ("Lost History", "When a document is updated, the old version is overwritten. There's no way to retrieve what the document said six months ago or who made specific changes.")
        ],
        "features": [
            ("📄", "Full Version Lifecycle", "Documents move through states: Draft → Active → Superseded or Rejected. Only one version can be Active at a time per document record."),
            ("✅", "Approval Workflow", "Drafts can require approval before going Active. Approvers are notified automatically. Rejection includes a reason logged on the version record."),
            ("📎", "Any Odoo Model", "The document.version.mixin can be attached to any Odoo model — sale orders, purchase orders, projects, employees, or custom models."),
            ("🔗", "Version Chain", "Each version links to its predecessor via previous_version_id — creating a complete, navigable chain of document history."),
            ("👤", "Author & Approver Tracking", "Every version records who created it and who approved it. The complete audit trail is always visible on the version record."),
            ("📂", "Upload Wizard", "A clean upload wizard lets users attach new document files, add notes, and optionally request approval — all in one step.")
        ],
        "steps": [
            ("Attach Document Version Control", "Use the Upload Wizard to create version 1 of any document on any Odoo record. Add notes and choose whether approval is required."),
            ("Route for Approval", "If approval is enabled, the designated approver is notified. They review the document and approve or reject with a reason. The state updates automatically."),
            ("Supersede When Updated", "When a new version is ready, upload it and the previous Active version is automatically marked Superseded — keeping the full history intact.")
        ],
        "use_cases": [
            ("📝", "Contract Management", "Legal teams track every contract revision with full approval history. The Active version is always clearly identified, and the full negotiation trail is preserved."),
            ("🏭", "Manufacturing SOPs", "Quality teams manage SOP versions with mandatory approval before any procedure goes live. Operators always access the current approved version."),
            ("🤝", "Vendor Documents", "Procurement teams track vendor certificates, insurance docs, and compliance certificates — knowing when each was last approved and when it expires.")
        ],
        "accent": "#3498db"
    },
    "sop_checklist": {
        "name": "SOP Checklist Builder",
        "tagline": "Build reusable SOP templates and launch live checklists on any Odoo record — with critical step enforcement, evidence capture, and completion tracking.",
        "badges": ["Reusable Templates", "Critical Step Blocking", "Evidence Attachments", "Works on Any Record"],
        "problems": [
            ("SOPs Live in Binders", "Standard operating procedures are documented in PDFs and binders — completely disconnected from the Odoo records where the work actually happens."),
            ("No Completion Enforcement", "Checklists in shared drives or printed forms can be submitted as 'done' without every step being completed. Critical steps get skipped."),
            ("No Evidence Capture", "Regulated processes require proof that steps were completed. Without an evidence attachment requirement, compliance cannot be demonstrated.")
        ],
        "features": [
            ("📋", "Reusable SOP Templates", "Define sop.template records with steps, sequences, criticality flags, and evidence requirements. Templates are reused across hundreds of checklist instances."),
            ("🚨", "Critical Step Enforcement", "Steps marked as critical must be completed before the checklist can be marked Done. The completion button is blocked until all critical steps are checked off."),
            ("📎", "Evidence Attachments", "Steps can require an evidence attachment — a photo, scan, or measurement record. The step cannot be marked done without an attachment uploaded."),
            ("👤", "Step-Level Accountability", "Each step records who marked it done and when. The done_by_id and done_date fields provide a full accountability trail."),
            ("📊", "Completion Metrics", "The checklist form shows real-time completion percentage, steps done vs. total, and whether any critical steps remain pending."),
            ("🚀", "Launch from Any Record", "The SOP Launch Wizard can attach a checklist to any Odoo record — sale orders, projects, manufacturing orders, service tickets, or custom models.")
        ],
        "steps": [
            ("Build Your Template", "In Project → SOP Templates, create a template with all required steps. Mark critical steps, set evidence requirements, and assign default responsible roles."),
            ("Launch on a Record", "From any Odoo record, click Launch SOP Checklist. Select the template, confirm the start date, and a live checklist instance is created immediately."),
            ("Work Through the Steps", "Team members complete steps on the live checklist — marking done, attaching evidence, adding notes. The system tracks completion and enforces critical step requirements.")
        ],
        "use_cases": [
            ("🏭", "Quality Control", "Manufacturing teams launch QC checklists on each production order. Critical inspection steps require evidence photos before the order can be released."),
            ("🚢", "Onboarding & Offboarding", "HR launches employee onboarding checklists covering IT setup, policy acknowledgment, and access provisioning — all tracked with completion accountability."),
            ("🔧", "Field Service", "Service technicians complete mandatory safety checklists before starting and completing service calls — with evidence attachments proving compliance.")
        ],
        "accent": "#8e44ad"
    },
    "status_calendar_sync": {
        "name": "Status-to-Calendar Event Automation",
        "tagline": "Automatically create calendar events when records move to configured stages — keep your team's calendar in sync with your pipeline, without manual entries.",
        "badges": ["Any Model & Stage", "Custom Event Templates", "Auto-Assigned Attendees", "Zero Manual Entry"],
        "problems": [
            ("Calendar Gaps", "Sales follow-ups, project milestones, and service appointments should trigger calendar events automatically. Instead, someone manually creates them — or forgets entirely."),
            ("Meeting-Record Disconnection", "Calendar events created manually have no link to the originating Odoo record. Updates to the sale or project don't propagate to the calendar."),
            ("Inconsistent Scheduling", "Different reps and project managers handle stage transitions differently. Some create follow-up events, others don't — leading to inconsistent pipeline management.")
        ],
        "features": [
            ("🔄", "Any Model, Any Stage", "Configure sync rules for sale.order, project.task, crm.lead, helpdesk.ticket, or any other model with stages. Rules trigger on stage field change."),
            ("📅", "Custom Event Templates", "Define the event name template, duration, and description dynamically using the record's fields — e.g., 'Follow-up: {partner_name} — {sale_amount}'."),
            ("👥", "Auto-Assigned Attendees", "Rules can automatically add the record's salesperson, project manager, or any configured partner as calendar event attendees."),
            ("⏱️", "Configurable Timing", "Set event start offset (e.g., +3 days from stage change) and duration. Events are created with the correct timing automatically."),
            ("🔗", "Linked to the Record", "Each calendar event includes a link back to the originating record — click from the calendar event to jump directly to the sale order or task."),
            ("📧", "Attendee Notifications", "Created calendar events send the standard Odoo invitation emails to all attendees — ensuring everyone is notified automatically.")
        ],
        "steps": [
            ("Configure a Sync Rule", "Go to Calendar → Stage Sync Rules → New. Select the model (e.g., sale.order), the stage that triggers the event, and the event template settings."),
            ("Move Records Through Stages", "Users process records as normal — moving a lead to 'Proposal Sent' or a task to 'In Review'. The system watches for configured stage changes."),
            ("Calendar Populates Automatically", "When a rule fires, a calendar event is created instantly — title, duration, attendees, and record link all populated. No manual intervention required.")
        ],
        "use_cases": [
            ("💼", "CRM Pipeline", "When a lead moves to 'Proposal Sent', auto-create a follow-up call event 3 days later. When it moves to 'Won', auto-create an onboarding kickoff meeting."),
            ("📋", "Project Management", "When a project task reaches 'Ready for Review', auto-create a review meeting with the project manager and client as attendees."),
            ("🎧", "Customer Service", "When a helpdesk ticket escalates to a configured stage, auto-schedule a customer call — ensuring no escalation falls through without a follow-up.")
        ],
        "accent": "#16a085"
    },
    "household_contact_mgmt": {
        "name": "Household & Family Contact Management",
        "tagline": "Group family members into household records — auto-compute 'John & Mary Smith', share addresses, and track life event dates that matter to your organization.",
        "badges": ["Household Records", "Auto-Salutations", "Family Roles", "Life Event Dates"],
        "problems": [
            ("Fragmented Family Records", "Each family member is a separate, unlinked contact. Sending a household mailing means exporting, deduplicating, and re-importing — or sending duplicates."),
            ("Inconsistent Salutations", "Addressing correspondence to 'The Smith Family' or 'John & Mary Smith' requires manual editing of every communication. Automation is impossible without a household model."),
            ("No Life Event Tracking", "For religious organizations, nonprofits, and membership bodies, birth dates, baptism dates, and anniversaries are important — but standard Odoo contacts have no place for them.")
        ],
        "features": [
            ("🏠", "Household Records", "The household.household model groups res.partner records into a family unit with shared address, phone, email, and membership date."),
            ("✉️", "Auto-Computed Salutations", "Display names compute automatically: primary members plus spouses become 'John & Mary Smith'. Groups of three+ become 'The Smith Family'. Overridable per household."),
            ("👥", "Family Member Roles", "Each household member has a role: Primary, Spouse, Child, Dependent, or Other. Roles drive salutation logic and can drive mailing segmentation."),
            ("📅", "Life Event Date Tracking", "Store birth_date, baptism_date, and marriage anniversary on each member — fields designed for the pastoral and nonprofit contexts where they matter most."),
            ("📍", "Address Sync", "When a household address is updated, a configurable sync ensures member contact records reflect the new address — eliminating the need to update each record separately."),
            ("📊", "Household-Level Reporting", "Filter donors, members, or constituents by household — enabling household-level giving summaries, communication histories, and engagement metrics.")
        ],
        "steps": [
            ("Create a Household", "Go to Contacts → Households → New. Add the family name, address, and contact details. These become the household-level record."),
            ("Add Members", "Link existing contacts (or create new ones) as household members. Assign each member a role — Primary, Spouse, Child — and add their personal dates."),
            ("Use Household Salutations", "The computed display name ('John & Mary Smith') is available for mailings, receipts, and correspondence. Override it any time for special salutations.")
        ],
        "use_cases": [
            ("⛪", "Parish & Religious Communities", "Churches track parishioner families with baptism dates, confirmation dates, and sacramental history — all linked to the household record."),
            ("🤝", "Nonprofits & Charities", "Donor households are tracked as a unit — giving summaries roll up to the household level, enabling accurate family-level donor recognition and tax receipting."),
            ("🎓", "Schools & Alumni Bodies", "Educational institutions track student families and alumni households — enabling family-level communications and multi-generational relationship management.")
        ],
        "accent": "#e74c3c"
    },
    "nonprofit_donation_mgmt": {
        "name": "Nonprofit Donation Management Suite",
        "tagline": "A complete donation lifecycle platform — funds, campaigns, sequential tax receipts, GL posting, and year-end giving statements built for Odoo 18.0.",
        "badges": ["Tax Receipt Generation", "Fund & Campaign Tracking", "Year-End Statements", "CRA/IRS Ready"],
        "problems": [
            ("No Structured Donation Records", "Odoo's standard accounting has invoices and payments — but no native donation concept with fund designation, campaign attribution, or donor acknowledgment workflows."),
            ("Manual Tax Receipt Production", "Organizations manually create tax receipts in Word or PDF tools, print, and mail them. The process is error-prone, time-consuming, and doesn't scale with donor volume."),
            ("Disconnected Year-End Reporting", "Producing year-end giving statements requires exporting payment data, matching to donors, calculating totals in Excel, and generating individual letters — a multi-day project.")
        ],
        "features": [
            ("🎁", "Structured Donation Records", "donation.donation records capture donor, amount, fund, campaign, payment method, and state — separate from the general invoice/payment workflow."),
            ("📊", "Fund & Campaign Tracking", "donation.fund and donation.campaign records let you segment gifts by purpose and fundraising initiative — with real-time totals and progress tracking."),
            ("🧾", "Sequential Tax Receipts", "Tax receipts are generated with sequential references (RCP-YYYY-#####) and a QWeb PDF layout — CRA and IRS format compliant, ready for mailing or email delivery."),
            ("📅", "Year-End Giving Wizard", "The year-end wizard selects all receipted donations for a donor in a year, computes the total, and generates a personalized giving statement PDF — in bulk."),
            ("💰", "GL Posting Integration", "Confirmed donations post journal entries to the correct revenue accounts (by fund) automatically — no double-entry between the donation record and accounting."),
            ("📧", "Donor Acknowledgment Emails", "Automatic acknowledgment emails can be sent when a donation is confirmed — thanking the donor and providing receipt details before the formal PDF is mailed.")
        ],
        "steps": [
            ("Record a Donation", "Go to Donations → New. Select the donor, enter the amount, choose the fund and campaign, and set the payment method. Save and Confirm."),
            ("Generate the Tax Receipt", "Click Generate Receipt on a confirmed donation. The system assigns the next sequential receipt number and produces a print-ready PDF in one click."),
            ("Run Year-End Statements", "At year end, run the Year-End Giving Wizard. Select the year, choose which donors to include, and generate individual giving statements for all of them at once.")
        ],
        "use_cases": [
            ("⛪", "Religious Organizations", "Parishes, dioceses, and religious institutions tracking weekly collections, memorial donations, and capital campaign gifts — with proper receipting for each."),
            ("🤝", "Charities & NGOs", "Registered charities issuing CRA (Canada) or IRS (US) compliant tax receipts need a structured, sequential, auditable system — not a spreadsheet."),
            ("🎓", "Educational Foundations", "School foundations and university development offices managing annual fund campaigns, scholarship donations, and planned gifts at scale.")
        ],
        "accent": "#f39c12"
    },
    "amadio_purchase_approval_matrix": {
        "name": "Purchase Approval Matrix",
        "tagline": "Configure multi-level PO approval tiers based on order value — route every purchase order to the right approver automatically, with a full audit log.",
        "badges": ["Amount-Based Tiers", "Multi-Approver Support", "Full Audit Log", "Override Controls"],
        "problems": [
            ("Bypassed Purchase Controls", "Without structured approval routing, purchase orders above any threshold can be confirmed by anyone with access — bypassing financial controls entirely."),
            ("Manual Approval Workflows", "Operations teams email purchase orders to managers for approval outside of Odoo. There's no audit trail, no tracking, and approvals get lost in inboxes."),
            ("One-Size-Fits-All Controls", "Some organizations need VP approval for orders over $50,000 but department manager approval is sufficient for routine purchases. Standard Odoo has no tier structure.")
        ],
        "features": [
            ("💰", "Amount-Based Approval Tiers", "Define tiers with minimum and optional maximum amounts. Orders in each range route to the designated approver group automatically."),
            ("👥", "Multi-Approver Configuration", "Each tier supports multiple approvers. Configure require-all (all must approve) or any-one mode depending on your governance requirements."),
            ("📋", "Full Audit Log", "Every approval action — approve, reject, or reset — is logged with the approver's name, timestamp, and optional note. The log is permanent and accessible on the PO."),
            ("🚫", "Confirmation Override", "The standard Confirm button is overridden to check the approval tier. POs cannot bypass the approval matrix — the system enforces compliance at the ORM level."),
            ("✅", "One-Click Approve/Reject", "Approvers see a clear action panel on the PO form. They approve or reject with an optional note — no email required, no external system."),
            ("🔧", "Admin-Managed Tiers", "The approval matrix is configured in Purchase → Configuration → Approval Tiers. Changes take effect immediately for new POs without code changes.")
        ],
        "steps": [
            ("Configure Your Tiers", "Go to Purchase → Configuration → Approval Tiers. Define tiers with amount ranges and assign approver users to each tier."),
            ("Submit a Purchase Order", "When a buyer confirms a PO, the system evaluates the total amount, identifies the applicable tier, and moves the PO to Pending Approval."),
            ("Approvers Act", "Designated approvers see pending POs in their queue. They review, approve or reject with a note, and the PO moves to Approved or back to Draft accordingly.")
        ],
        "use_cases": [
            ("🏢", "Mid-Market Businesses", "Organizations with $500K+ annual purchase spend need structured controls. A 3-tier matrix (manager / director / CFO) eliminates unauthorized purchasing."),
            ("🏥", "Healthcare & Public Sector", "Procurement compliance in regulated industries requires documented approval at defined thresholds — with an audit trail available for internal and external review."),
            ("🌍", "Multi-Entity Operations", "Groups with multiple legal entities can configure separate approval matrices per company — each with its own thresholds and approver hierarchies.")
        ],
        "accent": "#e67e22"
    },
    "amadio_hr_onboarding_checklist": {
        "name": "HR Employee Onboarding Checklist",
        "tagline": "Launch structured onboarding checklists automatically when a new employee is created — covering HR, IT, management, and employee tasks with deadline tracking.",
        "badges": ["Auto-Launch on Hire", "Role-Based Steps", "Completion Tracking", "Due Date Enforcement"],
        "problems": [
            ("Forgotten Onboarding Steps", "New hires miss critical first-week tasks — access cards not ordered, system accounts not created, policies not acknowledged — because there's no centralized checklist."),
            ("No Cross-Department Coordination", "Onboarding spans HR, IT, and the hiring manager. Without a shared system, each department does their part in isolation with no visibility into what others have done."),
            ("Inconsistent Experiences", "Onboarding quality varies by manager and department. Some new hires get thorough orientation; others are handed a laptop and left to figure it out.")
        ],
        "features": [
            ("🚀", "Auto-Launch on Creation", "When a new hr.employee record is created, the system automatically launches the default onboarding template — zero manual steps required to start the process."),
            ("👤", "Role-Based Step Assignment", "Steps are assigned to roles: HR (documentation), IT (system access), Manager (orientation), and Employee (self-serve). Each party sees only their tasks."),
            ("📅", "Due Date Calculation", "Step due dates are calculated from the employee's start date using configurable offsets — 'Day 1', 'Day 3', 'End of Week 1', etc."),
            ("✅", "Step-Level Completion", "Each step is marked done individually, recording who completed it and when. Steps can require evidence attachments for compliance-sensitive tasks."),
            ("📊", "Completion Dashboard", "HR can see all active onboarding checklists with completion percentage, overdue steps, and responsible parties — from a single dashboard view."),
            ("📋", "Multiple Templates", "Different departments, roles, or locations can have different onboarding templates. Templates are reusable and version-controlled.")
        ],
        "steps": [
            ("Configure Templates", "Go to Employees → Onboarding Templates. Create templates with steps assigned to HR, IT, Manager, or Employee roles. Set day-offset due dates."),
            ("Hire the Employee", "Create or import the new employee record normally. The system detects the new record and automatically launches the appropriate onboarding template."),
            ("Track to Completion", "HR monitors the onboarding dashboard. Each department completes their assigned steps. Overdue items are highlighted. Completion percentage updates in real time.")
        ],
        "use_cases": [
            ("🏢", "Growing SMBs", "Companies hiring 5–50 people per year need consistent, repeatable onboarding without dedicated HR software. This module runs entirely within their existing Odoo instance."),
            ("🏥", "Healthcare & Regulated Industries", "Mandatory policy acknowledgments, credential verifications, and compliance training sign-offs are tracked with evidence attachments and completion timestamps."),
            ("🌍", "Multi-Location Operations", "Different onboarding templates per location or department ensure new hires in different regions or functions get the right onboarding — not a generic one-size-fits-all process.")
        ],
        "accent": "#27ae60"
    },
    "amadio_stock_expiry_alert": {
        "name": "Stock Lot Expiry Alert & FEFO Enforcer",
        "tagline": "Monitor lot expiry dates in real time, send pre-expiry alerts automatically, enforce First Expired First Out on picks, and quarantine expired stock in one click.",
        "badges": ["Pre-Expiry Alerts", "FEFO Enforcement", "Quarantine Action", "Category-Based Rules"],
        "problems": [
            ("Expired Stock Shipped to Customers", "Without active monitoring, expired lots remain in available stock. Pickers select them — not because they're careless, but because Odoo doesn't warn them."),
            ("Manual Expiry Monitoring", "Someone is responsible for checking expiry dates manually — weekly or monthly. Between checks, product passes its expiry date and continues to be picked."),
            ("FIFO vs. FEFO Confusion", "Standard Odoo supports FIFO (First In, First Out) but not FEFO (First Expired, First Out). For perishables and pharmaceuticals, expiry-based rotation is mandatory.")
        ],
        "features": [
            ("🗓️", "Pre-Expiry Alert Rules", "Configure rules per product category: warn X days before expiry, block Y days before. Email alerts fire automatically to designated stakeholders."),
            ("🚦", "Live Expiry Status on Lots", "Each stock.lot shows a real-time expiry_alert_state: OK (green), Warning (orange), Critical (red), or Expired (gray). Visible at a glance on the lot list."),
            ("📦", "FEFO Pick Enforcement", "On pick validation, the system checks that selected lots are not past expiry. Expired lots are flagged and operators are prompted to select a fresher lot."),
            ("🔒", "One-Click Quarantine", "An action on expired or near-expired lots moves stock to a designated quarantine location instantly — removing it from available inventory without manual transfers."),
            ("⏰", "Daily Cron Monitoring", "A scheduled job runs daily, scanning all lots against their expiry rules. Email digest alerts are sent automatically — no manual monitoring required."),
            ("📊", "Expiry Dashboard", "A dashboard view shows all lots by expiry status — allowing QA managers to see exactly what's at risk without running a report.")
        ],
        "steps": [
            ("Configure Expiry Rules", "Go to Inventory → Configuration → Expiry Rules. Create rules per product category with warn days, block days, and alert email recipients."),
            ("Monitor Automatically", "The daily cron scans all tracked lots. As lots approach expiry thresholds, their status updates and email alerts fire to the configured contacts."),
            ("Act on Alerts", "QA managers review the expiry dashboard. Quarantine expired lots with one click. On picks, operators are guided to FEFO-compliant lot selection automatically.")
        ],
        "use_cases": [
            ("🥩", "Food Distribution", "Distributors handling perishable food products need FEFO-enforced picking and pre-expiry alerts to prevent expired goods from reaching consumers."),
            ("💊", "Pharmaceutical Wholesale", "Pharmaceutical distributors face regulatory requirements for lot tracking and expiry management. Automated alerts and quarantine ensure compliance."),
            ("🧴", "Consumer Goods & Cosmetics", "Personal care and cosmetic products with shelf-life requirements need systematic expiry monitoring to protect brand reputation and consumer safety.")
        ],
        "accent": "#e74c3c"
    },
    "amadio_project_recurring_tasks": {
        "name": "Recurring Project Task Generator",
        "tagline": "Define task templates with recurrence rules and let Odoo generate them automatically — daily, weekly, monthly, or on a custom schedule.",
        "badges": ["Daily/Weekly/Monthly", "Auto-Assigned & Tagged", "Pre-Staged Tasks", "Never Missed"],
        "problems": [
            ("Manually Creating Repetitive Tasks", "Weekly status reports, monthly reconciliations, quarterly reviews — someone manually creates the same task every cycle. It takes time, and sometimes it's forgotten."),
            ("Recurring Tasks Fall Through", "When the person responsible for creating recurring tasks is on leave, those tasks don't get created. Critical obligations are missed without anyone noticing."),
            ("No Traceability to Source", "Tasks created manually have no link to their recurring source. You can't see which tasks came from a recurring template or track completion patterns over time.")
        ],
        "features": [
            ("🔄", "Flexible Recurrence Rules", "Configure templates with daily, weekly (by day of week), monthly (by day of month), or custom interval recurrence. Each template defines its own schedule."),
            ("👤", "Pre-Assigned & Pre-Tagged", "Templates define the default assigned user(s), tags, project, and stage. Generated tasks are ready to work — no setup required after creation."),
            ("📅", "Next Run Date Tracking", "Each template shows its next_run_date. The daily cron checks all active templates and creates tasks for any whose next run date has arrived."),
            ("🔗", "Source Template Link", "Generated tasks include a link to their recurrence template — enabling reporting on recurring task completion rates and pattern analysis."),
            ("⏸️", "Pause and Resume", "Templates can be temporarily deactivated (paused) without deleting them. When reactivated, they resume their schedule from the next appropriate date."),
            ("📊", "Completion Monitoring", "Monitor whether recurring tasks are being completed on time using standard Odoo project reporting, filtered by the recurrence template source.")
        ],
        "steps": [
            ("Create a Task Template", "Go to Project → Recurring Task Templates → New. Set the project, stage, assignees, tags, and choose the recurrence type and interval."),
            ("Set the Schedule", "For weekly recurrence, pick the day of week. For monthly, pick the day of month. The system computes and displays the next_run_date automatically."),
            ("Let It Run", "The daily scheduled job checks all active templates. When next_run_date is today or past, a task is created and the next_run_date is updated. Done.")
        ],
        "use_cases": [
            ("📊", "Finance & Accounting Teams", "Monthly reconciliations, weekly AR aging reviews, quarterly tax reminders — all defined once as templates and generated automatically without manual intervention."),
            ("🔧", "IT Operations", "Weekly backup verifications, monthly security reviews, quarterly disaster recovery tests — critical IT governance tasks that must never be missed."),
            ("👥", "HR & People Ops", "Monthly 1:1 check-in tasks, quarterly performance review cycles, annual compliance training reminders — generated automatically for every relevant employee.")
        ],
        "accent": "#8e44ad"
    },
    "amadio_account_invoice_reminder": {
        "name": "Automated AR Invoice Reminder Engine",
        "tagline": "Configure multi-stage dunning sequences with escalating tone and send automated overdue reminders — with a complete audit trail on every invoice.",
        "badges": ["Multi-Stage Dunning", "Escalating Tone", "Full Audit Trail", "Partner-Level Control"],
        "problems": [
            ("Unpaid Invoices Piling Up", "AR teams have hundreds of overdue invoices but no systematic process for following up. Reminders are sent inconsistently — or not at all — based on individual initiative."),
            ("Manual Follow-Up Burden", "AR staff manually draft reminder emails, find the right invoice, and send them one by one. Hours of their time each week goes to a process that could be fully automated."),
            ("No Escalation Logic", "Day-1 reminders sound the same as day-30 reminders. Without escalating tone and escalation contacts, customers learn they can ignore initial reminders indefinitely.")
        ],
        "features": [
            ("📧", "Multi-Stage Reminder Sequences", "Define sequences with multiple stages — e.g., friendly reminder at day 7, firm notice at day 14, final demand at day 30 — each with its own email template."),
            ("📈", "Escalating Tone per Stage", "Each stage uses a different email template, allowing naturally escalating language from friendly to formal to final notice — appropriate for each point in the collection cycle."),
            ("👤", "Escalation Contacts", "Late stages can CC internal contacts (credit manager, sales rep) and external escalation parties — ensuring the right people are aware as accounts age."),
            ("⏸️", "Pause per Partner", "Individual customers can be marked reminder_paused — suspending all automatic reminders without affecting other customers or the sequence configuration."),
            ("📋", "Per-Invoice Audit Log", "Every reminder sent is logged on the invoice record: which stage, sent by whom, on what date, and any notes. The audit trail is permanent."),
            ("🤖", "Daily Automation", "A scheduled job runs daily, scanning all overdue invoices, matching them to their partner's reminder sequence, and sending the appropriate stage automatically.")
        ],
        "steps": [
            ("Build Your Dunning Sequence", "Go to Accounting → AR Reminders → Sequences. Create a sequence with stages — set days-overdue trigger and assign an email template to each stage."),
            ("Assign to Customers", "On each customer's contact record, select their reminder sequence (or leave blank for the default). Individual customers can be paused if needed."),
            ("Let the Cron Run", "The daily job scans overdue invoices, matches to sequences, sends the next applicable stage, and logs the action on the invoice. No manual follow-up required.")
        ],
        "use_cases": [
            ("🏢", "B2B Service Businesses", "Consulting firms, agencies, and professional service providers with net-30/60 terms need systematic follow-up to maintain cash flow without damaging relationships."),
            ("🏗️", "Distributors & Wholesalers", "High-volume B2B distributors with hundreds of customer accounts need automated AR follow-up that scales — not a manual process dependent on individual AR staff."),
            ("🏥", "Healthcare & Professional Practices", "Medical practices, law firms, and other professional services billing insurance and patients need compliant, trackable follow-up on aging receivables.")
        ],
        "accent": "#d35400"
    },
    "amadio_vendor_performance_scorecard": {
        "name": "Vendor Performance Scorecard",
        "tagline": "Rate vendors on delivery, quality, pricing, and service — scorecards auto-update from PO receipts and surface your best and worst performers at a glance.",
        "badges": ["4-Dimension Rating", "Auto-Computed Scores", "Monthly Scorecards", "Dashboard KPIs"],
        "problems": [
            ("Gut-Feel Vendor Decisions", "Procurement teams choose vendors based on price and habit — not data. Poor performers stay on the approved vendor list because there's no objective scorecard to flag them."),
            ("No Post-Delivery Feedback Loop", "Once a purchase order is received and closed, the performance data is lost. There's no mechanism to capture whether delivery was on time, quality was acceptable, or pricing was accurate."),
            ("Vendor Review Preparation", "Annual or quarterly vendor reviews require pulling data from email, spreadsheets, and memory. Preparation takes days — and the data is still incomplete and subjective.")
        ],
        "features": [
            ("⭐", "4-Dimension Rating on POs", "Rate each vendor on Delivery (on-time), Quality (defect rate), Price (accuracy vs. quote), and Service (communication, responsiveness) directly on the purchase order."),
            ("📊", "Weighted Overall Score", "An overall_score is computed as a configurable weighted average of the four dimensions — giving you a single number to compare vendors at a glance."),
            ("📅", "Monthly Scorecard Generation", "A scheduled job generates monthly vendor.scorecard records per active vendor — aggregating all rated POs in the period into a single scorecard."),
            ("📈", "Trend Visualization", "Scorecard history shows performance trends over time — identifying improving vendors, declining suppliers, and seasonal patterns."),
            ("🔔", "Low-Score Alerts", "Configure an alert threshold. Vendors scoring below the threshold trigger an email notification to the procurement manager for review."),
            ("🏆", "Dashboard Rankings", "A dashboard view ranks all vendors by overall score — instantly surfacing your top performers and flagging underperformers for corrective action.")
        ],
        "steps": [
            ("Rate at Receiving", "When closing a purchase order, the purchasing team rates the vendor on the four dimensions directly on the PO form. Ratings take 30 seconds."),
            ("Scorecards Auto-Generate", "At the start of each month, the cron job aggregates the previous month's ratings into a vendor scorecard — automatically, with no manual compilation."),
            ("Review and Act", "Procurement managers review the vendor dashboard. Low scorers are flagged for discussion, improvement plans, or replacement sourcing decisions.")
        ],
        "use_cases": [
            ("🏭", "Manufacturing Companies", "Manufacturers with multiple raw material suppliers need objective, data-driven vendor rankings to support sourcing decisions and ISO supplier evaluation requirements."),
            ("🛒", "Retail & Distribution", "Distributors buying from dozens of suppliers need to track on-time delivery rates, quality return rates, and pricing accuracy to protect margins and service levels."),
            ("🏗️", "Construction & Engineering", "Project-based businesses need contractor and subcontractor performance data to make informed decisions on repeat engagement and bid evaluations.")
        ],
        "accent": "#16a085"
    },
    "amadio_contract_lifecycle_mgr": {
        "name": "Contract Lifecycle & Renewal Manager",
        "tagline": "Track every contract with renewal dates, alert owners before windows close, manage amendments, and ensure no contract expires without a conscious decision.",
        "badges": ["Renewal Alert Engine", "Amendment Tracking", "Auto-Renew Flags", "Full Lifecycle States"],
        "problems": [
            ("Silent Contract Renewals", "Auto-renewing contracts roll over for another year unnoticed — committing the business to vendor relationships, pricing, or terms that haven't been reviewed."),
            ("Manual Contract Calendar", "Contracts are tracked in shared spreadsheets or on personal calendars. When the owner leaves, contract renewal dates leave with them."),
            ("No Amendment History", "Contract modifications are handled via email and replacement PDFs. There's no structured record of what changed, when, and who approved the amendment.")
        ],
        "features": [
            ("🔔", "Renewal Alert Engine", "Configure renewal notice periods (e.g., 90 days before expiry). The system automatically transitions contracts to 'Pending Renewal' state and emails all stakeholders."),
            ("📋", "Full Lifecycle States", "Contracts move through states: Draft → Active → Pending Renewal → Renewed or Expired or Terminated. Each state transition is date-stamped and logged."),
            ("🔄", "Auto-Renew Flag", "Mark contracts as auto-renewing. The system tracks these separately and sends earlier alerts — ensuring renewal decisions are made intentionally, not by default."),
            ("📝", "Amendment Tracking", "Contract amendments are logged as structured records — date, description, and attachment. The full amendment history is always visible on the contract record."),
            ("👥", "Stakeholder Notifications", "Each contract has an owner and optional legal contact. Both receive renewal alerts, plus any additional stakeholders configured on the alert list."),
            ("🔗", "Linked to Sales Orders", "Customer contracts can be linked to related sale.order records — providing context about the commercial relationship behind each contract.")
        ],
        "steps": [
            ("Register Your Contracts", "Create a contract.contract record for each agreement — customer, vendor, employment, or NDA. Set start date, end date, renewal notice period, and stakeholders."),
            ("System Monitors Expiry", "The daily cron evaluates all active contracts. When a contract enters its notice window, state changes to Pending Renewal and email alerts fire automatically."),
            ("Renew or Terminate", "Stakeholders review the contract during the notice window. Click Renew to create a new contract linked to the original, or Terminate to close it formally.")
        ],
        "use_cases": [
            ("🏢", "Corporate Legal Teams", "In-house legal departments managing vendor, customer, and employment contracts need a centralized system with proactive alerts — not reactive scrambling."),
            ("🤝", "SaaS & Subscription Businesses", "Companies with annual subscription contracts need to track renewal windows, manage auto-renew exceptions, and ensure sales teams engage customers before contracts lapse."),
            ("🏗️", "Real Estate & Facilities", "Organizations managing leases, service agreements, and maintenance contracts need renewal visibility — especially for contracts with significant cost or operational implications.")
        ],
        "accent": "#2980b9"
    },
    "amadio_meeting_minutes": {
        "name": "Structured Meeting Minutes & Action Tracker",
        "tagline": "Capture structured minutes directly in Odoo calendar events — record decisions, assign action items, and auto-email minutes to all attendees when published.",
        "badges": ["Calendar Integration", "Action Item Tracking", "Auto-Email Minutes", "Decision Register"],
        "problems": [
            ("Minutes in Email Threads", "Meeting notes are captured in email chains and shared drives — disconnected from the calendar event that generated them and lost within weeks."),
            ("Untracked Action Items", "Verbal commitments made in meetings are not tracked anywhere. Follow-up depends on individual memory. Action items are forgotten or revisited repeatedly."),
            ("No Decision Register", "Decisions made in meetings are buried in notes that nobody reads. When a decision is questioned six months later, nobody can find where it was made or who agreed.")
        ],
        "features": [
            ("📅", "Native Calendar Integration", "meeting.minutes records link directly to calendar.event records. Open any calendar event and access its minutes — agenda, decisions, and action items in one place."),
            ("✅", "Structured Action Items", "Each action item records: description, owner, due date, priority (low/medium/high/critical), and completion status — with done date stamped automatically."),
            ("📧", "Auto-Email on Publish", "When minutes are published, all calendar event attendees receive an automatic email with the full minutes — decisions, action items, and next steps."),
            ("📋", "Decision Register", "Decisions are captured as a structured field — separate from general notes — making it easy to find what was decided in any meeting without reading every line."),
            ("👤", "Facilitator Tracking", "Each meeting records the facilitator and attendees. The facilitator is defaulted to the calendar event organizer but can be changed."),
            ("🔍", "Action Item Dashboard", "All open action items across all meetings are visible in a single filtered view — sortable by owner, due date, and priority.")
        ],
        "steps": [
            ("Open the Minutes", "From any calendar event, click the Minutes button to open or create the meeting minutes record. The event, attendees, and date are pre-populated."),
            ("Capture During the Meeting", "Record the agenda, capture decisions as they're made, and add action items with owners and due dates in real time during the meeting."),
            ("Publish and Distribute", "Click Publish when the minutes are finalized. An automatic email is sent to all attendees with the full minutes. Action items are tracked to completion.")
        ],
        "use_cases": [
            ("🏢", "Executive & Board Meetings", "Board and executive team meetings with formal minutes requirements benefit from structured decision and action item capture — with automatic distribution to all attendees."),
            ("📋", "Project Kick-Off & Status Meetings", "Project teams capture meeting outcomes directly linked to project calendar events — keeping project communications in one place within Odoo."),
            ("🤝", "Client-Facing Meetings", "Account managers document client meetings with structured action items and auto-email minutes — providing clients with professional follow-up documentation automatically.")
        ],
        "accent": "#7f8c8d"
    },
    "amadio_asset_maintenance_scheduler": {
        "name": "Fixed Asset Preventive Maintenance Scheduler",
        "tagline": "Link maintenance schedules directly to Odoo fixed assets — configure service intervals, receive pre-due alerts, track costs, and extend asset life systematically.",
        "badges": ["Asset-Linked Schedules", "Pre-Due Alerts", "Maintenance Log", "Cost Tracking"],
        "problems": [
            ("Reactive Maintenance Culture", "Equipment is only serviced when it breaks down. Preventive maintenance is intended but never tracked — leading to higher repair costs and shorter asset life."),
            ("Maintenance Disconnected from Assets", "Service records are kept in paper logs, spreadsheets, or separate systems — completely disconnected from the fixed asset records in Odoo."),
            ("No Upcoming Maintenance Visibility", "Finance and operations teams have no visibility into what maintenance is coming up, what it will cost, and how it aligns with asset depreciation schedules.")
        ],
        "features": [
            ("🔧", "Asset-Linked Schedules", "Create asset.maintenance.schedule records directly linked to account.asset records — connecting maintenance planning with financial asset management."),
            ("📅", "Time-Based Service Intervals", "Configure maintenance intervals in days (e.g., every 90 days, every 365 days). Next maintenance date computes automatically from the last service date."),
            ("🔔", "Pre-Due Email Alerts", "Set an alert lead time (e.g., 14 days before due). The daily cron sends email alerts to the responsible person and configured stakeholders before maintenance is due."),
            ("📋", "Maintenance Log", "Each maintenance event is logged as asset.maintenance.log — recording date, who performed the service, cost, notes, and any attachment (service report, invoice)."),
            ("💰", "Cost Tracking", "Cumulative maintenance costs are tracked against each asset — providing data for total cost of ownership analysis and asset replacement decisions."),
            ("📊", "Next Maintenance Dashboard", "The fixed asset form shows next maintenance date and upcoming schedule summary — giving finance and operations a shared view of asset service status.")
        ],
        "steps": [
            ("Create a Schedule", "On any fixed asset record, go to the Maintenance tab and create a schedule — set the interval, responsible person, alert lead time, and first service date."),
            ("Log Each Service", "When maintenance is performed, add a maintenance log entry with date, cost, and notes. The next maintenance date updates automatically."),
            ("Receive Alerts", "The daily cron sends email alerts when maintenance is upcoming. Responsible staff are notified in advance — eliminating missed service events.")
        ],
        "use_cases": [
            ("🏭", "Manufacturing Equipment", "Factory operators maintain production equipment on scheduled intervals — with maintenance costs tracked against each machine for accurate cost-per-unit analysis."),
            ("🚚", "Fleet Management", "Companies with vehicle fleets link oil changes, tire rotations, and annual inspections to fleet asset records — with automatic reminders before each service is due."),
            ("🏢", "Facilities Management", "Building systems (HVAC, elevators, generators, fire suppression) require scheduled preventive maintenance. Linking schedules to asset records ensures nothing is missed.")
        ],
        "accent": "#f39c12"
    },
    "amadio_sales_commission_tracker": {
        "name": "Sales Commission Tracker",
        "tagline": "Configure commission rules by rep, team, product category, or customer — auto-calculate commissions on paid invoices and manage monthly statements through approval to payment.",
        "badges": ["Flexible Commission Rules", "Paid-Invoice Trigger", "Approval Workflow", "Payroll Export"],
        "problems": [
            ("Commission Disputes", "Without a transparent, rules-based system, sales reps don't trust commission calculations. Disputes consume management time and damage motivation."),
            ("Manual Spreadsheet Calculation", "Finance calculates commissions in Excel every month — matching invoices to reps, applying rates, handling exceptions manually. It takes days and errors happen."),
            ("No Approved Audit Trail", "When a rep questions their commission, there's no system record showing exactly which invoices contributed, at what rate, and who approved the statement.")
        ],
        "features": [
            ("📐", "Flexible Commission Rules", "Commission plans support rules by sales rep, team, product category, minimum order amount, and calculation basis (invoiced or paid) — any combination your business requires."),
            ("💰", "Paid-Invoice Trigger", "Commissions calculate on invoice payment — not invoicing — eliminating commission payments on uncollected revenue. The trigger is automatic and audit-logged."),
            ("📋", "Monthly Statements", "The monthly cron generates commission.statement records per active rep — listing every qualifying invoice, amount, rate, and commission line for full transparency."),
            ("✅", "Approval Workflow", "Statements move through Submit → Approve → Mark Paid. Each state change is date-stamped with the acting user — creating a clean approval audit trail."),
            ("📧", "Rep Notifications", "Reps receive automatic email notifications when their statement is generated and when it's approved — keeping them informed throughout the process."),
            ("📤", "Payroll Export", "Approved statements can be exported for payroll processing — providing the net commission amount per rep in a format ready for your payroll system.")
        ],
        "steps": [
            ("Define Commission Plans", "Go to Sales → Commission Plans → New. Create rules specifying rep/category/amount conditions and the applicable rate. Assign plans to sales reps."),
            ("Statements Generate Monthly", "At month end, the cron job creates statements for all active reps — calculating commissions on payments received during the period."),
            ("Review, Approve, Pay", "Reps review their statements. Sales managers approve. Finance marks as paid after payroll processing. Every step is timestamped and logged.")
        ],
        "use_cases": [
            ("💼", "Sales-Driven Organizations", "Any B2B business with a commissioned sales force — technology, manufacturing, distribution, professional services — benefits from a transparent, automated commission system."),
            ("🏗️", "Multi-Rep Teams", "Sales teams with complex commission structures (tiered rates, team commissions, category-specific rates) need a rules engine that handles complexity without spreadsheet gymnastics."),
            ("🌍", "Multi-Currency Operations", "International sales teams with commissions in different currencies need a commission system that handles multi-currency invoicing correctly.")
        ],
        "accent": "#f1c40f"
    },
    "amadio_inventory_reorder_optimizer": {
        "name": "Inventory Demand Forecast & Reorder Optimizer",
        "tagline": "Analyze 12 months of demand history to suggest optimal reorder points and safety stock — flag stockout risks and generate draft purchase orders automatically.",
        "badges": ["12-Month History Analysis", "Reorder Point Suggestions", "Stockout Prediction", "Draft PO Generation"],
        "problems": [
            ("Gut-Feel Reorder Points", "Reorder points are set once during implementation and never updated. As demand patterns change, some products stockout while others accumulate excess inventory."),
            ("Stockouts and Overstock Coexisting", "Warehouses simultaneously run out of fast-moving items while slow movers consume shelf space and working capital — because replenishment decisions aren't data-driven."),
            ("Reactive Purchasing", "Buyers only order when stock physically runs out — leading to emergency purchases at premium prices, expedite fees, and service level failures.")
        ],
        "features": [
            ("📊", "12-Month Demand Analysis", "The system analyzes 365 days of stock.move history per product/warehouse, computing average daily demand, demand variability, and trend direction."),
            ("📍", "Reorder Point Suggestions", "Based on average demand and lead time, the system suggests optimal reorder points and maximum order quantities — calculated to balance stockout risk and carrying cost."),
            ("🛡️", "Safety Stock Calculation", "Configurable safety stock days are factored into suggested reorder points — providing buffer for demand spikes and supplier lead time variability."),
            ("🚨", "Stockout Risk Flagging", "Products are classified as Healthy, Watch, or Critical based on current stock vs. suggested reorder point. Critical items are highlighted for immediate action."),
            ("📋", "Draft PO Generation", "For products at or below their suggested reorder point, the system generates draft RFQs (Request for Quotation) automatically — ready for buyer review and approval."),
            ("🔄", "Weekly Recalculation", "A weekly cron job re-runs demand analysis for all monitored products — keeping suggestions current as demand patterns evolve.")
        ],
        "steps": [
            ("Configure Products to Monitor", "Enable demand forecasting on products you want to monitor. Set the supplier lead time and safety stock days for accurate reorder point calculation."),
            ("Review Suggestions", "The weekly cron generates or updates inventory.forecast records per product/warehouse. Review the dashboard — Critical items need immediate attention."),
            ("Generate Draft Orders", "For Critical or Watch items below their reorder point, click Generate Purchase Orders. Draft RFQs are created and ready for buyer review and confirmation.")
        ],
        "use_cases": [
            ("🛒", "E-Commerce Retailers", "Online retailers with hundreds of SKUs and variable demand need data-driven reorder points to maintain service levels without tying up excess cash in inventory."),
            ("🏭", "Manufacturing Operations", "Manufacturers buying raw materials and components need accurate reorder points that account for production lead times and demand variability."),
            ("🏗️", "Wholesale Distributors", "Distributors balancing fill rates, carrying costs, and supplier lead times across large product catalogs benefit from systematic, data-driven reorder optimization.")
        ],
        "accent": "#1abc9c"
    },
}

def generate_html(module_dir, data):
    accent = data['accent']
    name = data['name']
    tagline = data['tagline']
    badges = data['badges']
    problems = data['problems']
    features = data['features']
    steps = data['steps']
    use_cases = data['use_cases']

    badges_html = ''.join(f'<span class="badge">{b}</span>' for b in badges)

    problems_html = ''.join(f'''
        <div class="problem-card">
            <div class="problem-title">{p[0]}</div>
            <p>{p[1]}</p>
        </div>''' for p in problems)

    features_html = ''.join(f'''
        <div class="feature-card">
            <div class="feature-icon" style="background:{accent}">{f[0]}</div>
            <div class="feature-content">
                <h4>{f[1]}</h4>
                <p>{f[2]}</p>
            </div>
        </div>''' for f in features)

    steps_html = ''.join(f'''
        <div class="step-card">
            <div class="step-number" style="background:{accent}">{i+1}</div>
            <h4>{s[0]}</h4>
            <p>{s[1]}</p>
        </div>''' for i, s in enumerate(steps))

    use_cases_html = ''.join(f'''
        <div class="usecase-card">
            <div class="usecase-icon">{u[0]}</div>
            <h4>{u[1]}</h4>
            <p>{u[2]}</p>
        </div>''' for u in use_cases)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — AMADIO for Odoo 18.0</title>
<meta name="description" content="{tagline}">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, sans-serif; color: #1a202c; line-height: 1.6; }}

/* Brand Header */
.brand-header {{ background: #0f3460; padding: 16px 40px; display: flex; justify-content: space-between; align-items: center; }}
.brand-name {{ color: #fff; font-size: 24px; font-weight: 800; letter-spacing: 4px; }}
.brand-sub {{ color: #a0aec0; font-size: 12px; letter-spacing: 1px; margin-top: 3px; }}
.brand-url {{ color: {accent}; font-size: 14px; font-weight: 600; text-decoration: none; }}

/* Hero */
.hero {{ background: linear-gradient(135deg, #0f3460 0%, #1a3a6b 60%, #0d2845 100%); padding: 60px 40px; border-bottom: 4px solid {accent}; }}
.hero-inner {{ max-width: 960px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; }}
.hero h1 {{ color: #fff; font-size: 38px; font-weight: 800; line-height: 1.2; margin-bottom: 16px; }}
.hero p {{ color: #cbd5e0; font-size: 17px; line-height: 1.7; margin-bottom: 24px; }}
.badges {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.badge {{ background: rgba(255,255,255,0.12); color: #e2e8f0; border: 1px solid rgba(255,255,255,0.2); padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 500; }}

/* Sections */
.section {{ padding: 60px 40px; }}
.section-inner {{ max-width: 960px; margin: 0 auto; }}
.section-gray {{ background: #f8fafc; }}
.section-white {{ background: #ffffff; }}
.section h2 {{ color: #0f3460; font-size: 28px; font-weight: 800; margin-bottom: 8px; }}
.section-sub {{ color: #718096; font-size: 16px; margin-bottom: 40px; }}

/* Problem Cards */
.problems-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
.problem-card {{ background: #fff; border-left: 4px solid #e53e3e; border-radius: 8px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); transition: box-shadow 0.2s; }}
.problem-card:hover {{ box-shadow: 0 4px 16px rgba(0,0,0,0.12); }}
.problem-title {{ color: #c53030; font-size: 16px; font-weight: 700; margin-bottom: 10px; }}
.problem-card p {{ color: #4a5568; font-size: 14px; }}

/* Feature Cards */
.features-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
.feature-card {{ background: #fff; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); transition: box-shadow 0.2s; display: flex; gap: 16px; align-items: flex-start; }}
.feature-card:hover {{ box-shadow: 0 6px 20px rgba(0,0,0,0.1); }}
.feature-icon {{ width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }}
.feature-content h4 {{ color: #0f3460; font-size: 15px; font-weight: 700; margin-bottom: 6px; }}
.feature-content p {{ color: #4a5568; font-size: 13px; line-height: 1.6; }}

/* Steps */
.steps-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
.step-card {{ text-align: center; padding: 32px 20px; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); transition: box-shadow 0.2s; }}
.step-card:hover {{ box-shadow: 0 6px 20px rgba(0,0,0,0.1); }}
.step-number {{ width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 24px; font-weight: 800; margin: 0 auto 20px; }}
.step-card h4 {{ color: #0f3460; font-size: 17px; font-weight: 700; margin-bottom: 12px; }}
.step-card p {{ color: #4a5568; font-size: 14px; line-height: 1.6; }}

/* Use Cases */
.usecases-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
.usecase-card {{ background: #fff; border-radius: 10px; padding: 28px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.06); transition: box-shadow 0.2s; }}
.usecase-card:hover {{ box-shadow: 0 6px 20px rgba(0,0,0,0.1); }}
.usecase-icon {{ font-size: 36px; margin-bottom: 16px; }}
.usecase-card h4 {{ color: #0f3460; font-size: 16px; font-weight: 700; margin-bottom: 10px; }}
.usecase-card p {{ color: #4a5568; font-size: 14px; line-height: 1.6; }}

/* Specs */
.specs-table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
.specs-table th, .specs-table td {{ padding: 14px 20px; text-align: left; border-bottom: 1px solid #edf2f7; }}
.specs-table th {{ background: #0f3460; color: #fff; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; width: 200px; }}
.specs-table td {{ color: #2d3748; font-size: 14px; }}
.specs-table tr:last-child th, .specs-table tr:last-child td {{ border-bottom: none; }}

/* Footer */
.footer {{ background: #0f3460; color: #a0aec0; text-align: center; padding: 40px 40px; }}
.footer-brand {{ color: #fff; font-size: 20px; font-weight: 800; letter-spacing: 3px; margin-bottom: 8px; }}
.footer-tagline {{ color: {accent}; font-size: 14px; font-style: italic; margin-bottom: 16px; }}
.footer-info {{ font-size: 13px; }}
</style>
</head>
<body>

<!-- Brand Header -->
<div class="brand-header">
  <div>
    <div class="brand-name">AMADIO</div>
    <div class="brand-sub">Premium Odoo 18.0 Applications</div>
  </div>
  <a href="https://amadio.io" class="brand-url">amadio.io</a>
</div>

<!-- Hero -->
<div class="hero">
  <div class="hero-inner">
    <div>
      <h1>{name}</h1>
      <p>{tagline}</p>
    </div>
    <div class="badges">{badges_html}</div>
  </div>
</div>

<!-- The Challenge -->
<div class="section section-white">
  <div class="section-inner">
    <h2>The Challenge</h2>
    <p class="section-sub">Why organizations need {name}</p>
    <div class="problems-grid">{problems_html}</div>
  </div>
</div>

<!-- Features -->
<div class="section section-gray">
  <div class="section-inner">
    <h2>What {name} Does</h2>
    <p class="section-sub">Six capabilities built specifically for this problem</p>
    <div class="features-grid">{features_html}</div>
  </div>
</div>

<!-- How It Works -->
<div class="section section-white">
  <div class="section-inner">
    <h2>How It Works</h2>
    <p class="section-sub">Operational in minutes — not weeks</p>
    <div class="steps-grid">{steps_html}</div>
  </div>
</div>

<!-- Use Cases -->
<div class="section section-gray">
  <div class="section-inner">
    <h2>Perfect For</h2>
    <p class="section-sub">Industries and organizations that rely on {name}</p>
    <div class="usecases-grid">{use_cases_html}</div>
  </div>
</div>

<!-- Technical Specs -->
<div class="section section-white">
  <div class="section-inner">
    <h2>Technical Specifications</h2>
    <p class="section-sub">Compatibility and deployment details</p>
    <table class="specs-table">
      <tr><th>Odoo Version</th><td>18.0</td></tr>
      <tr><th>Platform</th><td>Odoo.sh &amp; On-Premise</td></tr>
      <tr><th>License</th><td>OPL-1</td></tr>
      <tr><th>Author</th><td>AMADIO</td></tr>
      <tr><th>Support</th><td>info@amadio.io</td></tr>
      <tr><th>Website</th><td>amadio.io</td></tr>
    </table>
  </div>
</div>

<!-- Footer -->
<div class="footer">
  <div class="footer-brand">AMADIO</div>
  <div class="footer-tagline">Premium Odoo Consulting &amp; Applications</div>
  <div class="footer-info">amadio.io &nbsp;|&nbsp; info@amadio.io<br><br>Built by consultants who deploy Odoo every day.</div>
</div>

</body>
</html>"""

BASE = "/tmp/amadio-push"

for module_dir, data in MODULES.items():
    html_path = f"{BASE}/{module_dir}/static/description/index.html"
    if not os.path.exists(os.path.dirname(html_path)):
        print(f"SKIP {module_dir} — directory not found")
        continue
    html = generate_html(module_dir, data)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  OK {module_dir}/index.html ({len(html):,} chars)")

print("\nAll HTML pages written.")
