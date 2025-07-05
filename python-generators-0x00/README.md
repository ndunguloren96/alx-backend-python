# Python Generators - 0x00

This repository contains Python scripts demonstrating the use of generators for efficient data handling, particularly with large datasets and database interactions.

## Table of Contents

- [Project Setup](#project-setup)
- [Task 0: Getting Started with Python Generators](#task-0-getting-started-with-python-generators)
- [Task 1: Generator that Streams Rows from an SQL Database](#task-1-generator-that-streams-rows-from-an-sql-database)
- [Task 2: Batch Processing Large Data](#task-2-batch-processing-large-data)
- [Task 3: Lazy Loading Paginated Data](#task-3-lazy-loading-paginated-data)
- [Task 4: Memory-Efficient Aggregation with Generators](#task-4-memory-efficient-aggregation-with-generators)

## Project Setup

Before running the scripts, ensure you have MySQL installed and running.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/alx-backend-python.git
    cd alx-backend-python/python-generators-0x00
    ```

2.  **Install dependencies:**
    ```bash
    pip install mysql-connector-python python-dotenv uuid
    ```

3.  **Create a `.env` file:**
    In the `python-generators-0x00` directory, create a file named `.env` and populate it with your MySQL database credentials:

    ```
    DB_HOST=localhost
    DB_USER=your_mysql_user
    DB_PASSWORD=your_mysql_password
    DB_NAME=ALX_prodev
    ```
    **Replace `your_mysql_user` and `your_mysql_password` with your actual MySQL credentials.**

4.  **Create `user_data.csv`:**
    You'll need a CSV file named `user_data.csv` in the same directory. Here's an example of its structure:

    ```csv
    user_id,name,email,age
    00234e50-34eb-4ce2-94ec-26e3fa749796,Dan Altenwerth Jr.,Molly59@gmail.com,67
    # ... more data
    ```

## Task 0: Getting Started with Python Generators

**Objective:** Create a generator that streams rows from an SQL database one by one.

**Files:**
- `seed.py`: Contains functions to connect to MySQL, create the `ALX_prodev` database and `user_data` table, and insert data from `user_data.csv`.
- `0-main.py`: Demonstrates the functionality of `seed.py` by connecting, setting up the database/table, inserting data, and fetching initial rows.

**How to Run:**
```bash
chmod +x 0-main.py
./0-main.py
