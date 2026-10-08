import json, os
from pathlib import Path
from flask import Flask, render_template, jsonify

BASE = Path(__file__).parent
app = Flask(__name__)

def load():
    with open(BASE / "portfolio.json", encoding="utf-8") as f:
        return json.load(f)

@app.after_request
def headers(r):
    r.headers["X-Content-Type-Options"] = "nosniff"
    r.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return r

@app.route("/")
def index():
    return render_template("index.html", data=load())

@app.route("/api/profile")
def api_profile():
    return jsonify(load())

@app.route("/healthz")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=os.environ.get("FLASK_DEBUG") == "1")
