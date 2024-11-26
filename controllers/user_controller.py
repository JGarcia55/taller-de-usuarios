from models.user import User, UserSchema
from flask import jsonify, Blueprint, request

user_blueprint = Blueprint('user_bp', __name__, url_prefix="/users")

@user_blueprint.route('/', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def index():
    if request.method == "GET":
        users_schema = UserSchema(many=True)
        users = User.query.all()
        users = users_schema.dump(users)
        for user in users:
            user["es_sano"] = True
        return jsonify({"users": users}), 201
    if request.method == "POST":
        users = User.query.all()
        return jsonify({"users": users[0].email}), 201
    if request.method == "PUT":
        users = User.query.all()
        return jsonify({"users": users[0].email}), 201

@user_blueprint.route('/update')
def update():
    return "Este es una ruta para actualizar usuarios", 200