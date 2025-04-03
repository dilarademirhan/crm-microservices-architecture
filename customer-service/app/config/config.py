# import os
# from datetime import timedelta

# class Config:
#     # Flask
#     SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    
#     # MongoDB
#     MONGODB_SETTINGS = {
#         'host': os.getenv('MONGODB_URL', 'mongodb://admin:admin123@localhost:27017/crm_db'),
#         'db': 'crm_db'
#     }
    
#     # JWT
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-super-secret-key-here')
#     JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30)))
    
#     # API
#     API_TITLE = 'Customer Service API'
#     API_VERSION = 'v1'
#     OPENAPI_VERSION = '3.0.2'
#     OPENAPI_URL_PREFIX = '/'
#     OPENAPI_SWAGGER_UI_PATH = '/swagger-ui'
#     OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/' 