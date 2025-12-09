from flask import Blueprint, jsonify, request

moneyInStorage = 0

storage = Blueprint("storage",__name__)

@storage.route("/addMoney", methods=['POST'])
def AddMoney():
    data = request.get_json()
    money = data['money']
    moneyInStorage = money
    return jsonify({"status": "added"})


@storage.route("/getMoney", methods=['GET'])
def GetMoney():
    return jsonify({"money": moneyInStorage})

