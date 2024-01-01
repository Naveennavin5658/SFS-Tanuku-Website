from flask import Request
from scripts import get_db_client
db_client = get_db_client()
def add_user_as_alumni(request: Request):
    try:
        data = request.get_json(silent=True) or {}
        email, contact, yop = data.get('email'), data.get('contact'), data.get('passoutYear')
        if not data:
            return {"data": "Input request is empty", "code": 400}

        alumni_collection = db_client.get_collection("alumni")
        #Check if the user already exists:
        db_response = list(alumni_collection.find({"email":email,"contact":contact,"passoutYear":yop}))
        if(db_response!=[]):
            return {"code":200,"data":"User is already registered!"}
        else:
            alumni_collection.insert_one(data)
            return {"code": 201, "data": "Successfully registered as alumni"}

    except Exception as e:
        return {"error": str(e), "code": 500}





import boto3


def list_buckets():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if response:
            print("Buckets exist!")
            for bucket in response.get("Buckets"):
                print(bucket.get('Name'))
    except Exception as e:
        print(f"Printing buckets operation failed due to this error {e}")
        return False
    return True


import boto3

import boto3
import requests
from botocore.exceptions import NoCredentialsError

def get_default_region():
    try:
        session = boto3.Session()
        default_region = session.region_name
        if not default_region:
            # Fetch the region from the metadata service if not set in the config
            default_region = requests.get('http://169.254.169.254/latest/meta-data/placement/availability-zone').text[:-1]
        return default_region
    except NoCredentialsError as e:
        print(f"No AWS credentials found: {e}")
        return None

def create_bucket(bucket_name):
    try:
        default_region = get_default_region()
        if not default_region:
            print("Unable to determine the default region.")
            return False

        s3_client = boto3.client('s3', region_name=default_region)
        s3_client.create_bucket(Bucket=bucket_name)
        return True
    except Exception as e:
        print(f"Bucket creation failed due to this error: {e}")
        return False


def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        object_name = bucket
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except Exception as e:
        return False
    return True

def delete_file(bucket, key_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_object(Bucket=bucket,Key=key_name)
    except Exception as e:
        return False
    return True