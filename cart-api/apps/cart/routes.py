from flask import jsonify, request

from . import bp
from apps.db import db
from apps.models import Cart
from apps.config import Config

from authlib.integrations.flask_oauth2 import ResourceProtector
from utils.validator import Auth0JWTBearerTokenValidator

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    Config.AUTH0_DOMAIN,
    Config.API_AUDIENCE
)
require_auth.register_token_validator(validator)

@bp.route("", methods=['GET'])
@require_auth(None)
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
@require_auth(None)
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
@require_auth(None)
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
@require_auth(None)
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
