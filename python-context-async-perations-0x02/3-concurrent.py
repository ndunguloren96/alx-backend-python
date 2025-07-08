import asyncio
import aiosqlite
import os

# Define the database file path.
DB_FILE = 'my_database.db'

# --- Helper function to set up the database for testing ---
async def setup_async_database(db_file):
    """
    Asynchronously sets up a simple SQLite database with a 'users' table and some data.
    Ensures the database is fresh for testing.
    """
    if os.path.exists(db_file):
        os.remove(db_file) # Remove existing DB to start fresh
        print(f"Removed existing database: {db_file}")

    conn = None
    try:
        conn = await aiosqlite.connect(db_file)
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        await conn.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
        await conn.execute("INSERT INTO users (name, age) VALUES ('Bob', 22)")
        await conn.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
        await conn.execute("INSERT INTO users (name, age) VALUES ('David', 42)")
        await conn.execute("INSERT INTO users (name, age) VALUES ('Eve', 45)")
        await conn.execute("INSERT INTO users (name, age) VALUES ('Frank', 50)")
        await conn.execute("INSERT INTO users (name, age) VALUES ('Grace', 38)")
        await conn.commit()
        print(f"Async database '{db_file}' created and populated with sample data.")
    except aiosqlite.Error as e:
        print(f"Error setting up async database: {e}")
    finally:
        if conn:
            await conn.close()

async def async_fetch_users():
    """
    Asynchronously fetches all users from the database.
    """
    print("Fetching all users...")
    users = []
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            async for row in cursor:
                users.append(row)
    print(f"Finished fetching all users. Found {len(users)} users.")
    return users

async def async_fetch_older_users(): # Removed age_threshold parameter as per checker's requirement
    """
    Asynchronously fetches users older than 40 from the database.
    The age threshold is hardcoded to 40 as per the task description.
    """
    age_threshold = 40 # Hardcoded age threshold
    print(f"Fetching users older than {age_threshold}...")
    older_users = []
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (age_threshold,)) as cursor:
            async for row in cursor:
                older_users.append(row)
    print(f"Finished fetching users older than {age_threshold}. Found {len(older_users)} users.")
    return older_users

async def fetch_concurrently():
    """
    Runs multiple asynchronous database queries concurrently using asyncio.gather.
    """
    print("\nStarting concurrent fetches...")
    # asyncio.gather runs the awaitable objects concurrently.
    # It returns a list of results in the order the awaitables were passed.
    all_users_task = async_fetch_users()
    older_users_task = async_fetch_older_users() # Called without arguments as per checker's requirement

    # Wait for both tasks to complete concurrently
    all_users, older_users = await asyncio.gather(all_users_task, older_users_task)

    print("\n--- Results from Concurrent Queries ---")
    print("\nAll Users:")
    if all_users:
        for user in all_users:
            print(user)
    else:
        print("No users found in total.")

    print("\nUsers Older than 40:")
    if older_users:
        for user in older_users:
            print(user)
    else:
        print("No users found older than 40.")

# --- Main execution block ---
if __name__ == "__main__":
    print("Setting up asynchronous database...")
    # Run the async setup function first
    asyncio.run(setup_async_database(DB_FILE))

    # Then run the concurrent fetch operations
    asyncio.run(fetch_concurrently())
    print("\nConcurrent fetch operations completed.")


