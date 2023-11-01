"""
This file defines all of the global config variables.
"""


import os

# SERVER
HOST = "192.168.119.129"
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
TENSOR_PATH = os.path.join(IMG_FOLDER, "some_tensor.pt")

# SAVED TENSORS EVENT SOURCES
EVENT_SOURCE_CAMERA_MODE = "CAMERA_MODE"
EVENT_SOURCE_LIVE_MODE = "LIVE_MODE"
