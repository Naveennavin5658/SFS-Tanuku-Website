'''
Gallery blueprint handles all apis wrt to images
'''
from flask import Blueprint
home_page_blueprint = Blueprint("home",__name__)

from src.api.home_page import home_page_routes