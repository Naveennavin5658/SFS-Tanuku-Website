from scripts import find_aggregate, get_db_client
db_client = get_db_client()

def get_results(year: int):
    """
    Retrieves student results for a given year from the database and prepares an API response.
    Args:
    - year (int): The year for which student results are to be retrieved.
    Returns:
    - dict: A dictionary containing the API response.
      - 'code' (int): The status code of the response.
      - 'data' (list or str): If data is available, a list of student summaries. Otherwise, a message indicating no data is available.
    """

    results_collection = db_client.get_collection("results")
    db_result = list(results_collection.find({"Year": str(year)}, {"_id": False}))
    api_response = []
    for resp in db_result:
        student_summary = find_aggregate(resp)
        api_response.append(student_summary)
    if db_result == []:
        return {"code": 200, "data": "No Data Available"}
    return {"code": 200, "data": api_response}



def get_stats_in_year(year:int):
    """
    Retrieves statistics for a given year from the database.
    Args:
    - year (int): The year for which statistics are to be retrieved.
    Returns:
    - dict: A dictionary containing statistics:
        - "studentCount": Total number of students in the given year.
        - "gt570": Number of students with a total score greater than or equal to 570.
        - "gt550": Number of students with a total score greater than or equal to 550.
        - "gt500": Number of students with a total score greater than or equal to 500.
        - "passPercentage": Overall pass percentage (temporarily hardcoded to 100%).
    """
    SCORE_GT_570 = 570
    SCORE_GT_550 = 550
    SCORE_GT_500 = 500

    results_collection = db_client.get_collection("results")
    db_result = list(results_collection.find({"Year": str(year)}, {"_id": False}))
    total_student_count = len(db_result)
    count_greater_than_570 = sum(1 for result in db_result if int(result.get('Total')) >= SCORE_GT_570)
    count_greater_than_550 = sum(1 for result in db_result if int(result.get('Total')) >= SCORE_GT_550)
    count_greater_than_500 = sum(1 for result in db_result if int(result.get('Total')) >= SCORE_GT_500)

    pass_percentage = 100  # Temporarily hardcoding to 100%. We need to have failed candidates data in db.

    api_response = {
        "studentCount": total_student_count,
        "gt570": count_greater_than_570,
        "gt550": count_greater_than_550,
        "gt500": count_greater_than_500,
        "passPercentage": pass_percentage
    }  
    return {"code": 200, "data": api_response}




def get_toppers_of_year(year:int):
    """
    Retrieves top-performing students of a specific year from the database.
    Args:
    - year (int): The year for which to retrieve top-performing students.
    Returns:
    - dict: A dictionary containing information about the top 3 performing students:
        - "code": HTTP status code (200 for successful retrieval).
        - "data": A list containing information about each top-performing student.
            Each item in the list is a dictionary with student information:
                - Example format of student_summary:
                    {
                        'student_name': 'John Doe',
                        'total_score': 590,
                        'year': 2023,
                    }
    """
    pipeline = [
        {'$match': {'Year': str(year)}},
        {'$sort': {'Total': -1}},
        {'$limit': 3}
    ]

    results_collection = db_client.get_collection('results')
    top_students = list(results_collection.aggregate(pipeline))


    top_students_summary = [find_aggregate(student) for student in top_students]

    return {"code": 200, "data": top_students_summary}