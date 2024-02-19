import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase_app(credentials_path):
    """Initialize Firebase app with provided credentials."""
    cred = credentials.Certificate(credentials_path)
    firebase_admin.initialize_app(cred)
    return firestore.client()

def create_collection(db, collection_name):
    """Create a new collection in Firestore."""
    try:
        db.collection(collection_name)
        print(f"Collection '{collection_name}' created successfully.")
    except Exception as e:
        print(f"Error creating collection: {e}")

def add_data_to_collection(db, collection_name, document_name, data):
    """Add data to a document in a Firestore collection."""
    try:
        doc_ref = db.collection(collection_name).document(document_name)
        doc_ref.set(data)
        print(f"Data added to {collection_name}/{document_name} in Firestore.")
    except Exception as e:
        print(f"Error adding data: {e}")

def delete_record(db, collection_name, document_name):
    """Delete a record from a Firestore collection."""
    try:
        db.collection(collection_name).document(document_name).delete()
        print(f"Record deleted: {collection_name}/{document_name}")
    except Exception as e:
        print(f"Error deleting record: {e}")

def update_record(db, collection_name, document_name, updated_data):
    """Update a record in a Firestore collection."""
    try:
        doc_ref = db.collection(collection_name).document(document_name)
        doc_ref.update(updated_data)
        print(f"Record updated: {collection_name}/{document_name}")
    except Exception as e:
        print(f"Error updating record: {e}")

def search_record(db, collection_name, field, value):
    """Search for records in a Firestore collection based on a field-value pair."""
    try:
        query = db.collection(collection_name).where(field, '==', value)
        results = query.stream()

        if results:
            print(f"Records in {collection_name} where {field} is {value}:")
            for doc in results:
                print(f"- Document {doc.id}: {doc.to_dict()}")
        else:
            print(f"No records found in {collection_name} where {field} is {value}.")
    except Exception as e:
        print(f"Error searching records: {e}")

def list_all_records(db, collection_name):
    """List all records from a Firestore collection."""
    try:
        collection_ref = db.collection(collection_name)
        documents = collection_ref.stream()

        if documents:
            print(f"Listing all records in '{collection_name}':")
            for doc in documents:
                print(f"- Document {doc.id}: {doc.to_dict()}")
        else:
            print(f"No documents found in '{collection_name}'.")
    except Exception as e:
        print(f"Error listing records: {e}")

def show_last_n_records(db, collection_name, n=10):
    """Show the last N records from a Firestore collection."""
    try:
        collection_ref = db.collection(collection_name)
        query = collection_ref.order_by(firestore.FieldPath.documentId(), direction=firestore.Query.DESCENDING).limit(n)
        results = query.stream()

        if results:
            print(f"Showing last {n} records in '{collection_name}':")
            for doc in results:
                print(f"- Document {doc.id}: {doc.to_dict()}")
        else:
            print(f"No documents found in '{collection_name}'.")
    except Exception as e:
        print(f"Error showing last N records: {e}")

def show_records_between(db, collection_name, start_value, end_value):
    """Show records between two values in a Firestore collection."""
    try:
        collection_ref = db.collection(collection_name)
        query = collection_ref.where('field_to_compare', '>=', start_value).where('field_to_compare', '<=', end_value)
        results = query.stream()

        if results:
            print(f"Showing records between {start_value} and {end_value} in '{collection_name}':")
            for doc in results:
                print(f"- Document {doc.id}: {doc.to_dict()}")
        else:
            print(f"No documents found between {start_value} and {end_value} in '{collection_name}'.")
    except Exception as e:
        print(f"Error showing records between values: {e}")

if __name__ == "__main__":
    # Replace with your actual credentials file path
    credentials_path = "path/to/your/credentials.json"

    # Initialize Firebase
    firestore_db = initialize_firebase_app(credentials_path)

    # Replace with your desired collection and document names
    new_collection_name = "new_collection"
    new_document_name = "new_document"

    # Replace with the data you want to add or update
    data_to_add = {
        "field1": "value1",
        "field2": "value2",
        "field3": 42
    }

    # Create a new collection
    create_collection(firestore_db, new_collection_name)

    # Add data to the new collection
    add_data_to_collection(firestore_db, new_collection_name, new_document_name, data_to_add)

    # Update data in the new collection
    update_data = {"field2": "new_value2"}
    update_record(firestore_db, new_collection_name, new_document_name, update_data)

    # Search for records in the new collection
    search_record(firestore_db, new_collection_name, "field1", "value1")

    # List all records in the new collection
    list_all_records(firestore_db, new_collection_name)

    # Show the last 5 records in the new collection
    show_last_n_records(firestore_db, new_collection_name, n=5)

    # Show records between two values in the new collection
    show_records_between(firestore_db, new_collection_name, start_value="value1", end_value="value2")

    # Delete data from the new collection
    delete_record(firestore_db, new_collection_name, new_document_name)
