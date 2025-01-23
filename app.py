import os # Import the os module to access environment variables
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Enable CORS for all routes

""" # MySQL Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "",  # Replace with your MySQL password
    "database": "guest_registration"
} """

# Environment variables for sensitive data
db_connection = mysql.connector.connect(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME")
)


# Route: Handle Registration Form Submission
@app.route('/event_registration', methods=['POST'])
def register_guest():
    data = request.json

    # Extract data from request
    name = data.get('name')
    bringing_family = data.get('bringing_family')
    family_members = data.get('family_members')
    food = data.get('food')

    # Validate input
    if not name or not bringing_family or not family_members or not food:
        return jsonify({"message": "Please fill in all required fields"}), 400

    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert data into the database
        query = """
            INSERT INTO guests (name, bringing_family, family_members, food)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, bringing_family, family_members, food))
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
