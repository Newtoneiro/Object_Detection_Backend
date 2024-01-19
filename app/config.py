"""
This file defines all of the global config variables.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# SERVER
HOST = os.environ['SERVER_API_ADDRESS']
PORT = int(os.environ['SERVER_API_PORT'])

# STATIC FILES
STATIC_FOLDER = './static'
MODEL_PATH = os.path.join(STATIC_FOLDER, "yolov8n.pt")

# FIREBASE
SDK_PATH = './firebase-sdk.json'

# FIRESTORE
TENSOR_COLLECTION = "storedTensors"

# CAMERA MODE
SAVED_IMAGE_RESCALE = (152, 200)  # (w, h)

# LIVE MODE

# == if all pixel values are lower than this ==
# == the tensor represents black image       ==
TENSOR_DISCARD_TRESHOLD = 35

# SAVED TENSORS EVENT SOURCES
EVENT_SOURCE_CAMERA_MODE = "CAMERA_MODE"
EVENT_SOURCE_LIVE_MODE = "LIVE_MODE"
