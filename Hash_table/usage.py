hash_table = HashTable()

hash_table.put("name", "John Doe")
hash_table.put("age", 30)
hash_table.put("city", "New York")

print(hash_table.get("name"))  # Output: John Doe
print(hash_table.get("age"))  # Output: 30

hash_table.remove("age")

print("age" in hash_table)  # Output: False

keys = hash_table.keys()
print(keys)  # Output: ['name', 'city']

values = hash_table.values()
print(values)  # Output: ['John Doe', 'New York']

hash_table.clear()
print(hash_table.size())  # Output: 0
