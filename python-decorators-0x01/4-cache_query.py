import time
import sqlite3
import functools
import os

# Define the database file path
DB_FILE = 'users.db'

# Global dictionary to store cached query results
query_cache = {}

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

#### cache_query decorator
def cache_query(func):
    """
    A decorator that caches query results based on the SQL query string
    and its parameters.
    Assumes the decorated function takes 'conn' as the first arg and 'query' as a keyword arg.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        params = kwargs.get('params', ()) # Get parameters if any, default to empty tuple

        # Create a unique cache key based on the query and its parameters
        cache_key = (query, tuple(params))

        if cache_key in query_cache:
            print(f"CACHE HIT for query: '{query}' with params: {params}")
            return query_cache[cache_key]
        else:
            print(f"CACHE MISS for query: '{query}' with params: {params}. Executing query...")
            result = func(*args, **kwargs) # Execute the original function
            query_cache[cache_key] = result # Cache the result
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query, params=None):
    """
    Fetches users from the database. This function's results will be cached.
    """
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchall()

#### Main execution block
if __name__ == "__main__":
    setup_database(DB_FILE)

    print("\n--- First call: will execute query and cache result ---")
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print("Fetched Users (first call):")
    for user in users:
        print(user)
    print(f"Cache size: {len(query_cache)}")

    print("\n--- Second call: will use the cached result ---")
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print("Fetched Users (second call, from cache):")
    for user in users_again:
        print(user)
    print(f"Cache size: {len(query_cache)}")

    print("\n--- Third call: a different query, will execute and cache ---")
    users_over_25 = fetch_users_with_cache(query="SELECT * FROM users WHERE age > ?", params=(25,))
    print("Fetched Users (age > 25, third call):")
    for user in users_over_25:
        print(user)
    print(f"Cache size: {len(query_cache)}")

    print("\n--- Fourth call: same different query, will use cache ---")
    users_over_25_again = fetch_users_with_cache(query="SELECT * FROM users WHERE age > ?", params=(25,))
    print("Fetched Users (age > 25, fourth call, from cache):")
    for user in users_over_25_again:
        print(user)
    print(f"Cache size: {len(query_cache)}")

    # Clear cache for demonstration purposes
    query_cache.clear()
    print("\nCache cleared.")
    print(f"Cache size: {len(query_cache)}")

    print("\n--- Fifth call: after cache clear, will execute again ---")
    users_after_clear = fetch_users_with_cache(query="SELECT * FROM users")
    print("Fetched Users (after cache clear):")
    for user in users_after_clear:
        print(user)
    print(f"Cache size: {len(query_cache)}")

