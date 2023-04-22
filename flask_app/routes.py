from . import app, db
from flask import jsonify, request
from flask_app.models import User
from flask_app.utils import check_and_update


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users', methods=['POST'])
def add_new_user():
    new_user = request.get_json()
    new_user = User(username=new_user['username'], password=new_user['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 200

@app.route('/users/<string:username>', methods=['GET'])
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