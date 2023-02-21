from random import shuffle
values = {"duggi" : 2,"tiggi":3,"chowki" : 4,"panji" : 5,"chakki" : 6,"satti":7,"ethi" : 8,"nhela" : 9,"dhela" : 10, "gulab" : 11,"begam" : 12,"badshah" : 13,"ikki" : 14}
suits = ["eeth","chidi","paan","hukum"]

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def printcard(self):
        print("{} ki {}".format(self.suit,self.rank))


# mycard = Card("hukum","ikki")
# mycard.printcard()

class Deck(Card):

    def __init__(self):
        self.cardlist = []
        for x in suits:
            for y in values:
                newcard = Card(x,y)
                self.cardlist.append(newcard)
        shuffle(self.cardlist)

   
    def displaycards(self):
        for x in self.cardlist:
             x.printcard()

mydeck = Deck()
# mydeck.displaycards();

class Players(Card):

    def __init__(self,name,mycards):
        self.mycards = []
        self.name = name
        self.mycards = mycards

    def displayplayercards(self):
        for x in self.mycards:
             x.printcard()
        print("\n")
    def removecards(self):
        return self.mycards.pop(0)
    def addcards(self,newlist):
        self.mycards.extend(newlist)

        
Player1cards = mydeck.cardlist[0:26]
Player2cards = mydeck.cardlist[26:]

player1 = Players("shivank",Player1cards)
player2 = Players("Adarsh",Player2cards)
newlist = []

while len(player1.mycards)!=0 and len(player2.mycards)!=0:
    if(len(player1.mycards) == 0):
        print("player 2 is the winner")
    elif(len(player2.mycards) == 0):
        print("player 1 is the winner")
    card1 = player1.removecards()
    card2 = player2.removecards()
    newlist.append(card1)
    newlist.append(card2)
    card1 = newlist[-2]
    card2 = newlist[-1]
    if(card1.value > card2.value):
        player1.addcards(newlist)
        newlist.clear()
    elif(card1.value < card2.value):
        player2.addcards(newlist)
        newlist.clear()
    else:
        if(len(player1.mycards) < 5):
            print("player 2 is the winner")
            break
        elif(len(player2.mycards)  < 5):
            print("player 1 is the winner")
            break
        for x in range(5):
            newlist.append(player1.removecards())
            newlist.append(player2.removecards())

player2.displayplayercards()








