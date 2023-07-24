from app import app
from flask import request
import base64
import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")


MAIN_PATH = "/objectDetection/"


@app.route(f"{MAIN_PATH}capturePhoto", methods=["POST"])
def serve_capturePhoto():
    data = request.json
    file = data['file']
    imgdata = base64.b64decode(file)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    results = model.predict("some_image.jpg")
    results_json = results[0].tojson(normalize=True)

    predicted_image = results[0].plot()
    cv2.imwrite('./some_prediction.jpg', predicted_image)
    return results_json
