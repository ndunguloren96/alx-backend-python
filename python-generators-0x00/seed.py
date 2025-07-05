#!/usr/bin/python3

import psycopg2
from psycopg2.extras import RealDictCursor # To fetch rows as dictionaries
import csv
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT', 5432) # Default to 5432 if not set

def connect_db():
    """
    Connects to the PostgreSQL database server (to the default 'postgres' database initially).
    This allows creating other databases.
    """
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            database='postgres' # <-- CRUCIAL: Connect to the default 'postgres' database first
        )
        # Set autocommit to true for database creation, as CREATE DATABASE cannot be in a transaction block
        connection.autocommit = True
        print("Successfully connected to PostgreSQL server.")
        return connection
    except psycopg2.Error as err:
        print(f"Error connecting to PostgreSQL: {err}")
        return None

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    try:
        # Check if database exists before creating
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        exists = cursor.fetchone()
        if not exists:
            # Ensure the database is created with the correct owner
            cursor.execute(f'CREATE DATABASE "{DB_NAME}" WITH OWNER {DB_USER}')
            print(f"Database {DB_NAME} created.")
        else:
            print(f"Database {DB_NAME} already exists.")
    except psycopg2.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database in PostgreSQL."""
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME, # Now connect to the specific ALX_prodev database
            port=DB_PORT
        )
        print(f"Successfully connected to database {DB_NAME}.")
        return connection
    except psycopg2.Error as err:
        print(f"Error connecting to {DB_NAME}: {err}")
        return None

def create_table(connection):
    """Creates a table user_data if it does not exist with the required fields."""
    cursor = connection.cursor()
    table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age NUMERIC(5, 2) NOT NULL
    )
    """
    try:
        cursor.execute(table_query)
        connection.commit()
        print("Table user_data created successfully or already exists.")
    except psycopg2.Error as err:
        print(f"Failed creating table: {err}")
        connection.rollback() # Rollback on error
    finally:
        cursor.close()

def insert_data(connection, csv_file):
    """Inserts data into the database from a CSV file if it does not exist."""
    cursor = connection.cursor()
    
    # Check if the table is empty
    cursor.execute("SELECT COUNT(*) FROM user_data")
    if cursor.fetchone()[0] > 0:
        print("Data already exists in user_data table. Skipping insertion.")
        cursor.close()
        return

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = row.get('user_id')
                try:
                    # Validate if it's a UUID, otherwise generate a new one
                    uuid.UUID(user_id)
                except (ValueError, TypeError):
                    user_id = str(uuid.uuid4())

                # Use ON CONFLICT DO NOTHING for PostgreSQL to handle duplicates
                sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING"
                val = (user_id, row['name'], row['email'], float(row['age']))
                try:
                    cursor.execute(sql, val)
                except psycopg2.Error as err:
                    # PostgreSQL unique violation error code is 23505
                    if err.pgcode == '23505':
                        print(f"Skipping duplicate entry: {user_id}")
                    else:
                        raise err
            connection.commit()
            print("Data inserted successfully.")
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except psycopg2.Error as err:
        print(f"Failed inserting data: {err}")
        connection.rollback() # Rollback on error
    finally:
        cursor.close()

if __name__ == '__main__':
    # This block is for testing individual functions or for setting up
    pass


