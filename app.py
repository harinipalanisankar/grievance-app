from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "success", "system": "Campus Grievance Management System", "message": "Grievance API is operational"})

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "service": "grievance-backend"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
