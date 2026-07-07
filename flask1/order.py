from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

order = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["orderstatus"]

@order.route("/addpro", methods = ['POST'])
def addproduct():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"message": "Product added successfully!"})

@order.route("/getpro", methods = ["GET"])
def getproduct():
    data = []
    for pro in collection.find():
        # We are changing the id's type which is by default in object.
        # So changing to the string.
        pro["_id"] = str(pro["_id"])
        data.append(pro)
    return jsonify(data)

@order.route("/getpro/<id>", methods = ["GET"])
def getidproduct(id):
    data = collection.find_one({"_id": ObjectId(id)})
    data["_id"] = str(data["_id"])
    return jsonify(data)

@order.route("/update/<id>", methods = ["PUT"])
def updateproduct(id):
    data = request.get_json()
    sample = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    print(sample)
    return jsonify({"message": "Product updated successfully!"})

@order.route("/delete/<id>", methods = ["DELETE"])
def deleteproduct(id):
    collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Product deleted successfully!"})

if __name__ == '__main__':
    order.run(debug=True)