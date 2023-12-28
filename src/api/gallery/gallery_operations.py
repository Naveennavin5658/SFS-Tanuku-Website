import boto3
s3 = boto3.client('s3')
# Function to fetch images for a specific event in a year
def fetch_images_for_event(year, event):
    """
    Fetches image URLs for a specific event and year from an S3 bucket.

    Args:
    - year (int): The year of the event.
    - event (str): The name or identifier of the event.

    Returns:
    - list: A list of image URLs associated with the specified event and year.
            Returns an empty list if no images are found or if an error occurs.
    """
    bucket_name = 'bucket-sfs-gallery'  
    prefix = f'{year}-pics/{event}-pics/'  # Example: '2022-pics/Childrens-day-pics/'
    try:
        # List objects in the S3 bucket with the specified prefix
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        # Get base S3 URL
        base_s3_url = f"https://{bucket_name}.s3.amazonaws.com/"

        # Construct image URLs
        image_urls = [base_s3_url + obj['Key'] for obj in response.get('Contents', [])]
        
        return image_urls[1:] if len(image_urls)>1 else []
    except Exception as e:
        print(f"Error fetching images: {e}")
        return []

    
    
def get_events_for_year(year):
    """
    Retrieves image data for various events occurring in a given year.

    Args:
    - year (int): The year for which events' image data is requested.

    Returns:
    - dict: A dictionary containing image data for different events in the specified year.
            The dictionary structure is as follows:
            {
                "code": 200,  # HTTP status code indicating success
                "data": {
                    "<event_name>": [<image_url1>, <image_url2>, ...],  # List of image URLs for each event
                    ...
                }
            }
            Returns an empty dictionary if the year is invalid or if there's an error fetching the data.
    """
    # Simulated data structure of events
    available_events = ["INDEPENDENCE_DAY", "TEACHERS_DAY", "CHILDRENS_DAY", "X_MAS_DAY", "PONGAL_DAY", "FETE_DAY","SCIENCE_EXPO","SPORTS_DAY"]
    images_data = {}
    for event in available_events:
        images_data[event] = fetch_images_for_event(year, event)[:5]  # Get 5 images for each event
    return {"code": 200, "data": images_data}
