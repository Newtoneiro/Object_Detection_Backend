"""This file contains the endpoint related to user authentication."""

from app import app
from app import error_codes

from firebase_admin import auth
from flask import request


MAIN_PATH = "/auth/"


@app.route(f"{MAIN_PATH}verifyToken", methods=["POST"])
def serve_verifyToken() -> tuple:
    """
    Endpoint responsible for receiving the token and
    verifying it via Firebase.

    Returns:
        (tuple): tuple containing:

            Error Signature(str): If token is invalid, else the
                output of wrapped function.
            Status Code(int): Server status code.
    """
    try:
        req_data = request.get_json()
        token = req_data['token']
    except KeyError:
        return error_codes.BAD_REQUEST, 400

    try:
        auth.verify_id_token(token)
    except auth.ExpiredIdTokenError:
        return error_codes.JWT_EXPIRED, 401
    except auth.InvalidIdTokenError:
        return error_codes.JWT_INVALID, 401
    except Exception:
        return error_codes.JWT_OTHER, 401

    return "", 200
