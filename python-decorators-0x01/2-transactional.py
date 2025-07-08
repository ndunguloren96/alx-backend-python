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
    Adds an 'email' column for this task.
    """
    if os.path.exists(db_file):
        os.remove(db_file) # Remove existing DB to start fresh
        print(f"Removed existing database: {db_file}")

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create users table with an email column
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT
            )
        ''')

        # Insert some sample data
        cursor.execute("INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com')")
        cursor.execute("INSERT INTO users (name, age, email) VALUES ('Bob', 22, 'bob@example.com')")
        cursor.execute("INSERT INTO users (name, age, email) VALUES ('Charlie', 35, 'charlie@example.com')")
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
            # Pass the connection object as the first argument to the decorated function
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

#### transactional decorator
def transactional(func):
    """
    A decorator that wraps a function running a database operation inside a transaction.
    If the function raises an error, it rolls back; otherwise, it commits the transaction.
    Assumes the decorated function receives a 'conn' object as its first argument.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        # Try to find the connection object from args. It's assumed to be the first arg.
        if args and isinstance(args[0], sqlite3.Connection):
            conn = args[0]
        else:
            # This transactional decorator expects with_db_connection to provide the conn.
            # If not, it might need to open its own connection or raise an error.
            # For this task, we assume it's used with @with_db_connection.
            raise TypeError("Transactional decorator expects 'conn' as the first argument.")

        try:
            # Ensure autocommit is off for explicit transaction management
            conn.isolation_level = None # This sets the connection to manual commit mode
            cursor = conn.cursor() # Get a cursor if needed by the decorated function

            result = func(*args, **kwargs) # Execute the decorated function
            conn.commit()
            print(f"Transaction committed for {func.__name__}.")
            return result
        except Exception as e:
            if conn:
                conn.rollback()
                print(f"Transaction rolled back for {func.__name__} due to error: {e}")
            raise # Re-raise the exception after rollback
        finally:
            # Reset isolation level to default (or whatever is appropriate for your app)
            # Or simply let with_db_connection close the connection
            pass

    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Updates a user's email. This function will be wrapped in a transaction.
    """
    cursor = conn.cursor()
    print(f"Attempting to update user ID {user_id} email to {new_email}...")
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    if cursor.rowcount == 0:
        print(f"No user found with ID {user_id}.")
        # Optionally raise an error if user not found, to trigger rollback
        # raise ValueError(f"User with ID {user_id} not found.")
    else:
        print(f"User ID {user_id} email updated successfully (pending commit).")

@with_db_connection
@transactional
def create_user_and_fail(conn, name, age, email):
    """
    Attempts to create a user and then intentionally raises an error
    to demonstrate transaction rollback.
    """
    cursor = conn.cursor()
    print(f"Attempting to create user '{name}' and then fail...")
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    print(f"User '{name}' inserted (pending commit). Now raising an error...")
    raise ValueError("Simulated error during user creation!")


#### Update user's email with automatic transaction handling
if __name__ == "__main__":
    setup_database(DB_FILE)
    print("\n--- Updating user email (successful transaction) ---")
    try:
        update_user_email(user_id=1, new_email='alice.new@example.com')
        # Verify the update
        conn_check = sqlite3.connect(DB_FILE)
        cursor_check = conn_check.cursor()
        cursor_check.execute("SELECT * FROM users WHERE id = 1")
        print(f"User 1 after successful update: {cursor_check.fetchone()}")
        conn_check.close()
    except Exception as e:
        print(f"Error during successful update test: {e}")


    print("\n--- Attempting to create user and fail (transaction rollback) ---")
    try:
        create_user_and_fail(name='Frank', age=28, email='frank@example.com')
    except ValueError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error during failed creation: {e}")
    finally:
        # Verify that 'Frank' was NOT added to the database
        conn_check = sqlite3.connect(DB_FILE)
        cursor_check = conn_check.cursor()
        cursor_check.execute("SELECT * FROM users WHERE name = 'Frank'")
        frank_user = cursor_check.fetchone()
        print(f"User 'Frank' after failed creation attempt: {frank_user} (should be None)")
        conn_check.close()


