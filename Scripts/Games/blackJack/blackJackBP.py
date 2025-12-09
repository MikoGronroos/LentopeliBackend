from Scripts.Games.blackJack import cardDeckforBlackJack as deck
from flask import Blueprint, request
import Scripts.Core.gambleStorage as storage

blackJackBP = Blueprint("blackJack",__name__,url_prefix="/games/blackJack")

#Here comes the starting values like player's and dealer's cards
@blackJackBP.route('/setup')
def setupGame():
    moneyToGamble = int(storage.moneyInStorage)
    moneyWon = 1
    cards = deck.getBlackjackCards()
    cards = deck.Shuffle(cards)

    playerCards = []
    deck.setupCards(playerCards, cards)

    dealerCards = []
    deck.setupCards(dealerCards, cards)

    state = 0
    playerValue = deck.calculateValue(playerCards)
    dealerValue = deck.calculateValue(dealerCards)

    if playerValue == 21:
        state = 3
        moneyWon = moneyToGamble * 3

    response = {

    "playerCardsjson": playerCards,
    "playerValuejson": playerValue,
    "dealerCardsjson": dealerCards,
    "dealerValuejson": dealerValue,
    "cardsjson": cards,
    "statejson": state,
    "moneyToGamblejson": moneyToGamble,
    "moneyWonjson": moneyWon

    }

    return response

#Here it appends cards to dealer's hand according to the rules when you choose to stand
@blackJackBP.route('/stand', methods=['POST'])

def stand():
    data = request.get_json()
    dealerCards = data['dealerCards']
    playerCards = data['playerCards']
    cards = data['cards']
    state = data['state']
    playerValue = data['playerValue']
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']

    howManyDealerCards = 1


    #This if statement is here so that if you get a blackjack on the first hand,
    #you can't get a draw if the dealer also gets a blackjack
    if state != 3:

        while True:
            dealerSum = deck.calculateValue(dealerCards)
            if dealerSum <= 16:
                dealerCards.append(cards.pop(0))
                howManyDealerCards += 1
            elif dealerSum >= 17 and dealerSum <= 21:
                if deck.calculateValue(dealerCards) > deck.calculateValue(playerCards):
                    state = -1
                    moneyWon = -moneyToGamble
                elif deck.calculateValue(dealerCards) == deck.calculateValue(playerCards):
                    state = 2
                    moneyWon = moneyToGamble
                elif deck.calculateValue(dealerCards) < deck.calculateValue(playerCards):
                    state = 1
                    moneyWon = moneyToGamble * 3
                break
            elif dealerSum > 21:
                state = 1
                moneyWon = moneyToGamble * 3
                break

    dealerValue = deck.calculateValue(dealerCards)
    response = {
        "playerCardsjson": playerCards,
        "playerValuejson": playerValue,
        "dealerCardsjson": dealerCards,
        "dealerValuejson": dealerValue,
        "cardsjson": cards,
        "statejson": state,
        "moneyToGamblejson": moneyToGamble,
        "moneyWonjson": moneyWon,
        "howManyDealerCardsjson": howManyDealerCards
    }

    return response

#Here it appends cards to your hand when you choose to hit
@blackJackBP.route('/hit', methods=['POST'])

def hit():
    data = request.get_json()
    dealerCards = data['dealerCards']
    playerCards = data['playerCards']
    cards = data['cards']
    state = data['state']
    dealerValue = data['dealerValue']
    moneyWon = data['moneyWon']
    moneyToGamble = data['moneyToGamble']

    playerCards.append(cards.pop(0))
    if deck.calculateValue(playerCards) > 21:
        state = -1
        moneyWon = -moneyToGamble
    elif deck.calculateValue(playerCards) == 21:
        state = 3
        moneyWon = moneyToGamble * 3

    playerValue = deck.calculateValue(playerCards)

    response = {
        "playerCardsjson": playerCards,
        "playerValuejson": playerValue,
        "dealerCardsjson": dealerCards,
        "dealerValuejson": dealerValue,
        "cardsjson": cards,
        "statejson": state,
        "moneyToGamblejson": moneyToGamble,
        "moneyWonjson": moneyWon
    }

    return response
