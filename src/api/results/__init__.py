'''
Gallery blueprint handles all apis wrt to images
'''
from flask import Blueprint
results_blueprint = Blueprint("results",__name__)

from src.api.results import results_routes