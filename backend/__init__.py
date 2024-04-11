import logging
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from .configs import SECRET_KEY, ALLOWED_HOSTS

app = Flask('WISH')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['ALLOWED_HOSTS'] = ALLOWED_HOSTS.split()

CORS(app, origins=app.config['ALLOWED_HOSTS'])
socketio = SocketIO(app, cors_allowed_origins=app.config['ALLOWED_HOSTS'])

logging.basicConfig(level=logging.INFO, filename="backend_lk.log", format="%(asctime)s %(levelname)s %(message)s")


from .account import account_bp
app.register_blueprint(account_bp)

from .email import email_bp
app.register_blueprint(email_bp)

from .info import info_bp
app.register_blueprint(info_bp)