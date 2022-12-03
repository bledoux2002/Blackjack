# Blackjack.py, by Benjamin Ledoux, Andrea Mello
# The purpose of this program is to simulate a game of Blackjack between a player and a computer-controlled dealer.

from graphics import *
from deckClass import *
from buttonClass import *
import time
"""
graphics is used to display the game
deckClass makes a deck of cards from the playingCardClass module
buttonClass makes fully functional buttons for the UI
time is used to slow the game down to simulate real life, for a more pleasing presentation
"""

# Creates a class that simulates a game of Blackjack
class Blackjack:

    # Initializes the variables and lists, creates a new deck of cards from deckclass.py, and uses its .shuffleDeck() method to shuffle it.
    # dealerHand and playerHand will hold the cards of each hand from playingcardclass.py, while dHandImg and pHandImg will hold the associated images.
    # playingDeck will hold the deck of cards from deckclass.py used for this instance of the game.
    def __init__(self, dealerHand, playerHand):

        # Lists for cards
        self.dealerHand = dealerHand
        self.playerHand = playerHand

        # Images for cards
        self.dHandImg = []
        self.pHandImg = []

        # Create and shuffle new deck of cards
        self.playingDeck = Deck()
        self.playingDeck.shuffleDeck()


    # This method uses the deckclass.py .dealCard() method to deal two cards each to the dealer and player, adding them to the instance lists for the hands.
    # It then finds the associated image in the playingcards folder and displays them in a GraphWin, adding them to the image lists.
    # It takes inputted x and y coordinates for the location on the GraphWin the card images will show up in.
    def initDeal(self, gwin, xposD, yposD, xposP, yposP):

        for i in range(2):

            # Add new card to each hand
            self.dealerHand.append(self.playingDeck.dealCard())
            self.playerHand.append(self.playingDeck.dealCard())

            # Add corresponding image to game board
            self.dHandImg.append(Image(Point(xposD + (75 * i), yposD), "playingcards/" + self.dealerHand[i].__str__() + ".gif"))
            self.pHandImg.append(Image(Point(xposP + (75 * i), yposP), "playingcards/" + self.playerHand[i].__str__() + ".gif"))

            self.dHandImg[i].draw(gwin)
            self.pHandImg[i].draw(gwin)


    # Add a card from playingDeck to playerHand
    def hit(self, gwin, xpos, ypos):

        self.playerHand.append(self.playingDeck.dealCard())
        self.pHandImg.append(Image(Point(xpos, ypos), "playingcards/" + self.playerHand[-1].__str__() + ".gif"))
        self.pHandImg[-1].draw(gwin)


    # Add up card value of a given hand, count face cards as 10 and aces as 11 until the hand goes over 21
    def evaluateHand(self, hand):

        self.hand = hand
        self.handTot = 0
        self.handAces = 0

        # goes through every card in hand, looking for an Ace
        for card in hand:

            # if the card is an Ace, handAces increments by 1, and handTot adds 10 to account for the extra 10 points an Ace accounts for
            if card.value() == 1:
                self.handAces = self.handAces + 1
                self.handTot = self.handTot + 10
            self.handTot = self.handTot + card.value()

            # while loop to decrease ace value(s) in hand until tot < 21 or all aces have been adjusted.
            while self.handTot > 21 and self.handAces > 0:
                self.handTot = self.handTot - 10
                self.handAces = self.handAces - 1

        return self.handTot


    # Using the predefined rules of a dealer in Blackjack, an automated system is set up to simulate their turn
    def dealerPlays(self, gwin, xpos, ypos, label):

        # label is used to update the total value seen next to the visible dealer's hand
        self.label = label

        # while the dealer's hand totals less than 17, they will continue to draw cards
        while self.evaluateHand(self.dealerHand) < 17:

            # spaces out the deals for smoother presentation
            time.sleep(0.75)

            # same functionality at .hit()
            self.dealerHand.append(self.playingDeck.dealCard())
            self.dHandImg.append(Image(Point((xpos + (75 * (len(self.dealerHand) - 1))), ypos), "playingcards/" + self.dealerHand[-1].__str__() + ".gif"))
            self.dHandImg[-1].draw(gwin)

            # changes label to reflect the new value of the dealer's hand
            self.label.setText("Dealer\nTotal: " + str(self.evaluateHand(self.dealerHand)))


