import requests
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime

def get_html_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve HTML source. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to retrieve HTML source: {e}")
    return None

def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded successfully and saved at: {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to download image: {e}")

today = datetime.today().strftime('%Y%m%d')
print("Today is " + str(today))
url = "https://soho.nascom.nasa.gov/data/REPROCESSING/Completed/2024/c3/" + str(today) + "/"
html_source = get_html_source(url)
full_links = []
image_names = []
if html_source:
    # print(html_source)
    html_lines = html_source.split("\n")

    for line in html_lines:
        if "_c3_1024.jpg" in line:
            full_links.append(url + line[107:132])
            image_names.append(line[107:132])

else:
    quit()

already_files = [f for f in listdir("./") if isfile(join("./", f))]

for idx, link in enumerate(full_links):
    if not image_names[idx] in already_files:
        print("Downloading", image_names[idx])
        download_image(link, image_names[idx])
    
print("Done!")
