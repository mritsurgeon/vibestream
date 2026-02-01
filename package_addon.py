#!/usr/bin/env python3
import os
import zipfile
import shutil

# Configuration
ADDON_ID = "plugin.video.fenlight"
ADDON_NAME = "VibeStream"
VERSION = "1.0.0"
SOURCE_DIR = "plugin.video.fenlight"
OUTPUT_FILENAME = f"vibestream-{VERSION}.zip"
EXCLUDES = [
    ".git",
    "__pycache__",
    ".DS_Store",
    ".antigravityignore",
    ".idea",
    ".vscode",
    "brain",
    ".gemini"
]

def create_package():
    print(f"Packaging {ADDON_NAME} v{VERSION}...")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory {SOURCE_DIR} not found.")
        return

    with zipfile.ZipFile(OUTPUT_FILENAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            # Apply excludes
            dirs[:] = [d for d in dirs if d not in EXCLUDES]
            
            for file in files:
                if file in EXCLUDES or any(file.endswith(ext) for ext in [".pyc", ".pyo"]):
                    continue
                    
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, os.path.join(SOURCE_DIR, ".."))
                
                print(f"  Adding: {rel_path}")
                zipf.write(abs_path, rel_path)

    print(f"\nDone! Package saved as: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    create_package()
