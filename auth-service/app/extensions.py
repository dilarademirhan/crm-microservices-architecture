from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
jwt = JWTManager()
