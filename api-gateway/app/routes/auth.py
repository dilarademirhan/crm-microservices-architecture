from flask import request, jsonify
import requests
from ..config.config import Config
from flask import Blueprint

AUTH_SERVICE_API_URL = f"{Config.AUTH_SERVICE_URL}/api/auth"

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    response = requests.post(f"{AUTH_SERVICE_API_URL}/register", json=request.json)
    return jsonify(response.json()), response.status_code

@auth_bp.route('/login', methods=['POST'])
def login():
    response = requests.post(f"{AUTH_SERVICE_API_URL}/login", json=request.json)
    return jsonify(response.json()), response.status_code

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{AUTH_SERVICE_API_URL}/me", headers=headers)
    return jsonify(response.json()), response.status_code

@auth_bp.route('/users', methods=['GET'])
def get_users():
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{AUTH_SERVICE_API_URL}/users", headers=headers)
    return jsonify(response.json()), response.status_code

@auth_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.put(f"{AUTH_SERVICE_API_URL}/users/{user_id}", json=request.json, headers=headers)
    return jsonify(response.json()), response.status_code

@auth_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.delete(f"{AUTH_SERVICE_API_URL}/users/{user_id}", headers=headers)
    return jsonify(response.json()), response.status_code

@auth_bp.route('/user-role', methods=['GET'])
def get_user_role():
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{AUTH_SERVICE_API_URL}/user-role", headers=headers)
    return jsonify(response.json()), response.status_code
