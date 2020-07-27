from flask import Flask, jsonify, request
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


@app.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "name": request.json.get("name"),
        "price": request.json.get("price"),
        "quantity": request.json.get("quantity"),
    }
    products.append(new_product)
    return jsonify({"status": "OK", "message": "Product added", "products": products})


@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
    for index, product in enumerate(products):
        if product.get("name") == product_name:
            products[index] = request.json
            return jsonify({"message": "Product Updated", "product": products[index]})
    else:
        return jsonify({"error": "Product not Found", "message": "❌ Product not found"})


@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteProduct(product_name):
    for product in products:
        if product.get("name") == product_name:
            products.remove(product)
            return jsonify({"message": "Product Deleted", "delete_product": products,})
    else:
        return jsonify({"error": "Product not Found", "message": "❌ Product not found"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
