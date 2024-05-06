from flask import Blueprint, request, jsonify
from .models import db, Category

categories_bp = Blueprint('categories', __name__)

# When creating a new category
@categories_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Missing category name'}), 400

    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify(new_category.serialize()), 201

# Now if user wants to see a list of categories
@categories_bp.route('/categories', methods=['GET'])
def list_categories():
    categories = Category.query.all()
    serialized_categories = [category.serialize() for category in categories]
    return jsonify(serialized_categories), 200

# For mainly admin purposes  update category by ID
@categories_bp.route('<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.get_json()

    if name in data:
        category.name = data['name']

    db.session.commit()
    return jsonify(category.serialize()), 200

# Also for admin purposes Delete a category by ID
@categories_bp.route('<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Categort successfully deleted!'}), 200