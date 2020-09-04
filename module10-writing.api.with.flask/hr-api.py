import json

from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

from utility.rest import convert_request_to_dictionary

client = MongoClient("mongodb://localhost:27017")

hr = client['hr']  # database

employees = hr.employees  # collection

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

"""
REST API
curl -X POST http://localhost:7001/hr/api/v1/employees -H "Content-Type: application/json" -H "Accept: application/json" -d "{ \"identity\": \"1\", \"fullname\": \"james sawyer\"}"
"""
fields = ["identity", "fullName", "iban", "photo", "birthYear", "salary", "department", "fulltime"]


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


# http://localhost:7001/hr/api/v1/employees/1
@app.route("/hr/api/v1/employees/<identity>", methods=['GET'])
def getEmployeeByIdentity(identity):
    return jsonify(employees.find_one({"identity": identity}))


# http://localhost:7001/hr/api/v1/employees
@app.route("/hr/api/v1/employees", methods=['GET'])
def getEmployees():
    return json.dumps([emp for emp in employees.find({})])


# http://localhost:7001/hr/api/v1/employees
@app.route("/hr/api/v1/employees", methods=['POST'])
def addEmployee():
    print(f"addEmployee(): {request.json}")
    emp = {}
    for field in fields:
        if field in request.json:
            emp[field] = request.json[field]
    emp["_id"] = emp["identity"]
    employees.insert_one(emp)
    socketio.emit("hire", emp)
    return jsonify({"status": "ok"})


# http://localhost:7001/hr/api/v1/employees/1
@app.route("/hr/api/v1/employees/<identity>", methods=['PUT'])
def updateEmployee(identity):
    print(f"updateEmployee({identity}): {request.json}")
    emp = convert_request_to_dictionary(request, fields)
    document = employees.find_one_and_update(
        {"_id": identity},
        {"$set": emp},
        upsert=False
    )
    return jsonify(document)


# http://localhost:7001/hr/api/v1/employees/2
@app.route("/hr/api/v1/employees/<identity>", methods=['PATCH'])
def patchEmployee(identity):
    print(f"patchEmployee({identity}): {request.json}")
    emp = convert_request_to_dictionary(request, fields)
    document = employees.find_one_and_update(
        {"_id": identity},
        {"$set": emp},
        upsert=False
    )
    return jsonify(document)


# http://localhost:7001/hr/api/v1/employees/2
@app.route("/hr/api/v1/employees/<identity>", methods=['DELETE'])
def removeEmployee(identity):
    print(f"removeEmployee({identity})")
    emp = employees.find_one({"_id": identity})
    employees.delete_one({"_id": identity})
    socketio.emit("fire", emp)
    return jsonify(emp)


##if __name__ == '__main__':
socketio.run(app, port=7001)
