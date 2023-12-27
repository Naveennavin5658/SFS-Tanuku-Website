from scripts import get_db_client


db_client = get_db_client()
def get_reviews():
    """
    Fetches testimonials from the 'testimonials' collection.

    Returns:
    dict: A dictionary containing a response code and data.
        - 'code' (int): HTTP status code indicating the success of the operation (200 for success).
        - 'data' (list): A list of dictionaries containing testimonials fetched from the database.
    """
    testimonials_collection = db_client.get_collection('testimonials')
    db_response = list(testimonials_collection.find({}, {"_id": False, "email": False}))
    return {"code": 200, "data": db_response}

    