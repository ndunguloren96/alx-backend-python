import time
import sqlite3
import functools
import os
import random

# Define the database file path
DB_FILE = 'users.db'

# --- Helper function to set up the database for testing ---
def setup_database(db_file):
    """
    Sets up a simple SQLite database with a 'users' table and some data.
    Ensures the database is fresh for testing.
    """
    if os.path.exists(db_file):
        os.remove(db_file) # Remove existing DB to start fresh
        print(f"Removed existing database: {db_file}")

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')

        # Insert some sample data
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 22)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
        conn.commit()
        print(f"Database '{db_file}' created and populated with sample data.")
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
    finally:
        if conn:
            conn.close()

#### with_db_connection decorator (copied from Task 1)
def with_db_connection(func):
    """
    A decorator that handles opening and closing a database connection.
    It passes the connection object as the first argument to the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        try:
            conn = sqlite3.connect(DB_FILE)
            # print(f"DB Connection opened for {func.__name__}") # Optional: for debugging
            result = func(conn, *args, **kwargs)
            return result
        except sqlite3.Error as e:
            print(f"Database error in {func.__name__}: {e}")
            raise # Re-raise the exception after logging
        finally:
            if conn:
                # print(f"DB Connection closed for {func.__name__}") # Optional: for debugging
                conn.close()
    return wrapper

#### retry_on_failure decorator
def retry_on_failure(retries=3, delay=2):
    """
    A decorator that retries the decorated function a certain number of times
    if it raises an exception.

    Args:
        retries (int): The maximum number of times to retry the function.
        delay (int): The delay in seconds between retries.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries + 1): # +1 to include the initial attempt
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i < retries:
                        print(f"Attempt {i+1}/{retries+1} failed for {func.__name__}: {e}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"Attempt {i+1}/{retries+1} failed for {func.__name__}: {e}. No more retries.")
                        raise # Re-raise the last exception if all retries fail
        return wrapper
    return decorator

# Global counter to simulate transient failures for testing
_fetch_attempt_count = 0

@with_db_connection
@retry_on_failure(retries=3, delay=1) # Reduced delay for quicker testing
def fetch_users_with_retry(conn):
    """
    Fetches all users from the database.
    Simulates a transient failure for demonstration purposes.
    """
    global _fetch_attempt_count
    _fetch_attempt_count += 1
    print(f"Inside fetch_users_with_retry, attempt {_fetch_attempt_count}")

    # Simulate a transient error for the first 2 attempts
    if _fetch_attempt_count <= 2:
        print("Simulating a temporary database connection error...")
        raise sqlite3.OperationalError("Database is temporarily unavailable.")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
if __name__ == "__main__":
    setup_database(DB_FILE)
    print("\n--- Attempting to fetch users with automatic retry on failure ---")
    try:
        users = fetch_users_with_retry()
        print("\nFetched Users Successfully:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"\nFailed to fetch users after multiple retries: {e}")

    # Reset attempt count for another test if needed
    _fetch_attempt_count = 0
    print("\n--- Testing retry with a different scenario (e.g., permanent error) ---")
    @with_db_connection
    @retry_on_failure(retries=2, delay=1)
    def fetch_from_nonexistent_table_with_retry(conn):
        global _fetch_attempt_count
        _fetch_attempt_count += 1
        print(f"Inside fetch_from_nonexistent_table_with_retry, attempt {_fetch_attempt_count}")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM non_existent_table") # This will always fail
        return cursor.fetchall()

    try:
        fetch_from_nonexistent_table_with_retry()
    except sqlite3.OperationalError as e:
        print(f"\nCaught expected permanent error after retries: {e}")
    except Exception as e:
        print(f"\nCaught unexpected error: {e}")

