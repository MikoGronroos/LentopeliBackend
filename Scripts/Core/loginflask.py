from flask import Flask, request, jsonify, Blueprint
from Scripts.Core.loginhelper import tryLogin, tryRegister
import Scripts.Core.account as account


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if tryLogin(username, password):
        account.name = username
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Wrong username or password."})

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    if tryRegister(username, password):
        account.name = username
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Username already exists."})
    
