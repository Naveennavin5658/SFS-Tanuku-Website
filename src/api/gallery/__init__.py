'''
Gallery blueprint handles all apis wrt to images
'''
from flask import Blueprint
gallery_blueprint = Blueprint("gallery",__name__)

from src.api.gallery import gallery_routes