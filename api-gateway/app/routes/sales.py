from flask import request, jsonify
import requests
from ..config.config import Config
from flask import Blueprint

SALE_SERVICE_URL = Config.SALES_SERVICE_URL

sale_bp = Blueprint('sales', __name__, url_prefix='/api/sales')

@sale_bp.route('/', methods=['GET'])
def get_sales():
    print("Yönlendirilen URL:", f"{SALE_SERVICE_URL}/api/sales")
    response = requests.get(f"{SALE_SERVICE_URL}/api/sales")
    return jsonify(response.json()), response.status_code

@sale_bp.route('/<sale_id>', methods=['GET'])
def get_sale(sale_id):
    response = requests.get(f"{SALE_SERVICE_URL}/sales/{sale_id}")
    return jsonify(response.json()), response.status_code

@sale_bp.route('/', methods=['POST'])
def create_sale():
    response = requests.post(f"{SALE_SERVICE_URL}/sales", json=request.json)
    return jsonify(response.json()), response.status_code

@sale_bp.route('/sale-stages', methods=['POST'])
def create_sale_stage():
    response = requests.post(f"{SALE_SERVICE_URL}/sale-stages", json=request.json)
    return jsonify(response.json()), response.status_code

@sale_bp.route('/<sale_id>/last-stage', methods=['GET'])
def get_last_stage(sale_id):
    response = requests.get(f"{SALE_SERVICE_URL}/sales/{sale_id}/last-stage")
    return jsonify(response.json()), response.status_code
