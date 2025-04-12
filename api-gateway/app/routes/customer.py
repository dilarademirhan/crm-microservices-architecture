from flask import Blueprint, request, jsonify
import requests
from ..config.config import Config
from flask import Blueprint

CUSTOMER_SERVICE_API_URL = f"{Config.CUSTOMER_SERVICE_URL}/api/customers"

customer_bp = Blueprint('customer', __name__, url_prefix='/api/customers')

@customer_bp.route('', methods=['POST'])
def add_customer():
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.post(f"{CUSTOMER_SERVICE_API_URL}", json=request.json, headers=headers)
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

# Note endpoints
@customer_bp.route('/<customer_id>/notes', methods=['GET'])
def get_notes_by_customer(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f"{CUSTOMER_SERVICE_API_URL}/{customer_id}/notes", headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/<customer_id>/notes', methods=['POST'])
def add_note(customer_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.post(f"{CUSTOMER_SERVICE_API_URL}/{customer_id}/notes", json=request.json, headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.put(f"{CUSTOMER_SERVICE_API_URL}/notes/{note_id}", json=request.json, headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.delete(f"{CUSTOMER_SERVICE_API_URL}/notes/{note_id}", headers=headers)
    return jsonify(response.json()), response.status_code

@customer_bp.route('/notes', methods=['GET'])
def get_all_notes():
    headers = {'Authorization': request.headers.get('Authorization')}
    params = {
        'page': request.args.get('page', 1),
        'per_page': request.args.get('per_page', 10),
        'search': request.args.get('search', ''),
        'sort_by': request.args.get('sort_by', 'created_at'),
        'order': request.args.get('order', 'desc')
    }
    response = requests.get(f"{CUSTOMER_SERVICE_API_URL}/notes", headers=headers, params=params)
    return jsonify(response.json()), response.status_code


