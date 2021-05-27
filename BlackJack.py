import random
#-------------------------------------------------------------------------------
                #GLOBALS VARIABLES
table_chips=1000
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
#-------------------------------------------------------------------------------
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return " {r} of {s}".format(s=self.suit , r= self.rank)
#-------------------------------------------------------------------------------
class Deck():
    def __init__(self):
        self.new_deck=[]
        for i in suits:
            for y in ranks:
                NewCard=Card(i,y)
                self.new_deck.append(NewCard)
    def shuffle(self):
        random.shuffle(self.new_deck)

    def remove_one(self):
        return_card= self.new_deck.pop(0)
        return return_card

    def __str__(self):
        return "len is : {l}".format(l=len(self.new_deck))
#-------------------------------------------------------------------------------
class Hand():
    def __init__(self):
        self.Hand=[]
        self.value = 0
        self.aces = 0
    def addcart(self,card):
        self.Hand.append(card)
        self.value= self.value + card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


    def __str__(self):
            return "the value is : {l}".format(l=self.value)
#-------------------------------------------------------------------------------
class Bet():
    def __init__(self,bet):
        self.bet=bet
        self.total=table_chips

    def withdraw(self):
        if self.bet>table_chips:
            print("not enough money")
        else:
            self.total= table_chips - self.bet
    def deposit(self):
        self.total = table_chips +(self.bet * 2)

    def __str__(self):
        return "YOUR TOTAL CHIPS ARE : {l}".format(l=self.total)

#-------------------------------------------------------------------------------
                #DEFINE FUNCTIONS
def hit_or_stay(new_deck,Player_hand,Dealer_hand):
    global playing
    choise=input("Do you want to hit Y-N?\n")
    if choise == 'Y':
        Card5= new_deck.remove_one()
        Player_hand.addcart(Card5)
        print(Card5)
        print(Player_hand.value)
    elif choise =='N':
        playing =False
        return playing

#-------------------------------------------------------------------------------
                      #MAIN
while True:
    if first==1:
        print("#######WELCOME TO MY BLACKJACK GAME#######")
        print("#########TABLE OF 1000 CHIPS")
        print("------------------------------------------")
        first=0
    playing=True
    new_deck=Deck()
    new_deck.shuffle()

    My_bet=int(input("GIVE ME YOUR BET:\n"))
    new_bet=Bet(My_bet)
    new_bet.withdraw()
    print(new_bet)
    print("\nPLAYER FIRST 2 CARDS:")

    Player_hand=Hand()
    Card1=new_deck.remove_one()
    print(Card1)
    Player_hand.addcart(Card1)

    Card2=new_deck.remove_one()
    print(Card2)
    Player_hand.addcart(Card2)

    print("\nDEALER FIRST CARD:")
    Dealer_hand=Hand()
    Card3=new_deck.remove_one()
    print(Card3)
    Dealer_hand.addcart(Card3)

    Card4=new_deck.remove_one()
    print("<HIDEN CARD>")
    Dealer_hand.addcart(Card4)
    print("------------------------------------------")
    print("PLAYER CARD VALUE:")
    print(Player_hand.value)


    while playing:
            hit_or_stay(new_deck,Player_hand,Dealer_hand)
            print("PLAYER'S HAND:")
            print(Player_hand.value)
            if Player_hand.value>21:
                print("DEALER WINS")
                playing = False
                break
            if Player_hand.value == 21:
                print("BLACKJACK")
                playing=False
                break
    if Player_hand.value <21:
            print("\nDEALERDS SECOND CARD IS: {c}".format(c=Card4))
            print("DEALERS FIRST 2 CARDS IS {d}".format(d=Dealer_hand.value))
            while Dealer_hand.value<17:
                newCard=new_deck.remove_one()
                Dealer_hand.addcart(newCard)
                print("NEW CARD:{c}".format(c=newCard))
                print("DEALERS HAND IS {d}".format(d=Dealer_hand.value))
                print("------------------------------------------")
            if Dealer_hand.value >21:
                print("DEALER BURST...PLAYER WINS")
                new_bet.deposit()
            elif Dealer_hand.value > Player_hand.value:
                print("DEALER WINS")
            elif Dealer_hand.value < Player_hand.value:
                print("PLAYER WINS")
                new_bet.deposit()
            print("YOUR MONEY: {m}".format(m=new_bet))


    game= input("do you want to bet?")
    if game == 'Y':
        continue
    elif game == 'N':
        break
