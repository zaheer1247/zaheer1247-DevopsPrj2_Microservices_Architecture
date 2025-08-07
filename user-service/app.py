from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL connection config
DB_HOST = "postgres"
DB_NAME = "users"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

def get_db_connection():
    print("Establishing connection to PostgreSQL database...")  # sysout
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/")
def home():
    print("Root endpoint '/' was accessed")  # sysout
    return jsonify({"message": "User Service is running"}), 200

@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    print("Received registration data:", data)  # Print input data

    name = data.get("name")
    info = data.get("info")

    if not name or not info:
        print("Missing name or info")  # Print a warning
        return jsonify({"error": "Name and info are required"}), 400

    try:
        print("Call get_db_connection")  # sysout
        conn = get_db_connection()
        cur = conn.cursor()
        print(f"Inserting user into database: name={name}, info={info}")
        cur.execute("INSERT INTO usersdata (name, info) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING", (name, info))
        conn.commit()
        cur.close()
        conn.close()
        print("User inserted successfully")  # Print confirmation
        return jsonify({"message": f"User '{name}' registered successfully"}), 201
    except Exception as e:
        print("Database error:", e)  # Print exception details
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask app on http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

