import shelve

class PersistentInMemoryDatabase:
    def __init__(self, storage_file):
        self.storage = shelve.open(storage_file)

    def insert(self, key, value):
        self.storage[key] = value
        self.storage.sync()  # Ensure data is written immediately
        print(f"Inserted: {key} -> {value}")

    def delete(self, key):
        if key in self.storage:
            del self.storage[key]
            self.storage.sync()
            print(f"Deleted: {key}")
        else:
            print(f"Key '{key}' not found, cannot delete")

    def update(self, key, value):
        if key in self.storage:
            self.storage[key] = value
            self.storage.sync()
            print(f"Updated: {key} -> {value}")
        else:
            print(f"Key '{key}' not found, cannot update")

    def search(self, key):
        if key in self.storage:
            return self.storage[key]
        else:
            return None

    def close(self):
        self.storage.close()

if __name__ == "__main__":
    db = PersistentInMemoryDatabase("mydata.db")

    # Insert data
    
    db.insert("name", "Alice")
    db.insert("age", 30)

    # Search data
    name = db.search("name")
    print("Name:", name)
    age = db.search("age")
    print("Age:", age)

    # Update data
    db.update("age", 31)
    updated_age = db.search("age")
    print("Updated Age:", updated_age)

    # Delete data
    db.delete("name")
    deleted_name = db.search("name")
    print("Deleted Name:", deleted_name)

    # Close the database
    db.close()
