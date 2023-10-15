"""
Views module __init__ file.
"""

# flake8: noqa
from flask import Flask

app = Flask(__name__)

from app.views import object_detection_views
from app.views import auth_views
from app.views import views