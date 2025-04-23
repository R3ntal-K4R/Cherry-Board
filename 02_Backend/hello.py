# app.py
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import stripe

app = Flask(__name__)

# Config for SQLite (or you can use PostgreSQL, MySQL, etc.)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

# Create the tables
with app.app_context():
    db.create_all()

# Sample route
@app.route("/")
def index():
    return "Hello from Flask + DB!"


    CORS(app)

# Replace with your Stripe secret key
stripe.api_key = "sk_test_YOUR_SECRET_KEY"

@app.route("/create-payment-intent", methods=["POST"])
def create_payment():
    try:
        data = request.get_json()
        email = data.get("email", "")

        intent = stripe.PaymentIntent.create(
            amount=4999,  # $49.99 in cents
            currency="usd",
            receipt_email=email,
            automatic_payment_methods={"enabled": True},
        )

        return jsonify({"clientSecret": intent.client_secret})
    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == "__main__":
    app.run(debug=True)
