import Scripts.Database.database as db
import Scripts.Core.account as account
import random
from flask import Blueprint, request, jsonify

currency = Blueprint('money', __name__)

@currency.route('/getMoney', methods=['GET'])
def getMoney():
    value = db.GetCurrentMoney(account.getGameId())
    return jsonify({"money": value})

@currency.route('/hasMoney', methods=['GET'])
def hasMoney():
    value = db.HasMoney(account.name)
    newValue = "noMoney"
    if(value == True):
        newValue = "hasMoney"
    return jsonify({"HasMoney": newValue})
