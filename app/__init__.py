# flake8: noqa
from flask import Flask

app = Flask(__name__)

from app import utils
from app import views
from app import object_detection_views
from app import auth_views