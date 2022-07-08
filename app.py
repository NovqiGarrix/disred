from flask import Flask, request, jsonify
from utils import DiSred

import sys

app = Flask(__name__)

# http://localhost:9090?dbname=nama_database

# { dbname: "nama_database" }

@app.route("/", methods=["GET"])
def root():
    return jsonify("OK")

@app.route("/<dbname>/", methods=["GET"])
def getAll(dbname: str):
    db = DiSred.DiSred(dbname)
    return jsonify({ "error": None, "data": db.get_all() })

@app.route("/<dbname>/one", methods=["POST"])
def get(dbname: str):
    requestBody = request.get_json(force=True)
    if "key" not in requestBody:
        return jsonify({ "error": "Invalid Key atau Key nya tidak ada.", "data": None })

    key = requestBody["key"]
    db = DiSred.DiSred(dbname)
    return jsonify({ "error": None, "data": db.get(key) })

@app.route("/<dbname>/keys", methods=["GET"])
def get_keys(dbname: str):
    db = DiSred.DiSred(dbname)
    return jsonify({ "error": None, "data": db.get_keys() })

@app.route("/<dbname>/", methods=["POST"])
def insert(dbname: str):
    db = DiSred.DiSred(dbname)
    if "key" not in request.get_json(force=True):
        return jsonify({ "error": "Masukkan key di request body", "data": None })
    
    if "value" not in request.get_json(force=True):
        return jsonify({ "error": "Masukkan value di request body", "data": None })

    key = request.get_json(force=True)["key"]
    value = request.get_json(force=True)["value"]
    return jsonify({ "error": None, "data": db.insert(key, value) })

@app.route("/<dbname>/<key>", methods=["DELETE"])
def delete(dbname: str, key: str):
    db = DiSred.DiSred(dbname)
    return jsonify({ "error": None, "data": db.delete(key) })

@app.route("/<dbname>/", methods=["DELETE"])
def flush(dbname: str):
    db = DiSred.DiSred(dbname)
    return jsonify({ "error": None, "data": db.flush() })


app.run(host="localhost", port=9090, debug=True)