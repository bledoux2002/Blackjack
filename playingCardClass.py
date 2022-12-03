# playingCardClass.py, created by Benjamin Ledoux
# This creates a class for each playing card

class PlayingCard():
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank

    def __str__(self):
        return self.suit + str(self.rank)
