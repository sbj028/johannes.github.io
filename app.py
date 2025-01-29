import os # Import the os module to access environment variables
from flask import Flask, request, redirect, url_for, jsonify, render_template
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Enable CORS for all routes

# Environment variables for sensitive data
db_connection = mysql.connector.connect(
    host=os.getenv("DATABASE_HOST"), # Doppler provides this environment variable
    user=os.getenv("DATABASE_USER"), # Doppler provides this environment variable
    password=os.getenv("DATABASE_PASSWORD"), # Doppler provides this environment variable
    database=os.getenv("DATABASE_NAME")  # Doppler provides this environment variable
)

@app.route('/')
def home():
    return render_template('index.html')


# Route: Handle Registration Form Submission
@app.route('/event_registration', methods=['POST', 'GET'])
def register_guest():
    if request.method == 'GET':
        return "This is the event registration endpoint. Use POST to submit data.", 200

    # Extract data from request form: 

    name = request.form.get('name')
    bringing_family = int(request.form.get('bringing_family',0))
    family_members = int(request.form.get('family_members', 0))

    food = int(request.form.get('food'))

    print(f'request.form is' , request.form) 
   
    # Validate input
    # # Basic check for truly missing fields:
    bringing_family_str = request.form.get('bringing_family')
    family_members_str = request.form.get('family_members')
    food_str = request.form.get('food')

    if not all([name.strip(), bringing_family_str, family_members_str, food_str]):
        return "Please fill in all required fields", 400

    # Debugging: 

    print(request.form)
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME")
            )

        cursor = connection.cursor()

        # Insert data into the database
        query = """
            INSERT INTO guests (name, bringing_family, family_members, food)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, bringing_family, family_members, food))
        connection.commit()

        # 4. On success, redirect to the success page
        return redirect(url_for('registration_success.html'))

        #return jsonify({"message": "Registration successful!"}), 200

    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"message": "A database error occurred"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Route: Registration Success Page
@app.route('/registration_success')
def registration_success():
    # return "Registration successful!"
    # Render the separate 'registration_success.html' file
    return render_template('registration_success.html')

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
