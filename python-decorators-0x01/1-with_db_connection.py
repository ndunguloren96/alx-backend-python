import sqlite3
import functools
import os

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
            print(f"DB Connection opened for {func.__name__}")
            # Pass the connection object as the first argument to the decorated function
            result = func(conn, *args, **kwargs)
            return result
        except sqlite3.Error as e:
            print(f"Database error in {func.__name__}: {e}")
            raise # Re-raise the exception after logging
        finally:
            if conn:
                conn.close()
                print(f"DB Connection closed for {func.__name__}")
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetches a user by their ID from the database using an existing connection.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

#### Fetch user by ID with automatic connection handling
if __name__ == "__main__":
    setup_database(DB_FILE)
    print("\n--- Fetching user by ID with automatic connection handling ---")
    user = get_user_by_id(user_id=1)
    print(f"User with ID 1: {user}")

    user = get_user_by_id(user_id=99) # Non-existent user
    print(f"User with ID 99: {user}")

    print("\n--- Demonstrating error handling (e.g., table not found) ---")
    # This will simulate an error to show the connection closing properly
    @with_db_connection
    def fetch_from_nonexistent_table(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM non_existent_table")
        return cursor.fetchall()

    try:
        fetch_from_nonexistent_table()
    except sqlite3.OperationalError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")

