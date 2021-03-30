import re
import os
import glob
import zipfile
import requests
from urllib.request import urlretrieve
import json

article_id = 14096681
url = f"https://api.figshare.com/v2/articles/{article_id}"
headers = {"Content-Type": "application/json"}
output_directory = "data/"

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)
files = data["files"]

for file in files:
    if file["name"] == "data.zip":
        os.makedirs(output_directory, exist_ok=True)
        urlretrieve(file["download_url"], output_directory + file["name"])

with zipfile.ZipFile(os.path.join(output_directory, "data.zip"), 'r') as f:
    f.extractall(output_directory)