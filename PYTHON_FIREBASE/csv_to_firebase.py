import firebase_admin
from firebase_admin import credentials, firestore
import csv
import os
from datetime import datetime

def initialize_firestore_app(credentials_path):
    """Initialize Firestore app with provided credentials."""
    cred = credentials.Certificate(credentials_path)
    firebase_admin.initialize_app(cred)
    return firestore.client()

def create_firestore_collection(db, collection_name):
    """Create a new collection in Firestore."""
    try:
        db.collection(collection_name)
        print(f"Collection '{collection_name}' created successfully.")
    except Exception as e:
        print(f"Error creating collection: {e}")

def add_data_to_firestore_collection(db, collection_name, document_name, data):
    """Add data to a document in a Firestore collection."""
    try:
        doc_ref = db.collection(collection_name).document(document_name)
        doc_ref.set(data)
        print(f"Data added to {collection_name}/{document_name} in Firestore.")
    except Exception as e:
        print(f"Error adding data: {e}")

def import_csv_to_firestore(csv_file_path, collection_name, db):
    try:
        create_firestore_collection(db, collection_name)

        with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            header = next(reader)

            for row in reader:
                document_name = row[0]
                data = dict(zip(header[1:], row[1:]))
                add_data_to_firestore_collection(db, collection_name, document_name, data)

        return True
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
        return False
    except Exception as e:
        print(f"Error importing CSV to Firestore: {e}")
        return False

def list_files_in_folder_without_extensions(folder_path):
    try:
        files = os.listdir(folder_path)
        files_without_extensions = [file.split('.')[0] for file in files if '.' in file]
        return files_without_extensions
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except Exception as e:
        print(f"Error listing files: {e}")

def write_to_log(migrated_files):
    log_file = "migrated_files.log"
    with open(log_file, 'a') as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"\n{timestamp} - Migrated Files:\n")
        for file_name in migrated_files:
            log.write(f"{file_name}\n")
        log.write("="*50 + "\n")

def main():
    print("="*100)
    print(" CSV TO FIREBASE MIGRATE")
    print("="*100)

    json_key_path = input("Enter the path to your JSON key file: ")
    folder_path = input("Enter the path to your folder: ")

    try:
        db = initialize_firestore_app(json_key_path)

        files_without_extensions = list_files_in_folder_without_extensions(folder_path)

        if files_without_extensions:
            print(f"List of files without extensions in '{folder_path}':")
            for i, file_name in enumerate(files_without_extensions):
                print(f"{i+1}. {file_name}")

            choice = input("Enter the index of the file(s) to migrate (comma-separated, '0' for all): ")
            migrated_files = []

            if choice == '0':
                for i, file_name in enumerate(files_without_extensions):
                    csv_file_path = f"{folder_path}/{file_name}.csv"
                    collection_name = file_name
                    if import_csv_to_firestore(csv_file_path, collection_name, db):
                        migrated_files.append(file_name)
            else:
                selected_indices = [int(index.strip()) for index in choice.split(',') if index.strip().isdigit()]
                for index in selected_indices:
                    if 1 <= index <= len(files_without_extensions):
                        file_name = files_without_extensions[index-1]
                        csv_file_path = f"{folder_path}/{file_name}.csv"
                        collection_name = file_name
                        if import_csv_to_firestore(csv_file_path, collection_name, db):
                            migrated_files.append(file_name)
                        else:
                            print(f"Failed to import {file_name}.")
                    else:
                        print(f"Invalid index: {index}. Skipping.")

            if migrated_files:
                write_to_log(migrated_files)
                print(f"Migrated files logged in 'migrated_files.log'.")
            else:
                print("No files migrated.")

        else:
            print(f"No files found without extensions in '{folder_path}'.")
    except Exception as e:
        print(f"Error initializing Firestore: {e}")

if __name__ == "__main__":
    main()
