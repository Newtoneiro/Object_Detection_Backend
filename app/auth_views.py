from app import app
from flask import request
from firebase_admin import auth


MAIN_PATH = "/auth/"


@app.route(f"{MAIN_PATH}verifyToken", methods=["POST"])
def serve_verifyToken():
    try:
        req_data = request.get_json()
        token = req_data['token']
    except KeyError:
        return "Bad Request.", 400

    try:
        auth.verify_id_token(token)
        return "Valid Token.", 200
    except Exception as e:
        print(e)
        return "Invalid JWT token.", 400
