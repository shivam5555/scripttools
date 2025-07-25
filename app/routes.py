from flask import Blueprint, jsonify
from . import utils

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return jsonify({"message": "Welcome to ScriptTools API"})

@main.route("/health")
def health():
    return jsonify({"status": "healthy"})

@main.route("/uptime")
def uptime():
    return jsonify({"uptime": utils.get_uptime()})
