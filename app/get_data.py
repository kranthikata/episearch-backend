from opensearchpy import OpenSearch

client = OpenSearch(
    [{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    timeout=30,
    max_retries=10,
    retry_on_timeout=True,
)

index_name = 'epirecipes'

response = client.search(
    index=index_name,
    body={
        "query": {
            "match_all": {}
        },
        "size": 10  # Adjust the size as needed
    }
)

for hit in response['hits']['hits']:
    print(hit['_source'])
