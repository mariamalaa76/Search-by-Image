import os
import pandas as pd
import requests

# Load the CSV file
myFile = pd.read_csv("D:/Camera_images_1.csv")

# Specify the column that contains image URLs
image_column = "Img_Link"

# Create the full path for the download folder
base_path = "D:/Camera_images_1"
download_folder = os.path.join(base_path, "cameras_downloaded_images")
os.makedirs(download_folder, exist_ok=True)

# Loop through the rows and download each image
for index, row in myFile.iterrows():
    image_url = row[image_column]
    image_name = f"image_{index}.jpg"
    image_path = os.path.join(download_folder, image_name)

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {image_name}")
        else:
            print(f"Failed to download: {image_url}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

print("All images have been downloaded successfully!")
