import re

def replace_floorfy_paths(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Match: /equirectangular_<id>_<hash>/fallback/<file>
    pattern = r"/equirectangular_(\d+)_([a-z0-9]+)/fallback/([^\"'\s]+)"
    
    # Replace with: /skybox_<id>_<hash>_<file>
    replaced_content = re.sub(pattern, r"/skybox_\1_\2_\3", content)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(replaced_content)

# Example:
replace_floorfy_paths("cfg_2384270.json")
