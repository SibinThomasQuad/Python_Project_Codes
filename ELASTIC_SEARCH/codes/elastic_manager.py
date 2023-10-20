import requests
import json

class ElasticsearchManager:
    def __init__(self, host="localhost", port=9200):
        self.base_url = f"http://{host}:{port}"

    def create_index(self, index_name, mappings):
        index_url = f"{self.base_url}/{index_name}"
        headers = {"Content-Type": "application/json"}

        data = {
            "mappings": mappings
        }

        try:
            response = requests.put(index_url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                print(f"Index '{index_name}' created successfully.")
            else:
                print(f"Failed to create index: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    def index_document(self, index_name, document, doc_id=None):
        index_url = f"{self.base_url}/{index_name}/_doc"
        headers = {"Content-Type": "application/json"}

        if doc_id:
            index_url = f"{index_url}/{doc_id}"

        try:
            response = requests.post(index_url, data=json.dumps(document), headers=headers)
            if response.status_code == 201:
                print(f"Document indexed with ID: {json.loads(response.text)['_id']}")
            else:
                print(f"Failed to index document: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    def get_document(self, index_name, doc_id):
        get_url = f"{self.base_url}/{index_name}/_doc/{doc_id}"

        try:
            response = requests.get(get_url)
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print(f"Document with ID {doc_id} not found.")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        return None

    def delete_index(self, index_name):
        delete_url = f"{self.base_url}/{index_name}"

        try:
            response = requests.delete(delete_url)
            if response.status_code == 200:
                print(f"Index '{index_name}' deleted successfully.")
            else:
                print(f"Failed to delete index: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

# Example usage:
if __name__ == "__main__":
    es_manager = ElasticsearchManager()

    index_name = "sample_index"
    mappings = {
        "properties": {
            "title": {"type": "text"},
            "content": {"type": "text"},
        }
    }

    es_manager.create_index(index_name, mappings)

    document = {
        "title": "Sample Document",
        "content": "This is a sample document stored in Elasticsearch."
    }

    es_manager.index_document(index_name, document, doc_id=1)

    result = es_manager.get_document(index_name, doc_id=1)
    if result:
        print("Retrieved document:", result)

    es_manager.delete_index(index_name)
