from flask import Blueprint, request, jsonify
from models.user import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
import os

bcrypt = Bcrypt()
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(name=data['name'], email=data['email'], password=hashed_password)
    user.save()
    return jsonify({"message": "User registered successfully"})

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.objects(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401
