import json
import os
import requests
import sys

def download_images(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    scenes = data.get("scenes", {})
    
    for scene in scenes.values():
        keys = ['panorama', 'thumbnail', 'r_panorama', 'l_r_panorama', 'cubeMap', 'lowres_cubeMap']
        
        for key in keys:
            if isinstance(scene[key], list):
                for value in scene[key]:
                    download_file(value)
            else:
                download_file(scene[key])

def download_file(value):
    base_url = "https://cdn.floorfy.com/img/properties/89479/2384270/tourimages/"
    file_url = base_url + value.lstrip('/')
    local_path = os.path.join(os.getcwd(), value.lstrip('/'))

    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    response = requests.get(file_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {local_path}")
    else:
        print(f"Failed to download: {file_url}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    download_images(json_file)
