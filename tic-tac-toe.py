#tic-tac-toe


# taking user input on his chance/steps
def takeinput():
    x = int(input("Enter the Index where you want to insert 0-8 "));
    print("\n")
    return x;

# function to print the board everytime
def printboard(board):
    for x in board:
        print(x)
    print("\n")    

# function which update the board whenever an input is taken
def updateboard(y,steps,board):
    if(y < 3):
        if(steps % 2):
                board[0][y] = 'x'
        else:
                board[0][y] = 'O'
    elif(y < 6):
        if(steps % 2):
            board[1][y%3] = 'x'
        else:
            board[1][y%3] = 'O'
    else:
        if(steps % 2):
            board[2][y%3] = 'x'
        else:
            board[2][y%3] = 'O'
    printboard(board)    

# function to check for a winning chance in all 8 possible combinations        
def checkwinner(board):

    x1 = board[0];
    if(x1 == ['x','x','x']):
        return 1
    elif(x1 == ['O','O','O']):
        return 2

    
    x2 = board[1];
    if(x2 == ['x','x','x']):
        return 1
    elif(x2 == ['O','O','O']):
        return 2
    

    x3 = board[2];
    if(x3 == ['x','x','x']):
        return 1
    elif(x3 == ['O','O','O']):
        return 2

    
    x4 = ''
    for x in range(3):
        x4 = x4 + board[x][0]
    if(x4 == 'xxx'):
        return 1
    elif(x4 == 'OOO'):
        return 2


    x5 = ""
    for x in range(3):
        x5 = x5 + board[x][0]
    if(x5 == 'xxx'):
        return 1
    elif(x5 == 'OOO'):
        return 2

    
    x6 = ""
    for x in range(3):
        x6 = x6 + board[x][0]
    if(x6 == 'xxx'):
        return 1
    elif(x6 == 'OOO'):
        return 2
    
    x7 = ""
    x7 = x7 + board[0][0] + board[1][1] + board[2][2]
    if(x7 == 'xxx'):
        return 1
    elif(x7 == 'OOO'):
        return 2
    x8 = ""
    x8 = x8 + board[0][2] + board[1][1] + board[2][0]
    if(x8 == 'xxx'):
        return 1
    elif(x8 == 'OOO'):
        return 2
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
        board = [["0",'1','2'],['3','4','5'],['6','7','8']]
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