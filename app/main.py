from flask import Flask, jsonify

VERSION = 'v1'

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/version")
def version():
    return jsonify({"status":"ok", "message": VERSION})

app.run(host='0.0.0.0', port=80)
