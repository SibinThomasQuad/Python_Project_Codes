import requests
import json

# Elasticsearch server details
host = 'localhost'
port = 9200
base_url = f'http://{host}:{port}'

# Index and document details
index_name = '3a3'
document = {
    'title': 'username',
    'content': 'This is a sample document for Elasticsearch.'
}

# Index the document
index_url = f'{base_url}/{index_name}/_doc/1'
headers = {'Content-Type': 'application/json'}
response = requests.put(index_url, data=json.dumps(document), headers=headers)

if response.status_code == 201:
    print("Document indexed successfully.")
else:
    print("Failed to index the document.")

# Search for the document
search_query = {
    'query': {
        'match': {
            'content': 'Elasticsearch'
        }
    }
}

search_url = f'{base_url}/{index_name}/_search'
response = requests.get(search_url, data=json.dumps(search_query), headers=headers)
print(response.text)

if response.status_code == 200:
    search_results = response.json()
    print("Search Results:")
    for hit in search_results['hits']['hits']:
        print(f"Score: {hit['_score']}, Document: {hit['_source']}")
else:
    print("Search request succeeded, but no documents matched the query.")
