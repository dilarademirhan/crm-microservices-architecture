from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

db = MongoEngine()
jwt = JWTManager()
 