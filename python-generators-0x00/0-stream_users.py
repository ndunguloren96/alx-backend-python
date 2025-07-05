#!/usr/bin/python3

import seed
from psycopg2.extras import RealDictCursor

def stream_users():
    """
    Uses a generator to fetch rows one by one from the user_data table.
    Yields each row as a dictionary.
    """
    connection = None
    cursor = None
    try:
        connection = seed.connect_to_prodev()
        if connection:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT user_id, name, email, age FROM user_data")

            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                yield row
    except Exception as e:
        print(f"Error streaming users: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
