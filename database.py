import psycopg2
import psycopg2.extras
import os

def get_db_connection():
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://epl_db_user:F3WChu5Rbbre8RVPzrldMe42Qm3hSCPw@dpg-d43gpkemcj7s73b2o8b0-a.oregon-postgres.render.com/epl_db?sslmode=require"
    )

    # Use RealDictCursor so query results are dictionaries, not tuples
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    conn.autocommit = True
    return conn
