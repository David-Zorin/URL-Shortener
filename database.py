import psycopg2
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://MyName:MyPass@localhost:5432/shortener')

#connect, create and return db connection instanse
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except psycopg2.OperationalError as e:
        print(f"Failed to connect to database: {e}")
        raise

#close connection
def close_db_connection(conn):
    if conn:
        conn.close()