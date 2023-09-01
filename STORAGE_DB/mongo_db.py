import pymongo

# Connect to MongoDB (replace these with your MongoDB connection details)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Function to insert a document into the collection
def insert_document(data):
    result = collection.insert_one(data)
    print(f"Inserted document with ID: {result.inserted_id}")

# Function to find documents in the collection
def search_documents(query):
    documents = collection.find(query)
    for document in documents:
        print(document)

# Function to update documents in the collection
def update_document(query, new_data):
    result = collection.update_many(query, {"$set": new_data})
    print(f"Matched {result.matched_count} documents and modified {result.modified_count} documents")

# Function to delete documents from the collection
def delete_document(query):
    result = collection.delete_many(query)
    print(f"Deleted {result.deleted_count} documents")

if __name__ == "__main__":
    # Insert a document
    data_to_insert = {"name": "Alice", "age": 30}
    insert_document(data_to_insert)

    # Search for documents
    search_query = {"name": "Alice"}
    search_documents(search_query)

    # Update documents
    update_query = {"name": "Alice"}
    new_data = {"age": 31}
    update_document(update_query, new_data)

    # Search again to see the updated data
    search_documents(search_query)

    # Delete documents
    delete_query = {"name": "Alice"}
    delete_document(delete_query)
