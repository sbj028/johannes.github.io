from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Enable CORS for all routes

# MySQL Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "",  # Replace with your MySQL password
    "database": "guest_registration"
}

# Route: Handle Registration Form Submission
@app.route('/submit_registration', methods=['POST'])
def register_guest():
    data = request.json

    # Extract data from request
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    message = data.get('message', '')

    # Validate input
    if not name or not email or not phone or not password:
        return jsonify({"message": "Please fill in all required fields"}), 400

    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Insert data into the database
        query = """
            INSERT INTO guests (name, email, phone, password, message)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, email, phone, hashed_password, message))
        connection.commit()

        return jsonify({"message": "Registration successful!"}), 200

    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"message": "A database error occurred"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
