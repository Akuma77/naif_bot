import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Naif Bot is running!"

@app.route("/interactions", methods=["POST"])
def interactions():
    return jsonify({"type": 1})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
