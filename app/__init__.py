# flake8: noqa
from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')

from app import views
from app import utils
from app import error_codes