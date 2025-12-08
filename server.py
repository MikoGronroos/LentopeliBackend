from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
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
        game_id = db.getGameId(name)

        if db.alreadyHasPostcard(game_id, item_continent):
            return jsonify({"success": False, "message": "Already owned"})

        postcard_id = db.getPostcardId(item_continent)
        db.collect_postcard(game_id, postcard_id)
        db.UpdateMoney(name, -price)

        if db.playerHasAllPostcards(game_id):
            return jsonify({
                "success": True,
                "message": "You bought a postcard! You WIN!",
                "win": True
            })

        return jsonify({
            "success": True,
            "message": "Postcard bought!",
            "win": False
        })

    if item_type == "voucher":
        db.UpdateMoney(name, -price)
        return jsonify({
            "success": True,
            "message": "Voucher purchased!",
            "win": False
        })

    return jsonify({"success": False, "message": "Unknown item type"})

app = Flask(__name__)
CORS(app)

app.register_blueprint(shop)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
