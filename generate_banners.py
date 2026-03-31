from PIL import Image, ImageDraw
import os
try:
    from PIL import ImageFont
    import glob
    # Try to find a system font
    font_paths = glob.glob('/usr/share/fonts/truetype/**/*.ttf', recursive=True)
    bold_fonts = [f for f in font_paths if 'Bold' in f or 'bold' in f]
    regular_fonts = [f for f in font_paths if 'Bold' not in f and 'bold' not in f]
    FONT_BOLD = bold_fonts[0] if bold_fonts else (regular_fonts[0] if regular_fonts else None)
    FONT_REG = regular_fonts[0] if regular_fonts else FONT_BOLD
except:
    FONT_BOLD = None
    FONT_REG = None

NAVY = (15, 52, 96)         # #0f3460
NAVY_LIGHT = (26, 74, 122)  # #1a4a7a
WHITE = (255, 255, 255)
LIGHT_GRAY = (160, 174, 192) # #a0aec0

MODULES = [
    ("inventory_location_validation", "Real-Time Inventory Location Validation", "#e67e22"),
    ("shipment_doc_compliance", "Pre-Shipment Document Compliance Checker", "#2ecc71"),
    ("bank_deposit_prep", "Bank Deposit Preparation & Slip Generator", "#3498db"),
    ("smart_mail_template", "Smart Email Template Selector", "#9b59b6"),
    ("warehouse_pick_optimizer", "Warehouse Pick Path Optimizer", "#1abc9c"),
    ("budget_line_alert", "Analytic Budget Alert & Variance Monitor", "#e74c3c"),
    ("document_version_control", "Document Version Control", "#3498db"),
    ("sop_checklist", "SOP Checklist Builder", "#8e44ad"),
    ("status_calendar_sync", "Status-to-Calendar Event Automation", "#16a085"),
    ("household_contact_mgmt", "Household & Family Contact Management", "#e74c3c"),
    ("nonprofit_donation_mgmt", "Nonprofit Donation Management Suite", "#f39c12"),
    ("amadio_purchase_approval_matrix", "Purchase Approval Matrix", "#e67e22"),
    ("amadio_hr_onboarding_checklist", "HR Employee Onboarding Checklist", "#27ae60"),
    ("amadio_stock_expiry_alert", "Stock Lot Expiry Alert & FEFO Enforcer", "#e74c3c"),
    ("amadio_project_recurring_tasks", "Recurring Project Task Generator", "#8e44ad"),
    ("amadio_account_invoice_reminder", "Automated AR Invoice Reminder Engine", "#d35400"),
    ("amadio_vendor_performance_scorecard", "Vendor Performance Scorecard", "#16a085"),
    ("amadio_contract_lifecycle_mgr", "Contract Lifecycle & Renewal Manager", "#2980b9"),
    ("amadio_meeting_minutes", "Structured Meeting Minutes & Action Tracker", "#7f8c8d"),
    ("amadio_asset_maintenance_scheduler", "Fixed Asset Preventive Maintenance Scheduler", "#f39c12"),
    ("amadio_sales_commission_tracker", "Sales Commission Tracker", "#f1c40f"),
    ("amadio_inventory_reorder_optimizer", "Inventory Demand Forecast & Reorder Optimizer", "#1abc9c"),
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def draw_gradient(img, width, height, color1, color2):
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def make_font(path, size):
    if path:
        try:
            return ImageFont.truetype(path, size)
        except:
            pass
    return ImageFont.load_default()

def wrap_text(text, max_chars):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current = (current + " " + word).strip()
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

W, H = 1200, 628

for (dirname, display_name, accent_hex) in MODULES:
    out_path = f"/tmp/amadio-push/{dirname}/static/description/banner.png"
    if not os.path.exists(os.path.dirname(out_path)):
        print(f"  Skipping {dirname} — directory not found")
        continue

    accent_rgb = hex_to_rgb(accent_hex)
    accent_dark = tuple(max(0, c - 30) for c in accent_rgb)

    img = Image.new('RGB', (W, H), NAVY)

    # Gradient background
    draw_gradient(img, W, H, NAVY, (10, 38, 72))
    draw = ImageDraw.Draw(img)

    # Accent color panel — right 38% with semi-transparency effect
    panel_x = int(W * 0.62)
    # Draw accent panel with alpha blend manually
    accent_panel = Image.new('RGB', (W - panel_x, H), accent_rgb)
    # Blend
    for y in range(H):
        for x in range(W - panel_x):
            bg_px = img.getpixel((panel_x + x, y))
            blended = tuple(int(bg_px[c] * 0.35 + accent_rgb[c] * 0.65) for c in range(3))
            accent_panel.putpixel((x, y), blended)
    img.paste(accent_panel, (panel_x, 0))
    draw = ImageDraw.Draw(img)

    # Diagonal divider line
    draw.polygon([(panel_x, 0), (panel_x + 60, 0), (panel_x - 60, H), (panel_x - 120, H)], fill=tuple(int(c * 0.5) for c in accent_rgb))

    # Bottom accent bar
    draw.rectangle([(0, H - 8), (W, H)], fill=accent_rgb)

    # Accent circle decoration in right panel
    cx, cy = panel_x + (W - panel_x) // 2, H // 2
    r = 120
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=WHITE, width=3)
    draw.ellipse([(cx - r//2, cy - r//2), (cx + r//2, cy + r//2)], fill=tuple(int(c * 0.7) for c in accent_rgb))

    # "AMADIO" heading
    font_amadio = make_font(FONT_BOLD, 72)
    draw.text((60, 70), "AMADIO", font=font_amadio, fill=WHITE)

    # Subtitle
    font_sub = make_font(FONT_REG, 22)
    draw.text((62, 155), "Premium Odoo 18.0 Application", font=font_sub, fill=LIGHT_GRAY)

    # Separator line
    draw.rectangle([(60, 190), (400, 193)], fill=accent_rgb)

    # Module name (wrapped)
    font_name = make_font(FONT_BOLD, 44)
    lines = wrap_text(display_name, 26)
    y_name = 220
    for line in lines[:3]:  # max 3 lines
        draw.text((60, y_name), line, font=font_name, fill=WHITE)
        y_name += 58

    # amadio.io at bottom left
    font_url = make_font(FONT_REG, 20)
    draw.text((60, H - 45), "amadio.io", font=font_url, fill=LIGHT_GRAY)
    draw.text((W - 180, H - 45), "by AMADIO", font=font_url, fill=WHITE)

    img.save(out_path, 'PNG', optimize=True)
    print(f"  OK {dirname}/banner.png")

print("\nAll banners generated.")
