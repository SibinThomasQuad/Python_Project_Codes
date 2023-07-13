import csv

def csv_to_insert_queries(file_path, table_name):
    insert_queries = []
    create_table_query = None

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fields = csv_reader.fieldnames
        columns = ', '.join(fields)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

        for row in csv_reader:
            values = tuple(row.values())
            placeholders = ', '.join(['%s'] * len(row))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            insert_queries.append((query, values))
    
    return create_table_query, insert_queries

# Example usage
file_path = 'data.csv'
table_name = 'users'

create_table_query, insert_queries = csv_to_insert_queries(file_path, table_name)

print("CREATE TABLE query:")
print(create_table_query)
print()

print("INSERT queries:")
for query, values in insert_queries:
    print(query)
    print(values)
    print()
