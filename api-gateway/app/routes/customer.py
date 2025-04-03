from flask import Blueprint, request, jsonify
import requests
from ..config.config import Config
from flask import Blueprint

CUSTOMER_SERVICE_URL = Config.CUSTOMER_SERVICE_URL

customer_bp = Blueprint('customer', __name__, url_prefix='/api/customers')



@customer_bp.route('/api/customers', methods=['POST'])
def add_customer():
    response = requests.post(f"{CUSTOMER_SERVICE_URL}/customers", json=request.json)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/api/customers', methods=['GET'])
def get_customers():
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{CUSTOMER_SERVICE_URL}/customers", headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}", headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/api/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.put(f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}", json=request.json, headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/api/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.delete(f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}", headers=headers)
    return jsonify(response.json()), response.status_code
