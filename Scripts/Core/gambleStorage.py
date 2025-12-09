from flask import Blueprint, jsonify, request
import Scripts.Database.database as db
import Scripts.Core.account as account

storage = Blueprint("storage",__name__)

@storage.route("/addMoney", methods=['POST'])
def AddMoney():
    data = request.get_json()
    money = data['money']
    db.SetGambleStorage(account.getGameId(), money)
    return jsonify({"status": "added"})

def GetGambleStorage():
    return db.GetGambleStorage(account.getGameId())[0]
