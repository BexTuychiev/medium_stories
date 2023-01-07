import requests
from skimage.io import imread

endpoint = "https://pet-pawpularity.herokuapp.com/predict"

# Load a sample image
img = imread("data/raw/train/0a4f658ae77b7e4209e22b79fe1c28cb.jpg")

response = requests.post(endpoint, headers={"content-type": "text/plain"},
                         data=str(img))

print(response.text)