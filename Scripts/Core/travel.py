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

def travel1():
    while True:
        if db.HasMoney(account.name) == False:
            print("You run out of money")
        airports = db.takeAllAirports(db.getPlayerContinent(account.name))
        print(f"You have {db.GetPlayerMoney(account.name)} coins")
        print(f"A ticket costs 30 coins")
        i = 0
        for value in airports:
            i = i + 1
            print(f"{i}, name: {value[0]} and continent: {value[3]}")
        selection = int(input("select airport 1-5 or exit 6: "))
        if selection < 6 and selection > 0:
            if db.CheckMoney(account.name, 30):
                db.fly(airports[selection - 1][4], account.name)
                db.UpdateMoney(account.name, -30)
            else:
                print("You do not have enough money to fly")
                input("Press enter to continue...")
        if selection == 6:
            return

