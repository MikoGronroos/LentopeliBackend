from flask import Flask, request
from flask_cors import CORS
import random

pokerLite = Flask(__name__)
CORS(pokerLite, origins=["http://localhost:63342"])

#Here comes the starting values like playerCard, dealerCard and playerGuessedCorrectly
@pokerLite.route('/games/pokerLite/getcards/<moneyToGamble>')

def getCards(moneyToGamble):

    moneyToGamble = int(moneyToGamble)
    moneyWon = 1
    pList = []

    for i in range(5):
        pList.append(random.randint(1,9))

    response = {

    "pListjson": pList,
    "moneyToGamblejson": moneyToGamble,
    "moneyWonjson": moneyWon

    }

    return response

#Here it checks whether your guess was correct or not
@pokerLite.route('/games/pokerLite/checksum', methods=['POST'])

def checkSum():
    data = request.get_json()
    pList = data['pList']
    reRollCheck = data['reRollCheck']
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']

    cList = []

    for i in range(5):
        cList.append(random.randint(3,9))

        if reRollCheck[i] == 1:
            pList[i] = random.randint(1,9)

    if sum(pList) > sum(cList):
        winOrLose = "win"
        moneyWon = moneyToGamble * 3
    elif sum(pList) == sum(cList):
        winOrLose = "draw"
        moneyWon = moneyToGamble
    else:
        winOrLose = "lose"
        moneyWon = -moneyToGamble

    response = {
        "pListjson": pList,
        "sumPListjson": sum(pList),
        "sumCListjson": sum(cList),
        "winOrLosejson": winOrLose,
        "moneyToGamblejson": moneyToGamble,
        "moneyWonjson": moneyWon
    }

    return response

if __name__ == '__main__':
    pokerLite.run(use_reloader=True, host='127.0.0.1', port=3000)