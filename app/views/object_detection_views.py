"""This file contains the endpoint related to object detection."""

from app import app
from app import error_codes
from app.utils import token_required

from flask import request
import base64
import cv2
from ultralytics import YOLO
from app.config import IMG_PATH, PRED_PATH


model = YOLO("yolov8n.pt")


MAIN_PATH = "/objectDetection/"


@app.route(f"{MAIN_PATH}capturePhoto", methods=["POST"])
@token_required
def serve_capturePhoto() -> tuple:
    """
    [Token required] Endpoint responsible for receiving the
    image, making predictions and returning them in response.

    Returns:
        tuple(tuple): tuple containing:

            Error signature(str): If request is invalid, else None.
            Status Code(int): Server status code.
    """
    try:
        req_data = request.get_json()
        file = req_data['file']
        doSave = req_data['doSave']
    except KeyError:
        return error_codes.BAD_REQUEST, 400

    imgdata = base64.b64decode(file)
    with open(IMG_PATH, 'wb') as f:
        f.write(imgdata)
    results = model.predict(IMG_PATH)
    results_json = results[0].tojson(normalize=True)

    if (doSave):
        predicted_image = results[0].plot()
        cv2.imwrite(PRED_PATH, predicted_image)

    return results_json, 200
