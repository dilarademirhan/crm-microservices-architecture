from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from .config.config import Config
from .routes.customer import customer_bp
from .extensions import db, jwt
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    jwt.init_app(app)
    db.init_app(app)
    
    # Swagger UI
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Customer Service API"
        }
    )
    
    # Register blueprints
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(customer_bp, url_prefix='/api/customers')
    
    return app