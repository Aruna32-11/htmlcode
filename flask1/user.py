from flask import Flask, request, jsonify
from pymongo import MongoClient

user= Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["identity"]


# POST - Create student
@user.route('/student', methods=['POST'])
def create_student():
    data = request.get_json()

    email_id=data.get("email_id")
    username = data.get("username")
    password = data.get("password")

    student = {
        "email_id": email_id,
        "username": username,
        "password": password
    }

    collection.insert_one(student)

    return jsonify({"message": "Student added successfully"})


# GET - Read students
@user.route('/student', methods=['GET'])
def get_students():
    students = []

    for s in collection.find({}, {"_id": 0}):
        students.append(s)

    return jsonify(students)


if __name__ == "__main__":
    user.run(debug=True)