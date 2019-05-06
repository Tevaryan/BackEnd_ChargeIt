from flask import Blueprint, render_template, jsonify, url_for, request
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['POST'])
def new():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)

    user_password = password
    hashed_password = generate_password_hash(user_password)

    username_check = User.get_or_none(User.username == username)

    if not username_check :

        u = User(username=username, email=email, password=generate_password_hash(password))

        u.save()
        user = User.get(User.username == username)
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "message": "Successfully created a user and signed in.",
            "status": "success",
            "user": {
                "id": user.id,
                "username": user.username
            }
        }), 200
    else:
        return jsonify({"msg": "username or email already used"}), 400

@users_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.get_or_none(User.username == username)
    if user and check_password_hash(user.password, password):
        new_user_id = user.id
        access_token = create_access_token(new_user_id)
    
        return jsonify({
                "access_token": access_token,
                "message": "Successfully signed in.",
                "status": "success",
                "user": {
                    "id": user.id,
                    "username": user.username
                }
            }), 200
    else:
        return jsonify({"msg": "Bad login"}), 404


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
