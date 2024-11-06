from models.user import User
from flask import jsonify, Blueprint

user_blueprint = Blueprint('user_bp', __name__, url_prefix="/users")

@user_blueprint.route('/')
def index():
    users = User.query.all()
    return jsonify({"users": users[0].name}), 201

@user_blueprint.route('/update')
def update():
    return "Este es una ruta para actualizar usuarios", 200