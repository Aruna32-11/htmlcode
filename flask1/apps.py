from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

apps = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["LibraryDB"]
books = db["books"]


@apps.route("/add_book", methods=["POST"])
def add_book():
    data = request.get_json()
    result = books.insert_one(data)
    return jsonify({
        "message": "Book added successfully",
        "id": str(result.inserted_id)
    })

@apps.route("/get_books", methods=["GET"])
def get_books():
    data = []
    for book in books.find():
        book["_id"] = str(book["_id"])
        data.append(book)
    return jsonify(data)


@apps.route("/get_book/<id>", methods=["GET"])
def get_book(id):
    book = books.find_one({"_id": ObjectId(id)})
    if book:
        book["_id"] = str(book["_id"])
        return jsonify(book)
    return jsonify({"message": "Book not found"})


@apps.route("/update_book/<id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    books.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return jsonify({"message": "Book updated successfully"})


@apps.route("/delete_book/<id>", methods=["DELETE"])
def delete_book(id):
    books.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Book deleted successfully"})


if __name__ == "__main__":
    apps.run(debug=False)

    