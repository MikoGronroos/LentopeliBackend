from highCardLowCard import cardDeckForHighCardLowCard as deck
from flask import Blueprint, request
from flask_cors import CORS

highCardLowCardBP = Blueprint("highCardLowCard",__name__,url_prefix="/games/highCardLowCard")
CORS(highCardLowCardBP, origins=["http://localhost:63342"])

#Here comes the starting values like playerCard, dealerCard and playerGuessedCorrectly
@highCardLowCardBP.route('/getcards/<moneyToGamble>')

def getCards(moneyToGamble):
    moneyToGamble = int(moneyToGamble)
    moneyWon = 1
    cards = deck.getCards()
    cards = deck.Shuffle(cards)
    playerCard = cards.pop(0)
    dealerCard = cards.pop(0)
    highLow = ""

    response = {

    "playerCardjson": playerCard,
    "dealerCardjson": dealerCard,
    "highLow": highLow,
    "moneyToGamblejson": moneyToGamble,
    "moneyWonjson": moneyWon

    }

    return response

#Here it checks whether your guess was correct or not
@highCardLowCardBP.route('/highlow', methods=['POST'])

def isItHigherOrLower():
    data = request.get_json()
    guess = data['guess']
    playerCard = data['playerCard']
    dealerCard = data['dealerCard']
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']
    if playerCard[0] == dealerCard[0] and guess == "same":
        highLow = "same"
        moneyWon = moneyToGamble * 10
    elif playerCard[0] < dealerCard[0] and guess == "lower" :
        highLow =  "win"
        moneyWon = moneyToGamble * 2
    elif playerCard[0] > dealerCard[0] and guess == "higher":
        highLow = "win"
        moneyWon = moneyToGamble * 2
    else:
        highLow = "lose"
        moneyWon = -moneyToGamble

    response = {
        "highLowjson": highLow,
        "moneyWonjson": moneyWon
    }

    return response