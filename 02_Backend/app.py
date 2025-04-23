# app.py
from flask import Flask, jsonify
from flask_restful import Resource, Api, request
import pyodbc


# Create the Flask app
app = Flask(__name__)
# Create an API object
api = Api(app)

ConnString = "Driver={ODBC Driver 18 for SQL Server};" \
    "Server=tcp:sql-server-cs188-anthony-sneddon.database.windows.net,1433;" \
    "Database=cherrydb;Uid=sql-server-admin;Pwd=CS188-spring-2025;" \
    "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

def get_db_connection():
    connection = pyodbc.connect(ConnString)
    return connection


class Register(Resource):
    def post(self):
        data = request.get_json()
        # Process registration data
        return {"message": "User registered successfully!"}, 201

class Login(Resource):
    def get(self):
        # Process login data
        return {"message": "Login successful!"}, 200

class SubmitOrder(Resource):
    def post(self):
        data = request.get_json()
        # Process order data
        return {"message": "Order submitted successfully!"}, 201

class LoadOrder(Resource):
    def get(self):
        # Load order data
        return {"order": "Order details"}, 200

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(SubmitOrder, '/submitorder')
api.add_resource(LoadOrder, '/loadorder')



if __name__ == "__main__":
    app.run(debug=True)