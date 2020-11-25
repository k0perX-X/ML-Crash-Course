from flask import Flask
import os.path

test = Flask(__name__, template_folder=os.path.abspath('test'), static_folder=os.path.abspath('Anime'))

from test import z1