import Scripts.Database.database as db
import Scripts.Core.account as account
import random
from flask import Blueprint

startGame = Blueprint('startGame', __name__)

@startGame.route('/startNewGame')
def startNewGame():
    continentList = ["EU", "AS", "NA", "SA", "AF", "OC"]
    startingContinent = continentList[random.randint(0, len(continentList) - 1)]
    startingAirport = db.getRandomAirportCode(startingContinent)
    account.continent = startingContinent
    account.airport = startingAirport
    db.newPlayerCreated(account.airport, account.name)
    return "Account created"
