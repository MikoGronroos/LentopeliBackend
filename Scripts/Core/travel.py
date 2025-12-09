import Scripts.Database.database as db
import Scripts.Core.account as account
import random
from flask import Blueprint, request, jsonify

travel = Blueprint('travel', __name__)

@travel.route('/getAirports', methods=['GET'])
def getAirports():
    codes =  db.GetAllPossibleAirports(account.getGameId())
    newList = []
    for code in codes:
        newList.append(db.GetAirport(code[1]))
    return jsonify({"airports": newList})

@travel.route('/getIsCurrentAirport', methods=['GET'])
def getIsCurrentAirport():
    value = db.GetCurrentPlayerAirport(account.getGameId())
    return jsonify({"airport": value})

@travel.route('/getCurrentContinent', methods=['GET'])
def getCurrentContinent():
    print(db.getPlayerContinent(account.name))
    return jsonify({"status": "okay"})

def getNewAirports():
    airports = db.takeAllAirports()
    db.DeletePossibleAirports(account.getGameId())
    for airport in airports:
        db.AddPossibleAirport(account.getGameId(), airport[4])

def getStartingAirport():
    codes =  db.GetAllPossibleAirports(account.getGameId())
    code = codes[random.randint(0, len(codes) - 1)];
    return code[1]

@travel.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    status = "noMoneyForFlight"
    if db.HasMoney(account.name) == True:
        if db.CheckMoney(account.name, 30):
            db.fly(data['icao'], account.name)
            db.UpdateMoney(account.getGameId(), -30)
            status = "flightHasBeenCompleted"
    
    return jsonify({"status": status})

