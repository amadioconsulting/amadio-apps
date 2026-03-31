import os, re

BASE = "/tmp/amadio-push"

modules = [d for d in os.listdir(BASE) if os.path.isdir(os.path.join(BASE, d)) and not d.startswith('.') and not d.startswith('_')]

for module in sorted(modules):
    manifest_path = os.path.join(BASE, module, "__manifest__.py")
    if not os.path.exists(manifest_path):
        continue
    with open(manifest_path, 'r') as f:
        content = f.read()

    # Fix license
    content = re.sub(r'"license":\s*"LGPL-3"', '"license": "OPL-1"', content)
    content = re.sub(r"'license':\s*'LGPL-3'", "'license': 'OPL-1'", content)

    # Fix images key — ensure banner.png is first
    if 'banner.png' not in content:
        content = re.sub(
            r'"images":\s*\["static/description/icon\.png"\]',
            '"images": ["static/description/banner.png", "static/description/icon.png"]',
            content
        )
        content = re.sub(
            r"'images':\s*\['static/description/icon\.png'\]",
            "'images': ['static/description/banner.png', 'static/description/icon.png']",
            content
        )

    with open(manifest_path, 'w') as f:
        f.write(content)
    print(f"  OK {module}")

print("\nAll manifests updated.")
