import pandas as pd
from opensearchpy import OpenSearch, RequestsHttpConnection
from opensearchpy.helpers import bulk
import json
import os


client = OpenSearch(
    [{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    timeout=30,
    max_retries=10,
    retry_on_timeout=True,
    connection_class=RequestsHttpConnection,
)

data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'epi_r.csv')
df = pd.read_csv(data_path)

df.fillna(0, inplace=True)

index_name = 'epirecipes'


if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name)


def generate_docs():
    for _, row in df.iterrows():
        yield {
            '_index': index_name,
            '_id': row['title'], 
            '_source': {
                'title': row['title'],
                'rating': row['rating'],
                'calories': row['calories'],
                'protein': row['protein'],
                'fat': row['fat'],
                'sodium': row['sodium'],
                '#cakeweek': row['#cakeweek'],
                '#wasteless': row['#wasteless'],
                '22-minute meals': row['22-minute meals'],
                '3-ingredient recipes': row['3-ingredient recipes'],
                '30 days of groceries': row['30 days of groceries'],
                'advance prep required': row['advance prep required'],
            },
        }


bulk(client, generate_docs())
print(f"Indexed {len(df)} recipes into '{index_name}' index.")
