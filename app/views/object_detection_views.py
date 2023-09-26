from app import app
from app import error_codes
from app.utils import token_required

from flask import request
from flask_sock import Sock
import base64
import cv2
from ultralytics import YOLO

liveDetectionSock = Sock(app)

model = YOLO("yolov8n.pt")


MAIN_PATH = "/objectDetection/"


@app.route(f"{MAIN_PATH}capturePhoto", methods=["POST"])
@token_required
def serve_capturePhoto():
    try:
        req_data = request.get_json()
        file = req_data['file']
        doSave = req_data['doSave']
    except KeyError:
        return error_codes.BAD_REQUEST, 400

    imgdata = base64.b64decode(file)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    results = model.predict("some_image.jpg")
    results_json = results[0].tojson(normalize=True)

    if (doSave):
        predicted_image = results[0].plot()
        cv2.imwrite('./some_prediction.jpg', predicted_image)

    return results_json, 200
