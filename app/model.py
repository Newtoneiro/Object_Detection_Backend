"""
This file defines all of the model related functionalities.
"""


from ultralytics import YOLO
from app.config import MODEL_PATH


model = YOLO(MODEL_PATH)
