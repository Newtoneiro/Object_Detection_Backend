# flake8: noqa
from flask import Flask

app = Flask(__name__)

from app import views
from app import utils
from app import error_codes