from flask import Blueprint, request
import random
from flask_cors import CORS

dicegameBP = Blueprint("dicegame",__name__,url_prefix="/games/dicegame")
CORS(dicegameBP, origins=["http://localhost:63342"])

#Here comes all the starting variables like sum of the dice and the revealed dice
@dicegameBP.route('/getnumbers/<moneyToGamble>')

def rollNumbers(moneyToGamble):
    moneyToGamble = int(moneyToGamble)
    moneyWon = 1
    dicelist = []
    diceSum = 0
    for i in range(3):
        dice = random.randint(1, 6)
        dicelist.append(dice)
        diceSum += dice

    revealedDice = dicelist[0]

    response = {

    "dicelistjson": dicelist,
    "diceSumjson": diceSum,
    "revealedDicejson": revealedDice,
    "moneyToGamblejson": moneyToGamble,
    "moneyWonjson": moneyWon

    }

    return response

#Here it checks whether your guess was too high or too low or correct
@dicegameBP.route('/highlow', methods=['POST'])

def isItHigherOrLower():
    data = request.get_json()
    guess = int(data['guess'])
    guessTracker = int(data['guessTracker'])
    diceSum = int(data['diceSum'])
    revealedDice = int(data['revealedDice'])
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']
    highLow = ""
    if guess == diceSum:
        highLow = "win"
        moneyWon = moneyToGamble * 2
    elif guessTracker == 3:
        highLow = "lose"
        moneyWon = -moneyToGamble
    elif guess < diceSum:
        highLow =  "low"
    elif guess > diceSum:
        highLow = "high"

    response = {

        "highLowjson": highLow,
        "diceSumjson": diceSum,
        "revealedDicejson": revealedDice,
        "guessTrackerjson": guessTracker,
        "moneyToGamblejson": moneyToGamble,
        "moneyWonjson": moneyWon

    }

    return response