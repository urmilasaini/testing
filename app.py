from datetime import datetime

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

messages = []


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/messages")
def get_messages():
    return jsonify(messages)


@app.post("/messages")
def add_message():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "Guest").strip()[:32]
    text = (data.get("text") or "").strip()

    if not text:
        return jsonify({"error": "Message text is required."}), 400

    message = {
        "name": name or "Guest",
        "text": text[:500],
        "time": datetime.now().strftime("%H:%M"),
    }
    messages.append(message)

    return jsonify(message), 201


if __name__ == "__main__":
    app.run(debug=True)
