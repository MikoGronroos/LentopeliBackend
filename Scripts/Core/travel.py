import Scripts.Database.database as db
import Scripts.Core.account as account
from flask import Blueprint, request, jsonify

travel = Blueprint('travel', __name__)

@travel.route('/getAirports', methods=['GET'])
def getAirports():
    codes =  db.GetAllPossibleAirports(account.getGameId())
    newList = []
    for code in codes:
        newList.append(db.GetAirport(code[1]))
    return jsonify({"airports": newList})

def getNewAirports():
    airports = db.takeAllAirports(db.getPlayerContinent(account.name))
    db.DeletePossibleAirports(account.getGameId())
    for airport in airports:
        db.AddPossibleAirport(account.getGameId(), airport[4])

@travel.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    status = "noMoneyForFlight"
    if db.HasMoney(account.name) == True:
        if db.CheckMoney(account.name, 30):
            db.fly(data['icao'], account.name)
            db.UpdateMoney(account.name, -30)
            getNewAirports()
            status = "flightHasBeenCompleted"
    
    return jsonify({"status": status})

