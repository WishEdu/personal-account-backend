import psycopg2
from psycopg2.extras import RealDictCursor
from logging import info

from backend.configs import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST


db = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)

cursor = db.cursor(cursor_factory=RealDictCursor)

info(f'DATABASE LOAD.')
