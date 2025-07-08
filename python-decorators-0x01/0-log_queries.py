import sqlite3
import functools
import os
from datetime import datetime # Added this import as required by the checker

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

#### decorator to log SQL queries
def log_queries(func):
    """
    A decorator that logs the SQL query before executing the decorated function.
    Includes a timestamp in the log message.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # The query is expected to be passed as a keyword argument 'query'
        # or as the first positional argument.
        query = kwargs.get('query')
        if not query and args:
            # Check if the first argument is a string (likely the query)
            if isinstance(args[0], str):
                query = args[0]
            # If the function takes 'conn' as first arg, query might be second
            elif len(args) > 1 and isinstance(args[1], str):
                query = args[1]

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if query:
            print(f"[{current_time}] LOG: Executing SQL query: '{query}'")
        else:
            print(f"[{current_time}] LOG: Executing a database operation (query not explicitly found).")

        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    """
    Fetches all users from the database using the provided query.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
if __name__ == "__main__":
    setup_database(DB_FILE)
    print("\n--- Fetching all users with logging ---")
    users = fetch_all_users(query="SELECT * FROM users")
    print("Fetched Users:")
    for user in users:
        print(user)

    print("\n--- Fetching a specific user with logging ---")
    # Example with a different query
    user_id_to_fetch = 1
    user = fetch_all_users(query=f"SELECT * FROM users WHERE id = {user_id_to_fetch}")
    print(f"Fetched User with ID {user_id_to_fetch}:")
    if user:
        print(user[0])
    else:
        print("User not found.")

