from flask import Flask, request, redirect, jsonify
import string, random

app = Flask(__name__)

# In-memory storage
url_store = {}

def generate_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/")
def home():
    return "URL Shortener Running"

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.json["url"]
    short_id = generate_short()

    url_store[short_id] = long_url

    return jsonify({"short_url": f"http://localhost:5000/{short_id}"})

@app.route("/<short_id>")
def redirect_url(short_id):
    if short_id in url_store:
        return redirect(url_store[short_id])
    return "URL not found", 404

app.run(host="0.0.0.0", port=5000)