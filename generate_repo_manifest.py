import os
import hashlib

def generate_repo():
    repo_dir = "packages"
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)

    addon_xml_path = "plugin.video.fenlight/addon.xml"
    with open(addon_xml_path, 'r') as f:
        addon_xml = f.read()

    # Simple addons.xml generation
    addons_xml_content = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n"
    addons_xml_content += addon_xml
    addons_xml_content += "\n</addons>"

    with open("addons.xml", "w") as f:
        f.write(addons_xml_content)

    # MD5 hash
    md5_hash = hashlib.md5(addons_xml_content.encode('utf-8')).hexdigest()
    with open("addons.xml.md5", "w") as f:
        f.write(md5_hash)

    print("Generated addons.xml and addons.xml.md5")

if __name__ == "__main__":
    generate_repo()
