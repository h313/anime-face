#!/usr/bin/env python3
import io
import os
import requests
import shutil

# Import Google Cloud client libraries
from google.cloud import vision
from google.cloud.vision import types

# Instantiate a client
client = vision.ImageAnnotatorClient()


# Check an image for anime profile picture
def check_image(img_file):
    # Load image into memory
    with io.open(img_file, 'rb') as image_file:
        img_bin = image_file.read()

    # Convert into an image
    image = types.Image(content=img_bin)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    if "Anime" in labels:
        return True
    else:
        return False


# Download profile picture to a specified location
def get_profile_image(url, file_location):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(file_location, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            return file_location


# Test if profile image getter works
def main():
  img = get_profile_image('h313', 'file.png')
  if check_image(img):
    print('is_anime_image')


if __name__ == '__main__':
  main()
