from flask import Flask, request
import random
from flask_cors import CORS

dicegame = Flask(__name__)
CORS(dicegame, origins=["http://localhost:63342"])

#Here comes all the starting variables like sum of the dice and the revealed dice
@dicegame.route('/games/dicegame/getnumbers')

def rollNumbers():
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

    }

    return response

#Here it checks whether your guess was too high or too low or correct
@dicegame.route('/games/dicegame/highlow', methods=['POST'])

def isItHigherOrLower():
    data = request.get_json()
    guess = int(data['guess'])
    guessTracker = int(data['guessTracker'])
    diceSum = int(data['diceSum'])
    revealedDice = int(data['revealedDice'])
    highLow = ""
    if guess == diceSum:
        highLow = "win"
    elif guessTracker == 3:
        highLow = "lose"
    elif guess < diceSum:
        highLow =  "low"
    elif guess > diceSum:
        highLow = "high"

    response = {

        "highLowjson": highLow,
        "diceSumjson": diceSum,
        "revealedDicejson": revealedDice,
        "guessTrackerjson": guessTracker

    }

    return response

if __name__ == '__main__':
    dicegame.run(use_reloader=True, host='127.0.0.1', port=3000)
