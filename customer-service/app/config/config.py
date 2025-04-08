import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 
                                os.getenv('AUTH_SERVICE_ROLE_DOCKER_URL') if 'DOCKER' in os.environ 
                                else os.getenv('AUTH_SERVICE_ROLE_LOCAL_URL'))
    
    # MONGODB_SETTINGS = {
    #     'host': os.getenv('MONGODB_DOCKER_URL') if 'DOCKER' in os.environ else os.getenv('MONGODB_LOCAL_URL')
    #     }      
    
    MONGODB_SETTINGS = {
        'host': os.getenv(
            'MONGODB_URL', 
            os.getenv('MONGODB_DOCKER_URL') if 'DOCKER' in os.environ 
            else os.getenv('MONGODB_LOCAL_URL', 'mongodb://localhost:27017/customer-db')
        )
    }
     
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = 'headers'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'