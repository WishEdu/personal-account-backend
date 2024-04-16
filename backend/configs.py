from dotenv import load_dotenv, find_dotenv

from os import getenv


load_dotenv(find_dotenv())

# DATABASE SOURCE
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')

# NETWORK SETTINGS
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS')
CLOUD_HOST = getenv('CLOUD_HOST')
FRONTEND_HOST = getenv('FRONTEND_HOST')

# PROJECT SETTINGS
SECRET_KEY = getenv('SECRET_KEY')

# EMAIL SOURCE
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD')
SENDER_NAME = getenv('SENDER_NAME')