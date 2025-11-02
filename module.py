from database import get_db_connection

def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            mobile VARCHAR(20),
            password VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_logs_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            email VARCHAR(100),
            activity TEXT,
            page_name TEXT,
            ip_address TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def log_user_activity(email, activity, page_name, ip_address):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (email, activity, page_name, ip_address)
        VALUES (%s, %s, %s, %s)
    """, (email, activity, page_name, ip_address))
    conn.commit()
    cursor.close()
    conn.close()
