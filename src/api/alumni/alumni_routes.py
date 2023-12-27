from flask import request
from src.api.alumni import alumni_blueprint
from src.api.alumni.alumni_operations import add_user_as_alumni
@alumni_blueprint.route('/register',methods=["POST"])
def register_alumni():
    try:
        response = add_user_as_alumni(request)
        return response, response['code']
    except Exception as e:
        print(f"******FAILED TO INSERT RECORD DUE TO ERROR {e}******")
        