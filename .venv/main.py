from random import randint

def printBoard():
    print(board[0])
    print(board[1])
    print(board[2])

def winCondition(board):
    if ((board[0][0] == board[0][1] == board[0][2]) and board[0][0] != "_"):
        return True
    if ((board[1][0] == board[1][1] == board[1][2]) and board[1][0] != "_"):
        return True
    if ((board[2][0] == board[2][1] == board[2][2]) and board[2][0] != "_"):
        return True
    if ((board[0][0] == board[1][0] == board[2][0]) and board[0][0] != "_"):
        return True
    if ((board[0][1] == board[1][1] == board[2][1]) and board[0][1] != "_"):
        return True
    if ((board[0][2] == board[1][2] == board[2][2]) and board[0][2] != "_"):
        return True
    if ((board[0][0] == board[1][1] == board[2][2]) and board[0][0] != "_"):
        return True
    if ((board[0][2] == board[1][1] == board[2][0]) and board[0][2] != "_"):
        return True
    return False

print("Welcome to TIC TAC TOE!!!!!!!!")

remainingSpots = [0, 1, 2, 3, 4, 5, 6, 7, 8]
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

team = input("Would you like to go first (X) or go second (O)? ")
while (not(team == "X" or team == "O")):
    team = input("Please input a valid option (X or O): ")

if team == "O":
    computerMove = remainingSpots.pop(randint(0, len(remainingSpots)))
    board[computerMove // 3][computerMove % 3] = "X"
printBoard()
print("________________________")
lastmove = ""
while(not winCondition(board)):
    move = int(input("Please input where you would like to place an " + team + " (places are labeled 0-8, left-to-right, top-to-bottom): "))
    while (move not in remainingSpots):
        move = int(input("Please input a valid location: "))
    remainingSpots.pop(remainingSpots.index(move))
    board[move // 3][move % 3] = team
    printBoard()
    lastmove = team
    print("__________________________")
    if (winCondition(board)):
        break
    computerMove = remainingSpots.pop(randint(0, len(remainingSpots)-1))
    board[computerMove // 3][computerMove % 3] = "X" if team == "O" else "O"
    printBoard()
    lastmove = "X" if team == "O" else "O"

if (lastmove == team):
    print("wow good job you won against my trash ai tic tac toe player")
else: 
    print("LOL how do you even lose its picking random spots. u suk")



