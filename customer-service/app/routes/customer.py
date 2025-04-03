from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.queryset.visitor import Q
from mongoengine.errors import DoesNotExist
from ..models.customer import Customer
from ..models.note import Note
from ..utils.auth import sales_rep_required
from functools import wraps

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/', methods=['POST'])
@jwt_required()
@sales_rep_required
def create_customer():
    data = request.get_json()
    current_user = get_jwt_identity()
    
    if Customer.objects(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        company=data.get('company'),
        address=data.get('address'),
        tags=data.get('tags', []),
        metadata=data.get('metadata', {}),
        created_by=current_user
    )
    
    customer.save()
    return jsonify(customer.to_dict()), 201


@customer_bp.route('/', methods=['GET'])
def get_customers():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    search = request.args.get('search', '')
    sort_by = request.args.get('sort_by', 'created_at')
    order = request.args.get('order', 'desc')
    
    # Başlangıçta boş bir sorgu oluşturuluyor
    query = Q()
    
    # Eğer search parametresi varsa, sorguya arama ekleniyor
    if search:
        query &= (Q(name__icontains=search) | Q(email__icontains=search) | Q(company__icontains=search))
    
    # Müşterileri sorgulama
    customers = Customer.objects(query)
    print(customers)  # Debugging: Kontrol etmek için çıktıyı yazdır
    
    # Sıralama işlemi
    if order == 'desc':
        customers = customers.order_by(f'-{sort_by}')
    else:
        customers = customers.order_by(sort_by)
    
    # Sayfalama işlemi
    customers = customers.skip((page - 1) * per_page).limit(per_page)
    
    # Müşterileri JSON formatına dönüştürüp döndürme
    return jsonify({
        'customers': [customer.to_dict() for customer in customers],
        'total': Customer.objects(query).count(),  # Toplam müşteri sayısını al
        'page': page,
        'per_page': per_page
    })



@customer_bp.route('/<customer_id>', methods=['GET'])
@jwt_required()
def get_customer(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        return jsonify(customer.to_dict())
    except DoesNotExist:
        return jsonify({"error": "Customer not found"}), 404


@customer_bp.route('/<customer_id>', methods=['PUT'])
@jwt_required()
@sales_rep_required
def update_customer(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except DoesNotExist:
        return jsonify({'error': 'Customer not found'}), 404

    data = request.get_json()
    
    if 'email' in data and data['email'] != customer.email:
        if Customer.objects(email=data['email']).first():
            return jsonify({'error': 'Email already registered'}), 400
        customer.email = data['email']
    
    if 'name' in data:
        customer.name = data['name']
    if 'phone' in data:
        customer.phone = data['phone']
    if 'company' in data:
        customer.company = data['company']
    if 'address' in data:
        customer.address = data['address']
    if 'tags' in data:
        customer.tags = data['tags']
    if 'metadata' in data:
        customer.metadata = data['metadata']
    
    customer.save()
    return jsonify(customer.to_dict())

@customer_bp.route('/<customer_id>', methods=['DELETE'])
@jwt_required()
@sales_rep_required
def delete_customer(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except DoesNotExist:
        return jsonify({'error': 'Customer not found'}), 404
    
    customer.delete()
    return '', 204

@customer_bp.route('/<customer_id>/notes', methods=['GET'])
@jwt_required()
@sales_rep_required
def get_notes_by_user(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except DoesNotExist:
        return jsonify({'error': 'Customer not found'}), 404
    
    notes = [note.to_dict() for note in customer.notes]
    return jsonify({'notes': notes}), 200

@customer_bp.route('/<customer_id>/notes', methods=['POST'])
@jwt_required()
@sales_rep_required
def add_note(customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return jsonify({'error': 'Customer not found'}), 404
    
    data = request.get_json()
    content = data.get('content', '').strip()
    current_user = get_jwt_identity()
    
    existing_note = next((note for note in customer.notes if note.content == content), None)
    if existing_note:
        return jsonify({'error': 'A note with the same content already exists'}), 400
    
    note = customer.add_note(content, current_user)
    
    return jsonify({
        'id': str(note.id),
        'content': note.content,
        'created_at': note.created_at.isoformat(),
        'created_by': note.created_by
    }), 201


@customer_bp.route('/notes/<note_id>', methods=['PUT'])
@jwt_required()
@sales_rep_required
def update_note(note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return jsonify({'error': 'Note not found'}), 404
    
    data = request.get_json()
    note.content = data.get('content', note.content)
    note.save()
    
    return jsonify({
        'id': str(note.id),
        'content': note.content,
        'created_at': note.created_at.isoformat(),
        'created_by': note.created_by
    })


@customer_bp.route('/notes/<note_id>', methods=['DELETE'])
@jwt_required()
@sales_rep_required
def delete_note(note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return jsonify({'error': 'Note not found'}), 404
    
    note.delete()
    
    return jsonify({'message': 'Note successfully deleted'}), 200



@customer_bp.route('/notes', methods=['GET'])
def get_notes():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    search = request.args.get('search', '')
    sort_by = request.args.get('sort_by', 'created_at')
    order = request.args.get('order', 'desc')
    
    query = Q()
    if search:
        query = Q(content__icontains=search)
    
    notes = Note.objects(query)
    
    # Apply sorting
    if order == 'desc':
        notes = notes.order_by(f'-{sort_by}')
    else:
        notes = notes.order_by(sort_by)
    
    # Apply pagination
    notes = notes.skip((page - 1) * per_page).limit(per_page)
    
    return jsonify({
        'notes': [note.to_dict() for note in notes],
        'total': Note.objects(query).count(),
        'page': page,
        'per_page': per_page
    })
