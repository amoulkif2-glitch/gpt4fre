import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))

@app.route("/v1/chat/completions", methods=["POST"])
def proxy():
    data = request.json
    headers = {"Authorization": "Bearer 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"}
    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
