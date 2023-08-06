'''
Gallery blueprint handles all apis wrt to images
'''
from flask import Blueprint
alumni_blueprint = Blueprint("alumni",__name__)

from src.api.alumni import alumni_routes