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

# FIRESTORE
TENSOR_COLLECTION = "storedTensors"

# CAMERA MODE
SAVED_IMAGE_RESCALE = (152, 200)  # (w, h)

# SAVED TENSORS EVENT SOURCES
EVENT_SOURCE_CAMERA_MODE = "CAMERA_MODE"
EVENT_SOURCE_LIVE_MODE = "LIVE_MODE"
