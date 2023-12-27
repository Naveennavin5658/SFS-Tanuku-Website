from apispec import APISpec
from flask_apispec import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_compress import Compress


from src import api


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    
    
    Compress(app)
    JWTManager(app)

    CORS(app)

    api_spec = APISpec(
        title="SFS School API",
        version="v1",
        openapi_version="3.0.2",
        plugins=[MarshmallowPlugin()],
    )
    api_key_scheme = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
    api_spec.components.security_scheme("ApiKeyAuth", api_key_scheme)

    app.config.update(
        {
            "APISPEC_SPEC": api_spec,
            "APISPEC_SWAGGER_URL": "/swagger/",
        }
    )
    docs = FlaskApiSpec(app, document_options=False)

    register_blueprints(app, docs)
    return app
from src.api.gallery import gallery_blueprint
from src.api.alumni import alumni_blueprint
from src.api.home_page import home_page_blueprint
from src.api.results import results_blueprint
from src.api.testimonials import testimonials_blueprint

def register_blueprints(app: Flask, docs: FlaskApiSpec):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)


    app.register_blueprint(gallery_blueprint, url_prefix='/gallery')
    app.register_blueprint(alumni_blueprint, url_prefix='/alumni')
    app.register_blueprint(home_page_blueprint, url_prefix='/home')
    app.register_blueprint(results_blueprint, url_prefix='/results')
    app.register_blueprint(testimonials_blueprint, url_prefix='/testimonials')
