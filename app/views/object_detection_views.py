"""
This file contains the endpoint related to object detection.

ROUTE = "/objectDetection/"
"""

import datetime
import json
import numpy as np
import torch
import base64
import cv2
import torchvision.transforms as transforms
from app import app
from app import error_codes
from app.utils import token_required
from app.config import SAVED_IMAGE_RESCALE, EVENT_SOURCE_LIVE_MODE, \
                       EVENT_SOURCE_CAMERA_MODE, TENSOR_COLLECTION, \
                       TENSOR_DISCARD_TRESHOLD
from app.model import model

from flask import request
from firebase_admin import firestore
from dataclasses import dataclass


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

    np_arr = np.frombuffer(imgdata, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    results = model.predict(img)
    results_json = results[0].tojson(normalize=True)

    if (doSave):
        resized_image = cv2.resize(img, SAVED_IMAGE_RESCALE)
        transform = transforms.ToTensor()
        tensor = transform(resized_image) * 255  # float -> int
        tensor = tensor.to(torch.uint8).permute(1, 2, 0)  # (h, w, d)
        try:
            db = firestore.client()
            tensor_object = StoredTensor(
                user_id=user["user_id"],
                timestamp=datetime.datetime.now(),
                flattened_tensor=json.dumps(
                    tensor.reshape(-1).numpy().tolist()),
                tensor_shape=tensor.shape,
                event_source=EVENT_SOURCE_CAMERA_MODE
            )
            new_tensor_ref = db.collection(TENSOR_COLLECTION).document()
            new_tensor_ref.set(tensor_object.__dict__)
        except Exception:
            return error_codes.FIRESTORE_ERROR, 500

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

            Error signature(str): If request is invalid /
                                  server throws an error,
                                  else None.
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

    if torch.all(tensor < TENSOR_DISCARD_TRESHOLD):
        # The tensor is an useless black image
        return error_codes.TENSOR_INVALID, 400

    try:
        db = firestore.client()
        tensor_object = StoredTensor(
            user_id=user["user_id"],
            timestamp=datetime.datetime.now(),
            flattened_tensor=json.dumps(tensor.view(-1).numpy().tolist()),
            tensor_shape=shape,
            event_source=EVENT_SOURCE_LIVE_MODE
        )
        new_tensor_ref = db.collection(TENSOR_COLLECTION).document()
        new_tensor_ref.set(tensor_object.__dict__)
    except Exception:
        return error_codes.FIRESTORE_ERROR, 500

    return "", 200
