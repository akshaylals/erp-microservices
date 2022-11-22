from flask import Flask, jsonify, abort, request, Response
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, productId, quantity) -> None:
        self.productId = productId
        self.quantity = quantity



@app.route("/cart", methods=['GET'])
def get_all() -> str:
    cart_items = []
    for item in Cart.query.all():
        cart_items.append({
            "id": item.id,
            "productId": item.productId,
            "quantity": item.quantity
        })
    return jsonify({"cart": cart_items})


@app.route("/cart/<int:id>", methods=['GET'])
def get_one(id) -> str:
    item = Cart.query.filter_by(id=id).first()
    if item:
        return jsonify({"cartitem": {
            "id": item.id,
            "productId": item.productId,
            "quantity": item.quantity
        }})
    return jsonify({"message": "Not found" }), 404
    

@app.route("/cart", methods=['POST'])
def post() -> str:
    if not request.json:
        return jsonify({"message": "bad request"}), 400

    productId = request.json['productId']
    quantity = request.json['quantity']

    try:
        db.session.add(Cart(productId, quantity))
        db.session.commit()
    except Exception as e:
        return jsonify({"message": "bad request"}), 400
    else:
        return jsonify({"message": "success" }), 201


@app.route("/cart/<int:id>", methods=['DELETE'])
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

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 