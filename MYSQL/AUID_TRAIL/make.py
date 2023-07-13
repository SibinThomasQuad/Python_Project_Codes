import mysql.connector

def create_audit_trail(connection, table_name):
    # Create the audit trail table
    cursor = connection.cursor()
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS audit_trail (
            id INT AUTO_INCREMENT PRIMARY KEY,
            table_name VARCHAR(100),
            action VARCHAR(10),
            old_data JSON,
            new_data JSON,
            change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Get column names of the table
    get_columns_query = f"DESCRIBE {table_name}"
    cursor.execute(get_columns_query)
    columns = [column[0] for column in cursor.fetchall()]

    # Create the trigger to capture INSERT
    create_insert_trigger_query = f"""
        CREATE TRIGGER trigger_audit_insert_{table_name}
        AFTER INSERT ON {table_name}
        FOR EACH ROW
        BEGIN
            INSERT INTO audit_trail (table_name, action, new_data)
            VALUES ('{table_name}', 'INSERT', JSON_OBJECT(
                {", ".join([f"'{column}', NEW.{column}" for column in columns])}
            ));
        END
    """
    cursor.execute(create_insert_trigger_query)
    connection.commit()

    # Create the trigger to capture UPDATE
    create_update_trigger_query = f"""
        CREATE TRIGGER trigger_audit_update_{table_name}
        AFTER UPDATE ON {table_name}
        FOR EACH ROW
        BEGIN
            INSERT INTO audit_trail (table_name, action, old_data, new_data)
            VALUES ('{table_name}', 'UPDATE', JSON_OBJECT(
                {", ".join([f"'{column}', OLD.{column}" for column in columns])},
                'change_date', NOW()
            ), JSON_OBJECT(
                {", ".join([f"'{column}', NEW.{column}" for column in columns])}
            ));
        END
    """
    cursor.execute(create_update_trigger_query)
    connection.commit()

    # Create the trigger to capture DELETE
    create_delete_trigger_query = f"""
        CREATE TRIGGER trigger_audit_delete_{table_name}
        AFTER DELETE ON {table_name}
        FOR EACH ROW
        BEGIN
            INSERT INTO audit_trail (table_name, action, old_data)
            VALUES ('{table_name}', 'DELETE', JSON_OBJECT(
                {", ".join([f"'{column}', OLD.{column}" for column in columns])}
            ));
        END
    """
    cursor.execute(create_delete_trigger_query)
    connection.commit()

    cursor.close()

# Example usage
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ms'
)
table_name = 'users'

create_audit_trail(connection, table_name)
