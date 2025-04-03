from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from config import Config
from .routes.auth import auth_bp
from .extensions import jwt, db
from flasgger import Swagger


def create_app():
    app = Flask(__name__, static_folder='../static')

    app.config.from_object(Config)
    
    # Initialize extensions
    jwt.init_app(app)
    db.init_app(app)
    Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Swagger UI
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Auth Service API"
        }
    )
    
    # Register blueprints
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    
    return app 