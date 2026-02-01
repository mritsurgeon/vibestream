#!/usr/bin/env python3
import os
import zipfile
import xml.etree.ElementTree as ET

def get_addon_info(addon_dir):
    xml_path = os.path.join(addon_dir, 'addon.xml')
    if not os.path.exists(xml_path):
        return None, None
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return root.attrib['id'], root.attrib['version']

def create_package(addon_dir):
    addon_id, version = get_addon_info(addon_dir)
    if not addon_id:
        return
    
    output_filename = f"{addon_id}-{version}.zip"
    print(f"Packaging {addon_id} v{version}...")
    
    excludes = [".git", "__pycache__", ".DS_Store", "brain", ".gemini", ".idea", ".vscode"]
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(addon_dir):
            dirs[:] = [d for d in dirs if d not in excludes]
            for file in files:
                if file in excludes or any(file.endswith(ext) for ext in [".pyc", ".pyo"]):
                    continue
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, os.path.join(addon_dir, ".."))
                zipf.write(abs_path, rel_path)
    print(f"  Saved: {output_filename}")

if __name__ == "__main__":
    for item in os.listdir('.'):
        if os.path.isdir(item) and os.path.exists(os.path.join(item, 'addon.xml')):
            create_package(item)
