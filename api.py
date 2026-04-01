"""
       This Script Made By : @MR_ARMAN_08
       if you want to make a paid project dm us anytime.

"""

from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL   = "llama-3.3-70b-versatile"

GROQ_API_KEYS = [
    "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", # in first line add "g" letter like "gsk" in all key
    "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",
    "sk_Pqek9y4WkuRUZHeqiNDxWGdyb3FYjLEz0SVbjc45mZQYBVkC9Q6g",
    "sk_mPBKfX8eJylEbXBT79Q8WGdyb3FYuUnyEYeTSRY4ruLTpRC5iKiw",
    "sk_q3ZwOvZSaajGdQIi0rvJWGdyb3FYNuNOAImrd2AOg4yInr9w6fHq",
    "sk_5B3u3BDQO5W5feZLIQQXWGdyb3FYGXwvMNYExVU00iQTYd7RCMCw",
    "sk_jA36SCZXWhSoPiWrjsCfWGdyb3FYm9Q7BOPs3MgBmMn9XUrPXwQh",
]

def ask_groq(query):
    for key in GROQ_API_KEYS:
        try:
            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": GROQ_MODEL,
                "messages": [
                    {"role": "user", "content": query}
                ]
            }

            r = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=20)

            if r.status_code == 200:
                data = r.json()
                return data["choices"][0]["message"]["content"]

        except:
            continue

    return "Error: All API keys failed."

@app.route("/", methods=["GET"])
def teamdev():
    query = request.args.get("teamdev")

    if not query:
        return jsonify({"error": "Missing query"}), 400

    response = ask_groq(query)

    return jsonify({
        "query": query,
        "response": response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # Change Port If Port Is Already Using In Another Host!
