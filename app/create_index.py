from opensearchpy import OpenSearch

# Initialize OpenSearch client
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

index_name = 'epirecipes'

# Step 1: Create the new index with the desired mapping
try:
    client.indices.create(
        index=index_name,
        body={
            "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        }
    },
            "mappings": {
                "properties": {
                    "title": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "description": {
                        "type": "text"
                    },
                    "calories": {
                        "type": "float"
                    },
                    "protein": {
                        "type": "float"
                    },
                    "rating": {
                        "type": "integer"
                    }
                }
            }
        }
    )
    print(f"Created new index: {index_name}")
except Exception as e:
    print(f"Error creating index: {str(e)}")


# Step 2: Verify the data in the new index
try:
    index_count = client.count(index=index_name)
    print(f"Document count in new index: {index_count['count']}")
except Exception as e:
    print(f"Error counting documents in new index: {str(e)}")
