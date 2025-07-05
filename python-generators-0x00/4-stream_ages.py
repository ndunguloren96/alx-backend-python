#!/usr/bin/python3

import seed

def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    connection = None
    cursor = None
    try:
        connection = seed.connect_to_prodev()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT age FROM user_data")
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                yield float(row[0])
    except Exception as e:
        print(f"Error streaming user ages: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def calculate_average_age():
    """
    Calculates the average age of users without loading the entire dataset into memory.
    Uses the stream_user_ages generator.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No user data found to calculate average age.")

if __name__ == '__main__':
    calculate_average_age()
