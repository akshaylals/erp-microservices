from .db import db

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, productId, quantity) -> None:
        self.productId = productId
        self.quantity = quantity
