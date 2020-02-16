import io
import os
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"
path = 'banner.jpg'
vision_client = vision.ImageAnnotatorClient()
with io.open(path, 'rb') as image_file:
     content = image_file.read()
     image = types.Image(content=content)
     response = vision_client.text_detection(image=image)
texts = response.text_annotations
for text in texts:
    print(text.description)
