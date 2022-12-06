from flask import jsonify, request

from . import bp
from apps.db import db
from apps.models import Cart
from utils.auth import AuthError, requires_auth, requires_scope

@bp.route("", methods=['GET'])
@requires_auth
def get_all() -> str:
    cart_items = []
    for item in Cart.query.all():
        cart_items.append({
            "id": item.id,
            "productId": item.productId,
            "quantity": item.quantity
        })
    return jsonify(cart_items)


@bp.route("/<int:id>", methods=['GET'])
@requires_auth
def get_one(id) -> str:
    item = Cart.query.filter_by(id=id).first()
    if item:
        return jsonify({"cartitem": {
            "id": item.id,
            "productId": item.productId,
            "quantity": item.quantity
        }})
    return jsonify({"message": "Not found" }), 404
    

@bp.route("", methods=['POST'])
@requires_auth
def post() -> str:
    if not request.json:
        return jsonify({"message": "no data"}), 400

    productId = request.json['productId']
    quantity = request.json['quantity']
    item = Cart(productId, quantity)

    try:
        db.session.add(item)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": "bad request"}), 400
    else:
        return jsonify({
            "id": item.id,
            "productId": item.productId,
            "quantity": item.quantity
        }), 201


@bp.route("/<int:id>", methods=['DELETE'])
@requires_auth
def delete(id) -> str:
    try:
        item = Cart.query.filter_by(id=id)
    except:
        return jsonify({"message": "Internal Server Error" }), 500
    else:
        if item.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            return jsonify({"message": "Not found" }), 404

@bp.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response