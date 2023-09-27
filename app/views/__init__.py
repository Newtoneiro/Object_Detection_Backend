# flake8: noqa
from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')

from app.views import object_detection_views
from app.views import auth_views
from app.views import views