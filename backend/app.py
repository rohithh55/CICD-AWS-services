from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "company"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "password")
    )

@app.get("/employees")
def employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(result)

@app.get("/")
def home():
    return {"status": "Backend Running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
