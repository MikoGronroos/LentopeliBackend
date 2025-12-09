from flask import Blueprint, request, jsonify
import random
import Scripts.Core.gambleStorage as storage
import Scripts.Core.account as account
import Scripts.Database.database as db

pokerLiteBP = Blueprint("pokerLite",__name__,url_prefix="/games/pokerLite")

#Here comes the starting values like playerCard, dealerCard and playerGuessedCorrectly
@pokerLiteBP.route('/getcards', methods=['GET'])
def getCards():
    pList = []

    for i in range(5):
        pList.append(random.randint(1,9))

    response = {

    "pListjson": pList

    }

    return jsonify(response)

#Here it checks whether your guess was correct or not
@pokerLiteBP.route('/checksum', methods=['POST'])

def checkSum():
    data = request.get_json()
    pList = data['pList']
    reRollCheck = data['reRollCheck']
    moneyToGamble = int(storage.GetGambleStorage())

    cList = []

    for i in range(5):
        cList.append(random.randint(1,9))

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

    db.UpdateMoney(account.getGameId(), moneyWon)

    response = {
        "pListjson": pList,
        "sumPListjson": sum(pList),
        "sumCListjson": sum(cList),
        "winOrLosejson": winOrLose,
        "moneyWonjson": moneyWon
    }

    return response
