from enum import Enum
import os
from pymongo import MongoClient
from enums import Env
def find_aggregate(request):
    total = request.get('Total')
    return {"Name":request.get("Name"),"Total":total,"Percentage":round(float(total)/6,2)}
def environ(key: Enum):
    return os.environ.get(key.value)
def get_db_client():
    connection_url = environ(Env.MONGO_URL)
    mongo_client = MongoClient(connection_url)
    return mongo_client.get_database(environ(Env.DATABASE))

import pandas as pd
from pymongo import MongoClient
def ingest_excel_data_to_db():
    

    # Connect to MongoDB
    client = MongoClient('mongodb+srv://Naveen:Naveen@cluster0.h5lqydk.mongodb.net/')
    db = client['SFS-Tanuku']  
    collection = db['testimonials']  # Collection where data will be inserted

    # Read the CSV file
    csv_file = '/Users/Naveen/Downloads/Untitled form (Responses) - Sheet1.csv'  # Replace 'path_to_your_csv_file.csv' with your CSV file path
    data = pd.read_csv(csv_file)

    # Convert CSV data to a list of dictionaries (assuming CSV columns are 'full_name', 'year_of_passing', 'testimonial')
    data_dict = data.to_dict(orient='records')

    # Insert data into MongoDB collection
    collection.insert_many(data_dict)

