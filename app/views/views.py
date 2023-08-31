from app import app


MAIN_PATH = "/"


@app.route(MAIN_PATH, methods=["GET"])
def serve_home():
    return "Hello", 200
