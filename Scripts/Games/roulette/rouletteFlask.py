from flask import Flask, request
import random
from flask_cors import CORS

roulette = Flask(__name__)
CORS(roulette, origins=["http://localhost:63342"])

#Here comes the correct number
@roulette.route('/games/roulette/getnumbers/<moneyToGamble>')

def rollNumbers(moneyToGamble):
    moneyToGamble = int(moneyToGamble)
    moneyWon = 1
    nmb = random.randint(1,12)

    response = {

    "nmbjson": nmb,
    "moneyToGamblejson": moneyToGamble,
    "moneyWonjson": moneyWon

    }

    return response

#Here it checks whether your guess was correct
@roulette.route('/games/roulette/numbercheck', methods=['POST'])

def numberCheck():
    data = request.get_json()
    guess = int(data['guess'])
    nmb = int(data['nmb'])
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']

    odd = [1, 3, 5, 7, 9, 11]
    even = [2, 4, 6, 8, 10, 12]

    if guess == nmb:
        winOrLose = "exact"
        moneyWon = moneyToGamble * 4
    else:
        if guess in odd and nmb in odd:
            winOrLose = "odd"
            moneyWon = moneyToGamble // 2
        elif guess in even and nmb in even:
            winOrLose = "even"
            moneyWon = moneyToGamble // 2
        else:
            winOrLose = "lose"
            moneyWon = - moneyToGamble


    response = {

        "winOrLosejson": winOrLose,
        "nmbjson": nmb,
        "moneyWonjson": moneyWon
    }

    return response

if __name__ == '__main__':
    roulette.run(use_reloader=True, host='127.0.0.1', port=3000)