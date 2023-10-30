"""
This file contains the endpoint related to object detection.

ROUTE = "/objectDetection/"
"""

import torch
from app import app
from app import error_codes
from app.utils import token_required

from flask import request
import base64
import cv2
from app.config import IMG_PATH, PRED_PATH, TENSOR_PATH
from app.model import model


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


@app.route(f"{MAIN_PATH}captureTensor", methods=["POST"])
@token_required
def serve_captureTensor() -> tuple:
    """
    [Token required] Endpoint responsible for receiving the
    tensor and saving it in user's database.

    Returns:
        tuple(tuple): tuple containing:

            Error signature(str): If request is invalid, else None.
            Status Code(int): Server status code.
    """
    try:
        req_data = request.get_json()
        shape = req_data['shape']
        values = req_data['values']
    except KeyError:
        return error_codes.BAD_REQUEST, 400

    tensor = torch.tensor(data=[values],
                          dtype=torch.int16).squeeze()  # remove additional dim
    tensor = torch.flip(tensor, [1])  # flip the image
    assert tensor.shape == torch.Size(shape)

    torch.save(tensor, TENSOR_PATH)

    return "", 200
