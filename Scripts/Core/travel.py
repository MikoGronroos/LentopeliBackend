import Scripts.Database.database as db
import Scripts.Core.account as account
from flask import Blueprint, request, jsonify

travel = Blueprint('travel', __name__)

@travel.route('/getNewAirports')
def getNewAiports():
    airports = db.takeAllAirports(db.getPlayerContinent(account.name))
    db.DeletePossibleAirports(account.getGameId())
    return airports

@travel.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    status = "noMoneyForFlight"
    if db.HasMoney(account.name) == True:
        if db.CheckMoney(account.name, 30):
            db.fly(data['icao'], account.name)
            db.UpdateMoney(account.name, -30)
            status = "flightHasBeenCompleted"
    
    return jsonify({"status": status})

