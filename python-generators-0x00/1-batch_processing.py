#!/usr/bin/python3

import seed
from psycopg2.extras import RealDictCursor

def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows from the user_data table in batches.
    """
    connection = None
    cursor = None
    try:
        connection = seed.connect_to_prodev()
        if connection:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            offset = 0
            while True:
                cursor.execute(f"SELECT user_id, name, email, age FROM user_data LIMIT {batch_size} OFFSET {offset}")
                batch = cursor.fetchall()
                if not batch:
                    break
                yield batch
                offset += batch_size
    except Exception as e:
        print(f"Error streaming users in batches: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    Yields filtered users one by one.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user
