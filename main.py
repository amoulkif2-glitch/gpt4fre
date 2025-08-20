import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))
OPENAI_KEY = os.environ.get("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")  # plus sûr que mettre la clé en dur

@app.route("/v1/chat/completions", methods=["POST"])
def proxy():
    data = request.json
    headers = {"Authorization": f"Bearer {OPENAI_KEY}"}
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            json=data,
            headers=headers,
            timeout=20  # limite la durée d'attente
        )
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
