import random

def getCards():
    suits = [u"Hearts \u2665", u"Diamonds \u2666", u"Clubs \u2663", u"Spades \u2660"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck


def getBlackjackCards():
    suits = [u"Hearts \u2665", u"Diamonds \u2666", u"Clubs \u2663", u"Spades \u2660"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def Shuffle(deck):
    random.shuffle(deck)
    return deck
def setupCards(playerCards, cards):
    playerCards.append(cards.pop(0))
    playerCards.append(cards.pop(0))
def calculateValue(cards):
    newSum = sum(i for i, j in cards)
    if newSum > 21:
        newSum = 0
        for i, j in cards:
            if i == 11:
                newSum += 1
            else:
                newSum += i
    return newSum