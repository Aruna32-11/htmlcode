from flask import Flask, request, jsonify
from pymongo import MongoClient


entry = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["Amazon"]
collection = db["user"]


@entry.route("/register", methods=['POST'])
def register():
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    password=data.get("password")
    if collection.find_one({"email":email}):
        return jsonify({"error":"email already exist"})
    collection.insert_one({"name":name,"email":email,"password":password})
    return jsonify ({"message":"registered successfully"})

@entry.route("/login", methods=['POST'])
def login():
    data=request.get_json()
    email=data.get("email")
    password=data.get("password")
    user=collection.find_one({"email":email,"password":password})
    if user:
        return jsonify({"message":"login sucessfull"})
    else:
        return jsonify({"error":"invalid login"})
if __name__ == "__main__":
    entry.run(debug=True)