def main():

    # Create GraphWin for game
    myWin = GraphWin("Blackjack Simulator", 600, 600)
    myWin.setBackground('darkgreen')

    # Initialize buttons
    hitBtn = Button(myWin, Point(150, 300), 125, 50, "Hit")
    standBtn = Button(myWin, Point(450, 300), 125, 50, "Stand")
    resetBtn = Button(myWin, Point(300, 550), 125, 50, "Reset Board")
    newBtn = Button(myWin, Point(100, 550), 125, 50, "New Game")
    quitBtn = Button(myWin, Point(500, 550), 125, 50, "Quit")

    # Adjusts UI to only show necessary buttons
    hitBtn.deactivate()
    standBtn.deactivate()
    resetBtn.deactivate()
    newBtn.activate()
    quitBtn.activate()

    # Initialize labels to show the total value of each visible card in either hand
    dTotLbl = Text(Point(75, 100), "Dealer")
    pTotLbl = Text(Point(75, 450), "Player")
    resultLbl = Text(Point(300, 200), "Welcome to the Blackjack Simulator!\nPlease press 'New Game' to start.")

    resultLbl.setSize(20)

    dTotLbl.setFill('white')
    pTotLbl.setFill('white')
    resultLbl.setFill('white')

    dTotLbl.draw(myWin)
    pTotLbl.draw(myWin)
    resultLbl.draw(myWin)

    # Start the game
    pt = myWin.getMouse()

    # While quit button hasn't been clicked, check if other buttons have been clicked
    while quitBtn.clicked(pt) == False:

        # if new game button is clicked, sets up a new game of Blackjack
        if newBtn.clicked(pt) == True:

            # creates lists for use in BlackJack game, initializes Blackjack class under 'game'
            dHand = []
            pHand = []
            game = Blackjack(dHand, pHand)

            # hands out initial cards with .initDeal() method and updates value labels using .evaluateHand() method (doesn't reflect value of dealer's hidden card)
            game.initDeal(myWin, 150, 100, 150, 450)
            dTotLbl.setText("Dealer\nTotal: " + str(game.evaluateHand(game.dealerHand) - game.dealerHand[0].value()))
            pTotLbl.setText("Player\nTotal: " + str(game.evaluateHand(game.playerHand)))

            # covers first dealer card with face-down card
            firstDeal = Image(Point(150, 100), "playingcards/b1fv.gif")
            firstDeal.draw(myWin)

            # updates UI, hiding announcement label and activating play buttons, deactivating the new game button
            resultLbl.setFill('darkgreen')
            hitBtn.activate()
            standBtn.activate()
            resetBtn.activate()
            newBtn.deactivate()

        # if hit button is clicked (only possible if activated), deals player a new card as long as they haven't busted yet
        elif hitBtn.clicked(pt) == True:

            # .hit() method used to deal card and displays it according to the length of the hand
            game.hit(myWin, (150 + (75 * len(game.playerHand))), 450)

            # player total label updated with new total using .evaluateHand() method
            pTotLbl.setText("Player\nTotal: " + str(game.evaluateHand(game.playerHand)))

            # if the player busts, updates UI to reflect playern loss (can't use play buttons anymore, displays losing message w/ color)
            if game.evaluateHand(game.playerHand) > 21:

                # this undraws the face down card hiding the dealer's first card and updates the dealer's total label
                firstDeal.undraw()
                dTotLbl.setText("Dealer\nTotal: " + str(game.evaluateHand(game.dealerHand)))

                hitBtn.deactivate()
                standBtn.deactivate()
                resultLbl.setText("You busted!\nDealer wins.")
                resultLbl.setFill('red')

        # if stand button is clicked (only possible if activated), stops player from using play buttons and continues with simulating dealer hand
        elif standBtn.clicked(pt) == True:

            # deactivates play buttons
            hitBtn.deactivate()
            standBtn.deactivate()

            # reveals dealer's first card and updates dealer's total to reflect added card with .evaluateHand() method
            firstDeal.undraw()
            dTotLbl.setText("Dealer\nTotal: " + str(game.evaluateHand(game.dealerHand)))

            # simulation of dealer drawing cards using .dealerPlays() method
            game.dealerPlays(myWin, 150, 100, dTotLbl)

            # displays results according to final card count, who wins, loses, or even in case of a draw.
            if game.evaluateHand(game.dealerHand) > 21:
                resultLbl.setText("Dealer busted!\nYou win!")
                resultLbl.setFill('lightgreen')
            elif game.evaluateHand(game.dealerHand) < game.evaluateHand(game.playerHand):
                resultLbl.setText("Dealer hand is too low!\nYou win!")
                resultLbl.setFill('lightgreen')
            elif game.evaluateHand(game.dealerHand) == game.evaluateHand(game.playerHand):
                resultLbl.setText("Hands are the same.\nSplit Pot.")
                resultLbl.setFill('lightblue')
            elif game.evaluateHand(game.dealerHand) <= 21 and game.evaluateHand(game.dealerHand) > game.evaluateHand(game.playerHand):
                resultLbl.setText("Your hand is too low!\nDealer wins.")
                resultLbl.setFill('red')

        # if reset button is clicked, resets UI for new game
        elif resetBtn.clicked(pt) == True:

            # undraws any cards left on the board from previous game
            for image in game.dHandImg:
                image.undraw()
            for image in game.pHandImg:
                image.undraw()
            
            # firstDeal is undrawn here in case it wasn't before. 
            firstDeal.undraw()

            dTotLbl.setText("Dealer")
            pTotLbl.setText("Player")

            resultLbl.setText("Welcome to Blackjack!\nPlease press 'New Game' to start.")
            resultLbl.setFill('white')

            newBtn.activate()
            hitBtn.deactivate()
            standBtn.deactivate()
            resetBtn.deactivate()

        # this gets the next click for use in the while loop again
        pt = myWin.getMouse()

    # once the quit button is clicked at any time, the window is closed
    myWin.close()

# calls the main function
main()
