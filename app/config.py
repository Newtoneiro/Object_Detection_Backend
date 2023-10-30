"""
This file defines all of the global config variables.
"""


import os

# SERVER
HOST = "192.168.169.5"
PORT = 8888

# STATIC FILES
STATIC_FOLDER = './static'
MODEL_PATH = os.path.join(STATIC_FOLDER, "yolov8n.pt")

# FIREBASE
SDK_PATH = './firebase-sdk.json'

# PHOTO MODE
IMG_FOLDER = "./saved_images"
IMG_PATH = os.path.join(IMG_FOLDER, "some_image.jpg")
PRED_PATH = os.path.join(IMG_FOLDER, "some_prediction.jpg")
