# app.py
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_bcrypt import Bcrypt
import pyodbc

# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to something secure
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize extensions
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Azure SQL connection string
ConnString = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:sql-server-cs188-anthony-sneddon.database.windows.net,1433;"
    "Database=cherrydb;Uid=sql-server-admin;Pwd=CS188-spring-2025;"
    "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
)

def get_db_connection():
    return pyodbc.connect(ConnString)

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# API Resources
class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"message": "Missing username or password"}, 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {"message": "Username already taken"}, 409

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully!"}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return {"message": "Login successful!"}, 200
        return {"message": "Invalid credentials"}, 401

class SubmitOrder(Resource):
    @login_required
    def post(self):
        data = request.get_json()
        return {"message": "Order submitted successfully!"}, 201

class LoadOrder(Resource):
    @login_required
    def get(self):
        return {"order": "Order details for user: " + current_user.username}, 200

# Register API endpoints
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(SubmitOrder, '/submitorder')
api.add_resource(LoadOrder, '/loadorder')

# Create DB if it doesn't exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
