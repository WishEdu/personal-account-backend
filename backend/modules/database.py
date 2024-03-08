from os import getenv
from dotenv import load_dotenv

import psycopg2
from psycopg2.extras import RealDictCursor


load_dotenv()

db = psycopg2.connect(
    database=getenv('DB_NAME'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    host=getenv('DB_HOST')
)

cursor = db.cursor(cursor_factory=RealDictCursor)

print(f'[INFO] DATABASE LOAD.')
