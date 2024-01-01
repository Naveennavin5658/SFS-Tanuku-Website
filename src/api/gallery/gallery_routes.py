from src.api.gallery import gallery_blueprint
from src.api.gallery.gallery_operations import fetch_images_for_event, get_events_for_year

@gallery_blueprint.route('/<year>',methods=["GET"])
#This API is for gallery home page
def fetch_results_of_year(year):
    try:
        response = get_events_for_year(year)
        return response, response['code']
    except Exception as e:
        print(f"******FAILED TO FETCH DATA DUE TO ERROR {e}******")

@gallery_blueprint.route('/<year>/<event>',methods=['GET'])
#This is for individual API click on any event
def fetch_detailed_images_of_event(year,event):
    try:
        response = fetch_images_for_event(year,event)
        if(response is []):
            return {"code":200,"data":[]}
        return {"code":200,"data":response}
    except Exception as e:
        print(f"******FAILED TO FETCH DATA DUE TO ERROR {e}******")