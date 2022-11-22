from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


@app.route("/")
def index() -> str:
    # transform a dict into an application/json response 
    return jsonify({"message": "It Works"})
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 