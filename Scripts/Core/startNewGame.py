import Scripts.Database.database as db
import Scripts.Core.account as account
import Scripts.Core.travel as travel
import random

def startNewGame():
    travel.getNewAirports()
    code = travel.getStartingAirport()
    account.airport = code
    db.newPlayerCreated(account.airport, account.name)
    return "Account created"

