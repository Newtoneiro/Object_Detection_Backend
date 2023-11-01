"""
This file contains the endpoint related to object detection.

ROUTE = "/objectDetection/"
"""

from dataclasses import dataclass
import torch
from app import app
from app import error_codes
from app.utils import token_required

from flask import request
import base64
import cv2
from app.config import IMG_PATH, PRED_PATH, TENSOR_PATH, EVENT_SOURCE_LIVE_MODE
from app.model import model
from firebase_admin import firestore
import datetime


MAIN_PATH = "/objectDetection/"


@dataclass
class StoredTensor:
    """Class representing FireStore collection object of the same name."""
    user_id: str
    timestamp: str
    event_source: str
    flattened_tensor: str
    tensor_shape: list


@app.route(f"{MAIN_PATH}capturePhoto", methods=["POST"])
@token_required
def serve_capturePhoto(user: dict) -> tuple:
    """
    [Token required] Endpoint responsible for receiving the
    image, making predictions and returning them in response.

    Args:
        user (dict): info about current user.

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
def serve_captureTensor(user: dict) -> tuple:
    """
    [Token required] Endpoint responsible for receiving the
    tensor and saving it in user's database.

    Args:
        user (dict): info about current user.

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

    try:
        db = firestore.client()
        tensor_object = StoredTensor(
            user_id=user["user_id"],
            timestamp=datetime.datetime.now(),
            flattened_tensor=tensor.view(-1).numpy().tolist(),
            tensor_shape=shape,
            event_source=EVENT_SOURCE_LIVE_MODE
        )
        new_tensor_ref = db.collection("storedTensors").document()
        new_tensor_ref.set(tensor_object.__dict__)

    except Exception:
        return error_codes.FIRESTORE_ERROR, 500

    return "", 200
