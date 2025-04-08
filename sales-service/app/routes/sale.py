import uuid
from flask import Blueprint, request, jsonify
from ..models.sale import Sale
from ..models.sale_stage import SaleStage
from ..models.base import db

sale_bp = Blueprint('sale', __name__)

@sale_bp.route('/', methods=['GET'])
def get_sales():
    try:
        sales = Sale.query.all()
        return jsonify([sale.to_dict() for sale in sales]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@sale_bp.route('/<uuid:sale_id>', methods=['GET'])
def get_sale(sale_id):
    try:
        sale = Sale.query.get(sale_id)
        if not sale:
            return jsonify({'error': 'Sale not found!'}), 404
        return jsonify(sale.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@sale_bp.route('/', methods=['POST'])
def create_sale():
    try:
        data = request.get_json()
        
        customer_id = data.get('customer_id')
        name = data.get('name')
        product = data.get('product')
        amount = data.get('amount')

        if not all([customer_id, name, product, amount]):
            return jsonify({'error': 'You must provide all required fields!'}), 400
        
        new_sale = Sale(
            customer_id=uuid.UUID(customer_id),
            name=name,
            product=product,
            amount=amount
        )

        db.session.add(new_sale)
        db.session.commit()

        initial_stage = SaleStage(
            sale_id=new_sale.id,
            name='Initial Stage',
            notes='Initial stage of the sale.'
        )

        db.session.add(initial_stage)
        db.session.commit()

        return jsonify(new_sale.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@sale_bp.route('/sale-stages', methods=['POST'])
def create_sale_stage():
    try:
        data = request.get_json()

        sale_id = data.get('sale_id')
        name = data.get('name')
        notes = data.get('notes', '')

        if not sale_id or not name:
            return jsonify({'error': 'sale_id and name fields required.'}), 400

        sale = Sale.query.get(uuid.UUID(sale_id))
        if not sale:
            return jsonify({'error': 'Invalid sale_id!'}), 404

        new_stage = SaleStage(
            sale_id=sale.id,
            name=name,
            notes=notes
        )

        db.session.add(new_stage)
        db.session.commit()

        return jsonify(new_stage.to_dict()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@sale_bp.route('/<sale_id>/last-stage', methods=['GET'])
def get_last_stage(sale_id):
    try:
        try:
            sale_uuid = uuid.UUID(sale_id)
        except ValueError:
            return jsonify({'error': 'Invalid sale_id format!'}), 400

        last_stage = SaleStage.query.filter_by(sale_id=sale_uuid) \
            .order_by(SaleStage.created_at.desc()) \
            .first()

        if not last_stage:
            return jsonify({'error': 'No stages found for the given sale_id!'}), 404

        return jsonify(last_stage.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500