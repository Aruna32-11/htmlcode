from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson import ObjectId

pagelimit=Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db=client["school"]
collection=db["student"]

@pagelimit.route('/students', methods=['GET'])
def get_student():

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 3))

    skip = (page - 1) * limit

    studentslist = []

    for student in collection.find().skip(skip).limit(limit):
        student["_id"] = str(student["_id"])
        studentslist.append(student)

    return jsonify(studentslist) 

if __name__ == "__main__":
    pagelimit.run(debug=True)