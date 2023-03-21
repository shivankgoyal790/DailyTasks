from random import shuffle
def shufflelist(mylist):
    shuffle(mylist) 
    return mylist

def playerguess():
    x = input("guess a index")
    return int(x);

def checkguess(x,mylist):
    if('0' == mylist[x]):
        print("You won")
    else:
        print("You loose")
    
mylist = ['','0' ,'']
newlist = shufflelist(mylist)
guess = playerguess()
checkguess(guess,newlist)