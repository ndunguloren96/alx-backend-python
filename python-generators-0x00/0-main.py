#!/usr/bin/python3

import seed

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    # Don't close the connection here, we'll use it to connect to the new database

    connection = seed.connect_to_prodev()

    if connection:
        try:
            seed.create_table(connection)
            seed.insert_data(connection, 'user_data.csv')
            cursor = connection.cursor()
            cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{seed.DB_NAME}'")
            result = cursor.fetchone()
            if result:
                print(f"Database {seed.DB_NAME} is present ")
            cursor.execute(f"SELECT * FROM user_data LIMIT 5;")
            rows = cursor.fetchall()
            print(rows)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close() # Close connection after all operations
    else:
        print("Failed to connect to ALX_prodev database.")
else:
    print("Failed to establish initial database connection.")
