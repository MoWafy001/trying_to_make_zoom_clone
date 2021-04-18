from flask import Flask, request, abort, jsonify

app = Flask(__name__)



msgs = {}

#routes
@app.route("/send", methods=["POST"])
def send():
    id = request.json.get("id", None)
    msg = request.json.get("msg", None)

    if id is None or msg is None:
        abort(422)

    msgs[id] = msg
    
    return jsonify({"success": True})

@app.route("/receive", methods=["POST"])
def recieve():
    id = request.json.get("id", None)

    if id is None:
        abort(422)

    if id not in msgs:
        return jsonify({"messages": ""})

    return jsonify({"messages": msgs[id]})

@app.route("/")
def index():
    with open("public/index.html",'r') as f:
        return f.read()
