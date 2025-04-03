import os
from datetime import timedelta

class Config:
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    
    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30)))
    
    # Service URLs
    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 'http://127.0.0.1:5000')
    CUSTOMER_SERVICE_URL = os.getenv('CUSTOMER_SERVICE_URL', 'http://127.0.0.1:5001')
    SALES_SERVICE_URL = os.getenv('SALES_SERVICE_URL', 'http://sales-service:5002' if 'DOCKER' in os.environ else 'http://127.0.0.1:5002')    
    # API
    API_TITLE = 'CRM API Gateway'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/swagger-ui'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/' 