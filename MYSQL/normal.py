import pymysql

# Connect to the MySQL server
def create_connection(host, username, password, database):
    conn = None
    try:
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print("Connected to the MySQL server")
    except pymysql.Error as e:
        print(e)
    return conn

# Execute a query that does not return data
def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except pymysql.Error as e:
        print(e)

# Execute a SELECT query and return the result
def execute_select_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except pymysql.Error as e:
        print(e)

# Close the database connection
def close_connection(conn):
    try:
        conn.close()
        print("Connection closed")
    except pymysql.Error as e:
        print(e)


# Example usage
host = "localhost"
username = "root"
password = ""
database = "pyd"

conn = create_connection(host, username, password, database)

# Execute a query that does not return data
create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        salary FLOAT NOT NULL
    )
"""
execute_query(conn, create_table_query)

# Execute a query that returns data
select_query = "SELECT * FROM employees"
execute_select_query(conn, select_query)

# Close the database connection
close_connection(conn)
