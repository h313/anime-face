import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()


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
