from flask import Flask, request, jsonify
from utils import DiSred

import sys

app = Flask(__name__)

# http://localhost:9090?dbname=nama_database

# { dbname: "nama_database" }

@app.route("/", methods=["GET"])
def getAll():
    requestParams = request.args
    if requestParams == None:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    if "dbname" not in requestParams:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    nama_database = requestParams["dbname"]
    db = DiSred.DiSred(nama_database)
    return jsonify({ "error": None, "data": db.get_all() })

@app.route("/<key>/one", methods=["GET"])
def get(key: str):
    requestParams = request.args
    if requestParams == None:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    if "dbname" not in requestParams:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    nama_database = requestParams["dbname"]
    db = DiSred.DiSred(nama_database)

    return jsonify({ "error": None, "data": db.get(key) })

@app.route("/keys", methods=["GET"])
def get_keys():
    requestParams = request.args
    if requestParams == None:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    if "dbname" not in requestParams:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    nama_database = requestParams["dbname"]
    db = DiSred.DiSred(nama_database)

    return jsonify({ "error": None, "data": db.get_keys() })

@app.route("/", methods=["POST"])
def insert():
    requestParams = request.args
    if requestParams == None:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    if "dbname" not in requestParams:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    nama_database = requestParams["dbname"]
    db = DiSred.DiSred(nama_database)

    if "key" not in request.get_json(force=True):
        return jsonify({ "error": "Masukkan key di request body", "data": None })
    
    if "value" not in request.get_json(force=True):
        return jsonify({ "error": "Masukkan value di request body", "data": None })

    key = request.get_json(force=True)["key"]
    value = request.get_json(force=True)["value"]
    return jsonify({ "error": None, "data": db.insert(key, value) })

@app.route("/<key>", methods=["DELETE"])
def delete(key):
    requestParams = request.args
    if requestParams == None:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    if "dbname" not in requestParams:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    nama_database = requestParams["dbname"]
    db = DiSred.DiSred(nama_database)

    return jsonify({ "error": None, "data": db.delete(key) })

@app.route("/", methods=["DELETE"])
def flush():
    requestParams = request.args
    if requestParams == None:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    if "dbname" not in requestParams:
        return jsonify({ "error": "Nama database tidak ada", "data": None })

    nama_database = requestParams["dbname"]
    db = DiSred.DiSred(nama_database)

    return jsonify({ "error": None, "data": db.flush() })


app.run(host="localhost", port=9090, debug=True)