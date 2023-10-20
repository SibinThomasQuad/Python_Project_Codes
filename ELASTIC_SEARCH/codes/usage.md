To use the `ElasticsearchManager` class by including it in another file, follow these steps:

1. Save the `ElasticsearchManager` class in a separate Python file, for example, `elasticsearch_manager.py`.

```python
# elasticsearch_manager.py

import requests
import json

class ElasticsearchManager:
    # ... (rest of the class code)
```

2. In your main Python file, import the `ElasticsearchManager` class and use it as needed.

```python
# main.py

from elasticsearch_manager import ElasticsearchManager

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
```

3. Make sure that both files (`elasticsearch_manager.py` and `main.py`) are in the same directory or in a directory where Python can locate them.

4. Run the `main.py` file to execute the Elasticsearch operations.

You can use the `ElasticsearchManager` class in other Python files as well by importing it as shown in step 2 and using its methods for Elasticsearch operations.
