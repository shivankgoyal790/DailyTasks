#tic-tac-toe


# taking user input on his chance/steps
def takeinput():
    x = int(input("Enter the Index where you want to insert 0-8 "));
    print("\n")
    return x;

# function to print the board everytime
def printboard(board):
    print(board)
        

# function which update the board whenever an input is taken
def updateboard(y,steps,board):
    if(steps % 2):
        board[y] = 'x'
    else:
        board[y] = 'O'
    printboard(board)    

# function to check for a winning chance in all 8 possible combinations        
def checkwinner(board):
    if(board[0] == board[3] == board[6]):
        if(board[0] == 'x'):
            return 1
        else:
            return 2
    elif(board[1] == board[4] == board[7]):
        if(board[1] == 'x'):
            return 1
        else:
            return 2  
    elif(board[2] == board[5] == board[8]):
        if(board[2] == 'x'):
            return 1
        else:
            return 2
    elif(board[6] == board[7] == board[8]):
        if(board[8] == 'x'):
            return 1
        else:
            return 2 
    elif(board[3] == board[4] == board[5]):
        if(board[3] == 'x'):
            return 1
        else:
            return 2  
    if(board[0] == board[1] == board[2]):
        if(board[1] == 'x'):
            return 1
        else:
            return 2         
    elif(board[0] == board[4] == board[8]):
        if(board[0] == 'x'):
            return 1
        else:
            return 2
    elif(board[6] == board[4] == board[2]):
        if(board[2] == 'x'):
            return 1
        else:
            return 2  
    
    else:
        return 0

def startgame():
    print("\n")
    print("Welcome to the game!!")
    print("\n")
    ch = input("Press 'y' to Start the Game and 'n' to End it ")
    print("\n")
    print("Note : Always Player 1 starts the Game ")
    print("\n")
    while ch == 'y':
        board = ["0",'1','2','3','4','5','6','7','8']
        printboard(board);
        for x in range(1,10):
            z = takeinput()
            updateboard(z,x,board)
            if(x > 4):
                winner = checkwinner(board)
                if(winner == 0):
                    continue
                else:
                    print("Congratulations Player {} is the Winner!!".format(winner))
                    print("\n")
                    print('Press y to start the game and n to end it')
                    print("\n")
                    print("Note : Always Player 1 Starts the Game ")
                    ch = input()
                    break
                      
    else:
        print("Game Over")    


startgame()