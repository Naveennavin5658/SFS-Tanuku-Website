from src.api.results import results_blueprint
from src.api.results.results_operations import get_results, get_stats_in_year, get_toppers_of_year



@results_blueprint.route('/marks/<year>',methods=["GET"])
def fetch_results(year):
    try:
        response = get_results(year)
        return response, response['code']
    except Exception as e:
        print(f"******FAILED TO FETCH DATA DUE TO ERROR {e}******")


@results_blueprint.route('/stats/<year>',methods=['GET'])
def fetch_stats_of_year(year):
    try:
        response = get_stats_in_year(year)
        return response, response['code']
    except Exception as e:
        print(f"******FAILED TO FETCH DATA DUE TO ERROR {e}******")


@results_blueprint.route('/toppers/<year>',methods = ['GET'])
def fetch_toppers_of_year(year):
    try:
        response = get_toppers_of_year(year)
        return response, response['code']
    except Exception as e:
        print(f"******FAILED TO FETCH DATA DUE TO ERROR {e}******")