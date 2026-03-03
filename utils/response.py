from flask import jsonify


def success(data, message, status=200):
    return jsonify({"status": 200, "message": message, "data": data}), status


def error(message, status):
    return jsonify({"status": status, "message": message}), status
