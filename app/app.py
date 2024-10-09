from flask import Flask, request, jsonify
from opensearchpy import OpenSearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize OpenSearch client
client = OpenSearch(
    [{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    timeout=30,
    max_retries=10,
    retry_on_timeout=True,
)

index_name = 'epirecipes_v2'

@app.route('/search', methods=['GET'])
def search_recipes():
    query = request.args.get('q', '')  # Get the search query from request parameters
    calories_gt = request.args.get("calories_gt",None)
    protein_gt = request.args.get("protein_gt",None)
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))

    # Calculate from for pagination
    from_param = (page - 1) * size

    # Construct the OpenSearch query
    opensearch_query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": ["title","description"]  # Adjust fields as needed
                        }
                    }
                ],
                "filter": []
            }
        },
        
        "from": from_param,
        "size": size
    }

    # Add filter for calories range if provided
    if calories_gt:
        calorie_filter = {
            "range": {
                "calories": {
                    "gt":calories_gt
                }
            }
        }
        opensearch_query['query']['bool']['filter'].append(calorie_filter)

    if protein_gt:
        protein_filter = {
            "range": {
                "protein": {
                    "gt":protein_gt
                }
            }
        }
        opensearch_query['query']['bool']['filter'].append(protein_filter)
        
    if not calories_gt and not protein_gt:
        opensearch_query['sort'] = [{"title.keyword":{"order":"asc"}}]
    elif calories_gt:
        opensearch_query['sort'] = [{"calories":{"order":"desc"}}]
    elif protein_gt:
        opensearch_query['sort'] = [{"protein":{"order":"desc"}}]

    # Perform the search
    response = client.search(index=index_name, body=opensearch_query)
    recipes = response['hits']['hits']
    total = response['hits']['total']['value']

    # Extract relevant data
    results = [{"title": recipe['_source']['title'], "rating": recipe['_source']['rating'], "calories": recipe['_source']['calories'], "protein":recipe['_source']["protein"]} for recipe in recipes]

    return jsonify({
        "total": total,
        "page": page,
        "size": size,
        "recipes": results
    })

if __name__ == '__main__':
    app.run(debug=True)
