import psycopg2
import os

def get_db_connection():
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://epl_db_user:F3WChu5Rbbre8RVPzrldMe42Qm3hSCPw@dpg-d43gpkemcj7s73b2o8b0-a/epl_db")
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    return conn
