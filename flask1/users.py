from flask import Flask, jsonify
from pymongo import MongoClient

users = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["student"]

@users.route("/viewproducts", methods=["GET"])
def view_products():
    data = []
    for pro in collection.find():
        pro["_id"] = str(pro["_id"])
        data.append(pro)
    return jsonify(data)

@users.route("/viewproducts/<id>", methods=["GET"])
def view_product_by_id(id):
    from bson import ObjectId
    product = collection.find_one({"_id": ObjectId(id)})
    
    if product:
        product["_id"] = str(product["_id"])
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"})

if __name__ == "__main__":
    users.run(debug=True)