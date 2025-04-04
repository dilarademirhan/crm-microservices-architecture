import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL')
    MONGODB_URL = os.getenv('MONGODB_URL')
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = 'headers'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'