import requests
import re

def wiki_url_img(url):
    try:
        html = requests.get(url).text
        src_regex = re.compile(r'<img src="(.*?)"')
        
        match = src_regex.search(html)
        
        if match and match.group(1):
            img_url = match.group(1)
            # Processing the image URL to remove '/thumb' and get the correct URL part
            img_url = img_url[:img_url.rfind("/")].replace("/thumb", "")
            print(f"{url} : {img_url}")
            return img_url.replace("//", "")
        else:
            print("No src attribute found.")
            return "No image"
    except Exception as e:
        print(e)
        return "No image"
    


    import requests
import re

def wiki_url_img(url):
    try:
        html = requests.get(url).text
        src_regex = re.compile(r'<img src="(.*?)"')
        
        match = src_regex.search(html)
        
        if match and match.group(1):
            img_url = match.group(1)
            # Processing the image URL to remove '/thumb' and get the correct URL part
            img_url = img_url[:img_url.rfind("/")].replace("/thumb", "")
            print(f"{url} : {img_url}")
            return img_url.replace("//", "")
        else:
            print("No src attribute found.")
            return "No image"
    except Exception as e:
        print(e)
        return "No image"



wiki_url_img("https://en.wikipedia.org/wiki/Kansas_Saloon_Smashers")


import csv
import uuid
input_file_path="data/plots.csv"

with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile:
    data = []
    reader = csv.reader(infile)
    headers = next(reader) + ['image']
    data.append(headers)
    for row in reader:
        url = row[6]
        img = wiki_url_img(url)
        row.append(img)
        data.append(row)

        print(f"processed {len(data)} records...")    
        if len(data) % 5000 == 0:
            output_file_path = f"data/plot_{str(uuid.uuid4())}.csv"
            with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(data)
                data = []
                data.append(headers)

    if len(data)>0:
        output_file_path = f"data/plot_{str(uuid.uuid4())}.csv"
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer.writerows(data)
            writer = csv.writer(outfile)
            data = []
            data.append(headers)             



len(data)
output_file_path = f"data/plot_{str(uuid.uuid4())}.csv"
with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
    data = []
    data.append(headers)


import glob
directory_path = 'data/img_file/*.csv'
csv_files = glob.glob(directory_path)
print(csv_files)

import pandas as pd
df_all = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)


## don't need which have CentralAutoLogin Value
pattern = r'.*\.(jpg|jpeg|png|gif|bmp|tiff|webp|svg)$'
filtered_rows = df_all[df_all['image'].str.contains(pattern,regex=True,case=False)]

