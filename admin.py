from flask import Blueprint, jsonify
from models import User
from decorators import role_required
from flask_jwt_extended import jwt_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/users', methods=['GET'])
@jwt_required()
@role_required('Admin')
def list_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "name": u.name,
        "email": u.email,
        "role": u.role
    } for u in users])