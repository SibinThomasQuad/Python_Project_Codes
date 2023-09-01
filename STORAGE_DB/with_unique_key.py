import os
import json
import hashlib

class FileStorageDB:
    def __init__(self, storage_dir):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def generate_key(self, data):
        # Create a unique MD5 hash as the key
        data_json = json.dumps(data, sort_keys=True)
        md5_hash = hashlib.md5(data_json.encode()).hexdigest()
        return md5_hash

    def insert(self, data):
        key = self.generate_key(data)
        filename = os.path.join(self.storage_dir, key + '.json')
        with open(filename, 'w') as file:
            json.dump(data, file)

    def update(self, key, data):
        filename = os.path.join(self.storage_dir, key + '.json')
        if os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump(data, file)
        else:
            raise KeyError(f"Key '{key}' not found")

    def get(self, key):
        filename = os.path.join(self.storage_dir, key + '.json')
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        filename = os.path.join(self.storage_dir, key + '.json')
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise KeyError(f"Key '{key}' not found")

if __name__ == "__main__":
    db = FileStorageDB("data_storage")

    # Insert data
    user1_data = {"name": "Alice", "age": 30}
    db.insert(user1_data)
    
    user2_data = {"name": "Bob", "age": 25}
    db.insert(user2_data)

    # Get data
    user1_key = db.generate_key(user1_data)
    print("User 1:", db.get(user1_key))
    
    user2_key = db.generate_key(user2_data)
    print("User 2:", db.get(user2_key))

    # Update data
    db.update(user1_key, {"name": "Alice Smith", "age": 31})
    print("Updated User 1:", db.get(user1_key))

    # Delete data
    db.delete(user2_key)
    try:
        print("User 2 (after deletion):", db.get(user2_key))
    except KeyError as e:
        print(e)
