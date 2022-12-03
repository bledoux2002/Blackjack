# deckClass.py, created by Benjamin Ledoux
# This creates a class for a deck of playing cards

from playingCardClass import *
from random import *

class Deck:
    def __init__(self):
        self.cardList = []
        for s in ["s", "c", "d", "h"]:
            for r in range(1, 14):
                self.cardList.append(PlayingCard(r, s))

    def shuffleDeck(self):
        shuffle(self.cardList)

    def dealCard(self):
        self.card = self.cardList[0]
        self.cardList.remove(self.cardList[0])
        return self.card
    
    def cardsLeft(self):
        return len(self.cardList)
