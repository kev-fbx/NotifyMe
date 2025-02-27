import psycopg2
from config import DATABASE


def get_db_connection():
    conn = psycopg2.connect(
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    return conn


def insert_user(email, phone, pw_hash):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO public.profile (email, phone, pw_hash) VALUES (%s, %s, %s)",
            (email, phone, pw_hash)
        )

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error inserting user: {e}")
        if conn:
            conn.rollback()
        raise
