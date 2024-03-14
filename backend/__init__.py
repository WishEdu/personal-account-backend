from os import getenv

import flask
from dotenv import load_dotenv
import logging
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

load_dotenv()

app = Flask('WISH')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['ALLOWED_HOSTS'] = getenv('ALLOWED_HOSTS').split()

CORS(app, origins=app.config['ALLOWED_HOSTS'])
socketio = SocketIO(app, cors_allowed_origins=app.config['ALLOWED_HOSTS'])

logging.basicConfig(level=logging.INFO, filename="backend_lk.log", format="%(asctime)s %(levelname)s %(message)s")


from backend.account import account_bp
app.register_blueprint(account_bp)

from backend.email import email_bp
app.register_blueprint(email_bp)
