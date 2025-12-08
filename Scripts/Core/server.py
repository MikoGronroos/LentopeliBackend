from flask import Flask, request, jsonify, Blueprint
import Scripts.Database.database as db
import Scripts.Core.account as account

shop = Blueprint('shop', __name__)

@shop.post("/buy")
def buy_item():
    data = request.json
    item_type = data["type"]
    item_continent = data.get("continent")
    price = data["price"]
    name = account.name


    if not db.CheckMoney(name, price):
        return jsonify({"success": False, "message": "Not enough coins"})


    if item_type == "postcard":
        if db.alreadyHasPostcard(db.getGameId(name), item_continent):
            return jsonify({"success": False, "message": "Already owned"})

        card_id = db.getPostcardId(item_continent)
        db.collect_postcard(db.getGameId(name), card_id)
        db.UpdateMoney(name, -price)

        if db.playerHasAllPostcards(db.getGameId(name)):
            return jsonify({"success": True, "message": "You bought a postcard! You WIN!"})

        return jsonify({"success": True, "message": "Postcard bought!"})


    if item_type == "voucher":
        db.UpdateMoney(name, -price)

        return jsonify({"success": True, "message": "Voucher purchased!"})

    return jsonify({"success": False, "message": "Unknown item type"})
