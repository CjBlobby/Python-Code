import random
from Bank import Bankount

class Card():

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def display(self):
        print(" _____________")
        print("|             |")
        print("|             |")
        print("|             |")
        print(f" {self.face} of {self.suit}")
        print("|             |")
        print("|             |")
        print("|             |")
        print(" _____________")

    def value(self):
        values = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
                  "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        return values[self.face]

class Deck():
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    faces = ["A", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    
    def build(self):
        for suit in self.suits:
            for face in self.faces:
                self.deck.append(Card(suit, face))
    
    def mix(self):
        random.shuffle(self.deck)


def hand_val(cardlist):
    handvalue = 0
    for card in cardlist:
        handvalue += card.value()

    return handvalue

def draw_card(deck):
    card = deck[0]
    del deck[0]
    return card



        

account = Bankount()
game = True
choice = ""

print("Welcome to Conor'sino! You will play only one game: (as I am very broke)\n",
      "Twenty-one! My sidekick, Computer, will battle you. BEGIN!\n")

while game:
    pot = 0
    plyrhand = []
    cpuhand = []
    while pot == 0:
        pot = int(input(f"You have £{account.balance}. Place your bet:\t"))
        if pot <= account.balance:
            account.withdraw(pot)
            pot *= 2
        else:
            print("Insufficient funds")
            pot = 0
    
    deck = Deck()
    deck.build()
    deck.mix()
    plyrhand.append(draw_card(deck.deck))
    plyrhand.append(draw_card(deck.deck))
    cpuhand.append(draw_card(deck.deck))
    cpuhand.append(draw_card(deck.deck))

    print("\n\n\n\n\n\n\n\n\nPlayer's hand:")
    for card in plyrhand:
        card.display()
    print("\n\nComputer's first card:")
    cpuhand[0].display()

    print("\n\n")
    while True:
        choice = input("Stick or Twist? (s/t):\t")
        if choice == "t":
            plyrhand.append(draw_card(deck.deck))
        elif choice == "s":
            break
        else:
            print("Please input 's' or 't':\t")
        plyrhand[-1].display()

    aceval = 1
    handval = 0
    for card in plyrhand:
        if card.face == "A":
            aceval = int(input("You have an ace! Is it's value a 1 or an 11?\t"))
            handval += aceval
        else:
            handval += card.value()
    
    cpuval = 0
    for card in cpuhand:
        cpuval += card.value()

    while cpuval <= handval and cpuval < 21:
        cpuhand.append(draw_card(deck.deck))
        cpuval += cpuhand[-1].value()

    print("\n\nComputer's hand:\n\n")
    for card in cpuhand:
        card.display()

    if handval > 21:
        print("\n\nBust. You lost")
    elif cpuval > 21:
        print(f"\n\nYou win with a value of {handval}!")
        account.deposit(pot)
    else:
        print("\n\nYou lost! Unlucky.")
        
    











