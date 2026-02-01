import os
import hashlib
import xml.etree.ElementTree as ET

def generate_repo():
    addons_xml_content = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n"
    
    for item in os.listdir('.'):
        if os.path.isdir(item):
            xml_path = os.path.join(item, 'addon.xml')
            if os.path.exists(xml_path):
                with open(xml_path, 'r', encoding='utf-8') as f:
                    # Skip the XML declaration if present
                    lines = f.readlines()
                    if lines[0].startswith('<?xml'):
                        addons_xml_content += "".join(lines[1:])
                    else:
                        addons_xml_content += "".join(lines)
                addons_xml_content += "\n"

    addons_xml_content += "</addons>"

    with open("addons.xml", "w", encoding='utf-8') as f:
        f.write(addons_xml_content)

    # MD5 hash
    md5_hash = hashlib.md5(addons_xml_content.encode('utf-8')).hexdigest()
    with open("addons.xml.md5", "w") as f:
        f.write(md5_hash)

    # Generate Gothic-themed index.html for Kodi browsing
    # Only show the repository zip to the user to avoid confusion
    files = [f for f in os.listdir('.') if f.startswith('repository.vibestream') or f.startswith('addons.xml')]
    files.sort()
    
    links_html = ""
    for f in files:
        links_html += f'<li><a href="{f}">{f}</a></li>\n'
    
    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>VibeStream Repository</title>
    <link href="https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: #1a1a1a;
            color: #e6e6e6;
            font-family: 'Gothic A1', sans-serif;
            text-align: center;
            padding: 50px;
        }}
        h1 {{
            font-family: 'UnifrakturCook', cursive;
            font-size: 5em;
            color: #ff4c4c;
            margin-bottom: 0.2em;
            text-shadow: 2px 2px 4px #000;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            border: 1px solid #444;
            padding: 30px;
            background: #222;
            box-shadow: 0 0 20px #000;
        }}
        ul {{
            list-style: none;
            padding: 0;
            text-align: left;
            display: inline-block;
        }}
        li {{
            margin: 15px 0;
            font-size: 1.2em;
        }}
        a {{
            color: #ff4c4c;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }}
        a:hover {{
            color: #fff;
            text-shadow: 0 0 10px #ff0000;
        }}
        .divider {{
            height: 2px;
            background: linear-gradient(to right, transparent, #ff4c4c, transparent);
            margin: 30px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>VibeStream</h1>
        <p>The Ultimate Gothic Streaming Repository</p>
        <div class="divider"></div>
        <ul>
            {links_html}
        </ul>
        <div class="divider"></div>
        <p><a href="https://github.com/mritsurgeon/vibestream">View on GitHub</a></p>
    </div>
</body>
</html>"""

    with open("index.html", "w", encoding='utf-8') as f:
        f.write(index_content)

    print("Generated addons.xml, addons.xml.md5, and Gothic index.html")

if __name__ == "__main__":
    generate_repo()
