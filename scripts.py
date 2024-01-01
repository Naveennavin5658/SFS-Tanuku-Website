from enum import Enum
import os,boto3
from pymongo import MongoClient
from enums import Env
def find_aggregate(request):
    total = request.get('Total')
    return {"Name":request.get("Name"),"Total":total,"Percentage":round(float(total)/6,2)}
def environ(key: Enum):
    return os.environ.get(key.value)
def get_db_client():
    connection_url = os.environ.get(Env.MONGO_URL.value)  
    mongo_client = MongoClient(connection_url)
    return mongo_client.get_database('SFS-Tanuku')

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
    
from pymongo import MongoClient


def convert_fields_to_int(doc):
    fields_to_convert = ['Roll No.']  
    for field in fields_to_convert:
        if field in doc and isinstance(doc[field], str):
            try:
                doc[field] = int(doc[field])
            except ValueError:
                pass  # If conversion fails, keep the original value
    return doc

def results_data_preprocessing():
    client = MongoClient('mongodb+srv://Naveen:Naveen@cluster0.h5lqydk.mongodb.net/')
    db = client['SFS-Tanuku']  
    collection = db['results'] 
    cursor = collection.find()
    for doc in cursor:
        new_doc = convert_fields_to_int(doc)
        collection.replace_one(
            { '_id': doc['_id'] },
            new_doc
        )

    print("Conversion completed for multiple fields.")




def get_download_url(bucket_name, key):
    #Used to fetch
    s3_client = boto3.client("s3")
    response = s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": bucket_name,
            "Key": key,
        },
        ExpiresIn=5184000,  # Link is valid for 60 days = 5184000 seconds
    )
    return response
