import io
import os
import requests

# Import Google Cloud client libraries
from google.cloud import vision
from google.cloud.vision import types

# Import Graphene
from graphene import ObjectType, String, Schema

# Instantiate a client
client = vision.ImageAnnotatorClient()

# Check an image for anime profile picture
def check_image(img_bin):
    # Convert into an image
    image = types.Image(content=img_bin)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    if "Anime" in labels:
        return True
    else:
        return False


def get_profile_image(username):
  r = requests.get('https://github.com/' + username + '.png', stream=True)
  if r.status_code == 200:
    return r.raw

def main():
  img = get_profile_image('h313')
  if check_image(img):
    print('is_anime_image')

if __name__ == '__main__':
  main()
