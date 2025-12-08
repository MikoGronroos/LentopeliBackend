import Scripts.Database.database as db
import Scripts.Core.account as account
import random
from flask import Blueprint, request, jsonify

currency = Blueprint('money', __name__)

@currency.route('/getMoney', methods=['GET'])
def getMoney():
    value = db.GetCurrentMoney(account.getGameId())[0][0]
    return jsonify({"money": value})
