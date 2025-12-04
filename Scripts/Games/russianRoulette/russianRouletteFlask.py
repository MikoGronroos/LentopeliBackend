from flask import Flask, request
import random
from flask_cors import CORS

russianRoulette = Flask(__name__)
CORS(russianRoulette, origins=["http://localhost:63342"])

#Here the program rolls the bullet's spot
@russianRoulette.route('/games/russianRoulette/getbullet')

def rollBullet():
    bullet = random.randint(1, 6)
    player = 1

    response = {

    "bulletjson": bullet,
    "playerjson": player

    }

    return response

#Here it checks whether your shot or stood. Also it checks if you die if you shot
@russianRoulette.route('/games/russianRoulette/shootorstand', methods=['POST'])

def shoot():
    data = request.get_json()
    choice = data['shootOrStand']
    bullet = int(data['bullet'])
    player = int(data['player'])

    if choice == "shoot":
        if bullet == player:
            winOrLost = "lose"
        else:
            player += 1
            winOrLost = "win"
    else:
        winOrLost = "stand"


    print(player)
    response = {

        "winOrLostjson": winOrLost,
        "bulletjson": bullet,
        "playerjson": player

    }

    return response

if __name__ == '__main__':
    russianRoulette.run(use_reloader=True, host='127.0.0.1', port=3000)