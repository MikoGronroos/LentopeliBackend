from flask import Blueprint, request
from flask_cors import CORS
import random

pokerLiteBP = Blueprint("pokerLite",__name__,url_prefix="/games/pokerLite")
CORS(pokerLiteBP, origins=["http://localhost:63342"])

#Here comes the starting values like playerCard, dealerCard and playerGuessedCorrectly
@pokerLiteBP.route('/getcards/<moneyToGamble>')

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
@pokerLiteBP.route('/checksum', methods=['POST'])

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