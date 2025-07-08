import sqlite3
import os

# Define the database file path.
DB_FILE = 'my_database.db'

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
        cursor.execute("INSERT INTO users (name, age) VALUES ('David', 28)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Eve', 45)")
        conn.commit()
        print(f"Database '{db_file}' created and populated with sample data.")
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
    finally:
        if conn:
            conn.close()

class ExecuteQuery:
    """
    A class-based context manager for executing a specific SQL query
    with optional parameters, managing the database connection.
    """

    def __init__(self, db_name, query, params=None):
        """
        Initializes the ExecuteQuery context manager.

        Args:
            db_name (str): The name (path) of the SQLite database file.
            query (str): The SQL query string to be executed.
            params (tuple, optional): A tuple of parameters for the query. Defaults to None.
        """
        self.db_name = db_name
        self.query = query
        self.params = params if params is not None else ()
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        """
        Establishes a database connection, creates a cursor, and executes the query.

        Returns:
            list: The fetched results of the query.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Executing query: '{self.query}' with params: {self.params}")
            self.cursor.execute(self.query, self.params)
            self.result = self.cursor.fetchall()
            return self.result
        except sqlite3.Error as e:
            print(f"Error during query execution: {e}")
            raise # Re-raise the exception to be handled by the caller

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Commits changes (if no exception) or rolls back (if exception),
        and closes the database connection.
        """
        if self.conn:
            if exc_type:
                self.conn.rollback()
                print(f"Transaction rolled back due to exception: {exc_val}")
            else:
                self.conn.commit()
                print("Transaction committed.")
            self.conn.close()
            print(f"Database connection to '{self.db_name}' closed.")
        return False # Propagate exceptions

# --- Main execution block ---
if __name__ == "__main__":
    # Setup the database before using the context manager
    setup_database(DB_FILE)

    print("\n--- Using ExecuteQuery context manager for users older than 25 ---")
    try:
        # Query for users older than 25
        with ExecuteQuery(DB_FILE, "SELECT * FROM users WHERE age > ?", (25,)) as users_over_25:
            print("\nUsers older than 25:")
            if users_over_25:
                for user in users_over_25:
                    print(user)
            else:
                print("No users found older than 25.")

        print("\n--- Using ExecuteQuery context manager for all users (example) ---")
        # Example: Query for all users
        with ExecuteQuery(DB_FILE, "SELECT * FROM users") as all_users:
            print("\nAll users:")
            if all_users:
                for user in all_users:
                    print(user)
            else:
                print("No users found.")

    except sqlite3.Error as e:
        print(f"\nAn SQLite error occurred: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


