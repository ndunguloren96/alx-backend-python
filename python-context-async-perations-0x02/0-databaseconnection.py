import sqlite3
import os

# Define the database file path.
# This ensures the database is created in the same directory as the script.
DB_FILE = 'my_database.db'

class DatabaseConnection:
    """
    A custom class-based context manager for handling SQLite database connections.
    It ensures that the database connection is properly opened and closed,
    even if errors occur during the database operations within the 'with' block.
    """

    def __init__(self, db_name):
        """
        Initializes the DatabaseConnection context manager.

        Args:
            db_name (str): The name (path) of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Enters the runtime context related to this object.
        It establishes a connection to the SQLite database and creates a cursor.

        Returns:
            sqlite3.Cursor: The cursor object for executing SQL queries.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Database connection to '{self.db_name}' opened successfully.")
            return self.cursor
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            # Re-raise the exception to propagate it
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exits the runtime context related to this object.
        It commits any pending transactions and closes the database connection.
        Handles exceptions that might occur within the 'with' block.

        Args:
            exc_type (type): The type of the exception (e.g., ValueError, TypeError).
            exc_val (Exception): The exception instance.
            exc_tb (traceback): A traceback object.

        Returns:
            bool: True if the exception was handled, False otherwise.
        """
        if self.conn:
            if exc_type:
                # An exception occurred inside the 'with' block
                self.conn.rollback()  # Rollback changes if an error occurred
                print(f"Transaction rolled back due to an exception: {exc_val}")
            else:
                # No exception, commit changes
                self.conn.commit()
                print("Transaction committed successfully.")
            self.conn.close()
            print(f"Database connection to '{self.db_name}' closed.")
        return False # False propagates the exception, True suppresses it

# --- Helper function to set up the database for testing ---
def setup_database(db_file):
    """
    Sets up a simple SQLite database with a 'users' table and some data.
    """
    if os.path.exists(db_file):
        os.remove(db_file) # Remove existing DB to start fresh for testing
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
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('David', 42)")
        conn.commit()
        print(f"Database '{db_file}' created and populated with sample data.")
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
    finally:
        if conn:
            conn.close()

# --- Main execution block ---
if __name__ == "__main__":
    # Setup the database before using the context manager
    setup_database(DB_FILE)

    print("\n--- Using DatabaseConnection context manager ---")
    try:
        with DatabaseConnection(DB_FILE) as cursor:
            # Perform the query inside the 'with' block
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()

            print("\nQuery Results:")
            if results:
                for row in results:
                    print(row)
            else:
                print("No users found.")

        # Demonstrate error handling (optional: uncomment to test)
        # print("\n--- Testing error handling ---")
        # with DatabaseConnection(DB_FILE) as cursor:
        #     # This will cause an error because 'non_existent_table' does not exist
        #     cursor.execute("SELECT * FROM non_existent_table")
        #     print("This line will not be reached if an error occurs.")

    except sqlite3.Error as e:
        print(f"\nAn SQLite error occurred outside the context manager: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


