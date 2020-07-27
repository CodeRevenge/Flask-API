from flask import Flask, jsonify
from products import products

app = Flask(__name__)


@app.route("/ping")
def home():
    return jsonify({"message": "pong!"})


@app.route("/products", methods=["GET"])
def getProducts():
    return jsonify({"products": products})


@app.route("/products/<string:product_name>")
def getProduct(product_name):
    for product in products:
        if product.get("name") == product_name:
            return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not Found", "message": "❌ Product not found"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
