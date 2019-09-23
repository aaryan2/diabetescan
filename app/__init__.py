from flask import Flask
import os

application = Flask(__name__, template_folder='../templates')

basedir = os.path.abspath(os.path.dirname(__file__))

from app import routes
