import sqlite3

# Define the path to the SQL file and the desired SQLite database file
sql_file = 'input.sql'
sqlite_db = 'output.db'

# Connect to the SQLite database
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Read and execute the SQL script from the SQL file
with open(sql_file, 'r') as sql_script:
    sql_statements = sql_script.read()
    cursor.executescript(sql_statements)

# Commit and close the database connection
conn.commit()
conn.close()

print(f"Converted {sql_file} to {sqlite_db}")
