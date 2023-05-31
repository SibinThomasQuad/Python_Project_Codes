import json

def create_json(data):
    json_data = json.dumps(data)
    return json_data

def truncate_json(json_data):
    truncated_data = {}
    return json.dumps(truncated_data)

def update_json_with_key(json_data, key, value):
    data = json.loads(json_data)
    data[key] = value
    return json.dumps(data)

def delete_json_with_key(json_data, key):
    data = json.loads(json_data)
    if key in data:
        del data[key]
    return json.dumps(data)

def add_data_and_key_to_json(json_data, key, value):
    data = json.loads(json_data)
    if key not in data:
        data[key] = value
    return json.dumps(data)

# Example usage
data = {
    "name": "John",
    "age": 25
}

# Create JSON
json_data = create_json(data)
print(json_data)

# Truncate JSON
truncated_json = truncate_json(json_data)
print(truncated_json)

# Update JSON with Key
updated_json = update_json_with_key(json_data, "age", 30)
print(updated_json)

# Delete JSON with Key
deleted_json = delete_json_with_key(json_data, "age")
print(deleted_json)

# Add Data and New Key to JSON
new_json = add_data_and_key_to_json(json_data, "city", "New York")
print(new_json)
