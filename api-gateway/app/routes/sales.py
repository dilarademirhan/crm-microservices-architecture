from flask import request, jsonify
import requests
from ..config.config import Config
from flask import Blueprint

SALES_SERVICE_API_URL = f"{Config.SALES_SERVICE_URL}/api/sales"

sale_bp = Blueprint('sales', __name__, url_prefix='/api/sales')

@sale_bp.route('/', methods=['GET'])
def get_sales():
    response = requests.get(f"{SALES_SERVICE_API_URL}")
    return jsonify(response.json()), response.status_code

@sale_bp.route('/<sale_id>', methods=['GET'])
def get_sale(sale_id):
    response = requests.get(f"{SALES_SERVICE_API_URL}/{sale_id}")
    return jsonify(response.json()), response.status_code

@sale_bp.route('', methods=['POST'])
def create_sale():
    response = requests.post(f"{SALES_SERVICE_API_URL}", json=request.json)
    return jsonify(response.json()), response.status_code

@sale_bp.route('/sale-stages', methods=['POST'])
def create_sale_stage():
    response = requests.post(f"{SALES_SERVICE_API_URL}/sale-stages", json=request.json)
    return jsonify(response.json()), response.status_code

@sale_bp.route('/<sale_id>/last-stage', methods=['GET'])
def get_last_stage(sale_id):
    response = requests.get(f"{SALES_SERVICE_API_URL}/{sale_id}/last-stage")
    return jsonify(response.json()), response.status_code
