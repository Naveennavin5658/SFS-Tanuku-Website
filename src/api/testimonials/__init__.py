'''
Gallery blueprint handles all apis wrt to images
'''
from flask import Blueprint
testimonials_blueprint = Blueprint("testimonials",__name__)

from src.api.testimonials import testimonials_routes