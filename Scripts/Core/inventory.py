import Scripts.Database.database as db
import Scripts.Core.account as account
import os
from flask import Blueprint, request, jsonify

inventory = Blueprint('inventory', __name__)

@inventory.route("/getInventory", methods=['GET'])
def getAllCards():
    cards = db.show_collected_postcards(account.getGameId())
    return jsonify({"cards": cards})

@inventory.route("/getAllPostcards", methods=['GET'])
def getAllPostcards():
    cards = db.getAllPostcards()
    return jsonify({"cards": cards})

@inventory.route("/hasPostcard", methods=['POST'])
def hasPostcard():
    data = request.get_json()
    value = db.alreadyHasPostcard(account.getGameId(), data['postcard'][2]);
    print(value)
    if(value):
        return jsonify({"has": "true"})
    else:
        return jsonify({"has": "false"})
