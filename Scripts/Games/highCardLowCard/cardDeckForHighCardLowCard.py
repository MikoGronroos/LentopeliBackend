import random

def getCards():
    suits = [u"Hearts \u2665", u"Diamonds \u2666", u"Clubs \u2663", u"Spades \u2660"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def Shuffle(deck):
    random.shuffle(deck)
    return deck