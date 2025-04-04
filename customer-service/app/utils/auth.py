import requests
from flask import request, jsonify
from functools import wraps
from ..config.config import Config
import os

AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 'http://auth-service:5000' if 'DOCKER' in os.environ else 'http://127.0.0.1:5000') 


def sales_rep_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization") 
        if not token:
            return jsonify({"error": "Authorization token is missing"}), 401

        headers = {"Authorization": token}
        response = requests.get(AUTH_SERVICE_URL, headers=headers)

        if response.status_code != 200:
            return jsonify({"error": "Authentication failed"}), 401

        role = response.json().get("role")
        if role != "sales_rep":
            return jsonify({"error": "Permission denied"}), 403

        return f(*args, **kwargs)
    return decorated_function
