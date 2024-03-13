from os import getenv
from dotenv import load_dotenv

import psycopg2
from psycopg2.extras import RealDictCursor
from logging import info


load_dotenv()

db = psycopg2.connect(
    database=getenv('DB_NAME'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    host=getenv('DB_HOST')
)

cursor = db.cursor(cursor_factory=RealDictCursor)

info(f'DATABASE LOAD.')
