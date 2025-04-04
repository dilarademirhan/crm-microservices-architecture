from flask import Flask
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from .config.config import Config
from .routes.sales import sale_bp
from .routes.auth import auth_bp
from .routes.customer import customer_bp

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../static')

    app.config.from_object(config_class)
    
    # Initialize JWT
    jwt.init_app(app)

    
    # Swagger UI
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "CRM API Gateway"
        }
    )
    
    # Register blueprints
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(auth_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(sale_bp)
    
    return app 