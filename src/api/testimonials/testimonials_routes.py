from src.api.testimonials import testimonials_blueprint
from src.api.testimonials.testimonials_operations import get_reviews
@testimonials_blueprint.route('/reviews',methods=["GET"])
def fetch_results():
    try:
        response = get_reviews()
        return response, response['code']
    except Exception as e:
        print(f"******FAILED TO FETCH DATA DUE TO ERROR {e}******")