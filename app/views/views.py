"""
This file contains the endpoints related to default route.
(Mainly testing purposes)

ROUTE = "/"
"""

from app import app


MAIN_PATH = "/"


@app.route(MAIN_PATH, methods=["GET"])
def serve_home() -> tuple:
    """
    Sample endpoint returning hardcoded response.

    Returns:
        tuple(tuple): tuple containing:

            Response(str): Hardcoded response.
            Status Code(int): Server status code.
    """
    return "Hello", 200
