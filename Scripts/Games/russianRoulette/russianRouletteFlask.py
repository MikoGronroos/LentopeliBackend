from flask import Flask, request
import random
from flask_cors import CORS

russianRoulette = Flask(__name__)
CORS(russianRoulette, origins=["http://localhost:63342"])

#Here the program rolls the bullet's spot
@russianRoulette.route('/games/russianRoulette/getbullet/<moneyToGamble>')

def rollBullet(moneyToGamble):
    moneyToGamble = int(moneyToGamble)
    moneyWon = -moneyToGamble
    bullet = random.randint(1, 6)
    player = 1

    response = {

    "bulletjson": bullet,
    "playerjson": player,
    "moneyToGamblejson": moneyToGamble,
    "moneyWonjson": moneyWon

    }

    return response

#Here it checks whether your shot or stood. Also it checks if you die if you decided to shoot
@russianRoulette.route('/games/russianRoulette/shootorstand', methods=['POST'])

def shoot():
    data = request.get_json()
    choice = data['shootOrStand']
    bullet = int(data['bullet'])
    player = int(data['player'])
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']

    if choice == "shoot":
        if bullet == player:
            winOrLost = "lose"
            moneyWon = -moneyToGamble
        else:
            if player == 1:
                moneyWon = moneyToGamble
            elif player == 2:
                moneyWon = moneyToGamble + moneyToGamble//2
            elif player == 3:
                moneyWon = moneyToGamble*3
            elif player == 4:
                moneyWon = moneyToGamble*5
            else:
                moneyWon = moneyToGamble*7
            player += 1
            winOrLost = "win"


    else:
        winOrLost = "stand"


    print(player)
    response = {

        "winOrLostjson": winOrLost,
        "bulletjson": bullet,
        "playerjson": player,
        "moneyWonjson": moneyWon

    }

    return response

if __name__ == '__main__':
    russianRoulette.run(use_reloader=True, host='127.0.0.1', port=3000)