from flask import Flask, request, jsonify
import sqlite3
import time

app = Flask(__name__)

# Simulate a 10-second delay for all responses
def delayed_response(data):
    time.sleep(10)
    return jsonify(data)

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS inventory (name TEXT PRIMARY KEY, quantity INTEGER)")
    conn.commit()
    conn.close()

init_db()  # Ensure database is initialized

@app.route("/transform", methods=["POST"])
def transform():
    data = request.json
    print(f"Received transform data: {data}")
    return delayed_response({"message": "Transform received", "status": 200})

@app.route("/translation", methods=["POST"])
def translation():
    data = request.json
    print(f"Received translation data: {data}")
    return delayed_response({"message": "Translation received", "status": 200})

@app.route("/rotation", methods=["POST"])
def rotation():
    data = request.json
    print(f"Received rotation data: {data}")
    return delayed_response({"message": "Rotation received", "status": 200})

@app.route("/scale", methods=["POST"])
def scale():
    data = request.json
    print(f"Received scale data: {data}")
    return delayed_response({"message": "Scale received", "status": 200})

@app.route("/file-path", methods=["GET"])
def file_path():
    project_path = request.args.get("projectpath", "false").lower() == "true"
    file_path = "/path/to/maya/file.mb" if not project_path else "/path/to/project"
    return delayed_response({"file_path": file_path})

@app.route("/add-item", methods=["POST"])
def add_item():
    data = request.json
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (data["name"], data["quantity"]))
    conn.commit()
    conn.close()
    return delayed_response({"message": "Item added", "status": 200})

@app.route("/remove-item", methods=["POST"])
def remove_item():
    data = request.json
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE name = ?", (data["name"],))
    conn.commit()
    conn.close()
    return delayed_response({"message": "Item removed", "status": 200})

@app.route("/update-quantity", methods=["POST"])
def update_quantity():
    data = request.json
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET quantity = ? WHERE name = ?", (data["quantity"], data["name"]))
    conn.commit()
    conn.close()
    return delayed_response({"message": "Quantity updated", "status": 200})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
