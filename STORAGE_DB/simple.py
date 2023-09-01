import os
import json

class FileStorageDB:
    def __init__(self, storage_dir):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def insert(self, key, data):
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
    db.insert("user1", {"name": "Alice", "age": 30})
    db.insert("user2", {"name": "Bob", "age": 25})

    # Get data
    print("User 1:", db.get("user1"))
    print("User 2:", db.get("user2"))

    # Update data
    db.update("user1", {"name": "Alice Smith", "age": 31})
    print("Updated User 1:", db.get("user1"))

    # Delete data
    db.delete("user2")
    try:
        print("User 2 (after deletion):", db.get("user2"))
    except KeyError as e:
        print(e)
