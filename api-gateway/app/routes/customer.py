from flask import Blueprint, request, jsonify
import requests
from ..config.config import Config
from flask import Blueprint

CUSTOMER_SERVICE_API_URL = f"{Config.CUSTOMER_SERVICE_URL}/api/customers"

customer_bp = Blueprint('customer', __name__, url_prefix='/api/customers')

@customer_bp.route('', methods=['POST'])
def add_customer():
    response = requests.post(f"{CUSTOMER_SERVICE_API_URL}", json=request.json)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/', methods=['GET'])
def get_customers():
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{CUSTOMER_SERVICE_API_URL}", headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{CUSTOMER_SERVICE_API_URL}/{customer_id}", headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.put(f"{CUSTOMER_SERVICE_API_URL}/{customer_id}", json=request.json, headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.delete(f"{CUSTOMER_SERVICE_API_URL}/{customer_id}", headers=headers)
    return jsonify(response.json()), response.status_code
