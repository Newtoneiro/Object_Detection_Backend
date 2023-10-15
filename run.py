"""
This is the main file to run in order to start the server.
"""

from app import app
import firebase_admin

from app.config import HOST, PORT, SDK_PATH


def initialize_firebase() -> None:
    """Initialize firebase with the SDK file given in config."""
    cred = firebase_admin.credentials.Certificate(SDK_PATH)
    firebase_admin.initialize_app(cred)


if __name__ == "__main__":
    """
    Main script. Initializes the firebase app and runs flask server on
    [HOST]:[PORT] defined in config.
    """
    initialize_firebase()
    print(f"Server will be running on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)
