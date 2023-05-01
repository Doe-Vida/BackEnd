from . import app, db
from flask import jsonify, request
from flask_app.models import User
from flask_app.utils import check_and_update, check_username, token_required
import jwt
from flask_jwt_extended import jwt_required

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users', methods=['POST'])
def add_new_user():
    new_user = request.get_json()
    validation = check_username(new_user['username'])
    if validation != None:
        return validation, 400
    new_user = User(username=new_user['username'], password=new_user['password'])
    new_user.set_password(new_user.password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 200

@app.route('/login', methods=["POST"])
def login():
    user = request.get_json()
    try:
        user_db = User.query.filter_by(username=user["username"]).first()
        print(user_db.check_password(user["password"]))
        if user_db.check_password(user["password"]) == True:
            payload = {'user_id': user_db.id, 'exp': None}
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            return {'token': token}, 200
        else:
            return jsonify({"Erro": "Wrong password"}), 403
    except:
        return jsonify({"Erro": "User not found"}), 404


@app.route('/users/<string:username>', methods=['GET'])
@token_required
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"Error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"Error": "User not found"}), 404
    return jsonify(user.to_dict()), 200
    
@app.route('/users/<string:username>', methods=['PUT'])
def update_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"Error": "User not found"}), 404
    changed_password = request.get_json()
    user = check_and_update(user, **changed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 200


@app.route('/users/<string:username>', methods=['DELETE'])
def delete_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"Error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": "deleted user"}), 200