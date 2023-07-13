import json

def json_string_to_insert_query(table_name, json_string):
    json_data = json.loads(json_string)
    columns = ', '.join(json_data.keys())
    values = ', '.join("'" + str(value) + "'" for value in json_data.values())

    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    return insert_query

# Example usage
table_name = 'my_table'
json_string = '''
{
  "column1": "value1",
  "column2": "value2",
  "column3": 123,
  "column4": "value4"
}
'''

insert_query = json_string_to_insert_query(table_name, json_string)
print(insert_query)
