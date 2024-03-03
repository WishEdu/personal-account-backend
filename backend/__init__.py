from os import getenv
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

load_dotenv()

app = Flask('WISH')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['ALLOWED_HOSTS'] = getenv('ALLOWED_HOSTS').split()

CORS(app, origins=app.config['ALLOWED_HOSTS'])
socketio = SocketIO(app, cors_allowed_origins=app.config['ALLOWED_HOSTS'])



