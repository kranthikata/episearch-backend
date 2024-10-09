# Recipe Search Application

## Objective

Develop a full-stack web application that indexes the "EpiRecipes" dataset into OpenSearch,
provides a user-friendly interface for searching and filtering recipes, and demonstrates
proficiency in React for frontend development, Python (Flask/Django/FastAPI/any other) for
backend development, and version control using GitHub.

## Project Overview

You are tasked with creating a comprehensive recipe search platform that allows users to
efficiently search and filter through a vast collection of recipes. The application should mimic
the user experience of leading e-commerce platforms like Flipkart or Amazon, ensuring intuitive
navigation and responsive design.

## Prerequisites

- Ensure you have Docker installed on your machine.
- Make sure you have the EpiRecipes dataset in CSV format.

## Step 1: Set Up OpenSearch with Docker

1. Pull the OpenSearch Docker image:
   ```bash
   docker pull opensearchproject/opensearch:1
   ```
2. Run the below command:
   ```bash
   docker run -d -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" opensearchproject/opensearch:latest
   ```
3. Verify that OpenSearch is running by opening your browser and navigating to::

   ```bash
   http://localhost:9200
   ```

## Step 2: Create Index in OpenSearch and Load it

1. Run the `create_index.py`
2. Run the `index_recipes.py`

## Step 3: Verify the Indexing is success or not

1. Run `get_data.py`

## Step 4: Start the server

1. Run the command
   `python -m flask --app app.py run`

## Step 5: Start Frontend server

1. Run this command `npm start`

## Technologies Used

- Reat.js
- Python
- CSS
- Docker
- OpenSearch
- Github
