#!/usr/bin/python3
import seed
from psycopg2.extras import RealDictCursor

def paginate_users(page_size, offset):
    """
    Fetches a single page of user data from the database.
    """
    connection = None
    cursor = None
    try:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Error in paginate_users: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def lazy_pagination(page_size):
    """
    Generator function that lazily loads pages of user data.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
