from flask import Flask, request, jsonify
import base64
from ultralytics import YOLO
import cv2

HOST = "10.1.7.78"
PORT = 8888
app = Flask(__name__)
model = YOLO("yolov8n.pt")


@app.route("/", methods=["GET"])
def serve_home():
    return jsonify({
        'response': "Connected to backend."
    })


@app.route("/capturePhoto", methods=["POST"])
def serve_sampleResponse():
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


if __name__ == "__main__":
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)
