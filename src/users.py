from flask import Blueprint, jsonify, abort, request
from .models import User, db
import hashlib
import secrets

users_bp = Blueprint('users', __name__)

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

# Creating a new user
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing username, email, and/or password'}), 400

    hashed_password = scramble(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 201

# List all users
@users_bp.route('/user/<int:user_id>', methods=['GET'])
def list_users():
    users = User.query.all()
    serialized_users = [user.serialize() for user in users]
    return jsonify(serialized_users), 200

# Update user by ID
@users_bp.route('<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password = scramble(data['password'])

    db.session.commit()
    return jsonify(user.serialize()), 200

# Delete user by ID
@users_bp.route('<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User successfully deleted'}), 200
