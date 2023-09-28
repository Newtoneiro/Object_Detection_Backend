from flask import send_from_directory
from app import app


MAIN_PATH = "/"


@app.route(f"{MAIN_PATH}", methods=['GET'])
def serve_home():
    return 'Hello', 200


# serve model

@app.route(f"{MAIN_PATH}/getModelJSON/<path:filename>", methods=['GET'])
def serve_model_json(filename):
    return send_from_directory(app.static_folder, f'model/{filename}')
