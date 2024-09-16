# setup game board
gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
currentPlayer = "@"
Thewinner = None
gameRunning = True

# Welcome message and game instruction
print("------------------------------------")
print("Welcome to RK tic tac toe game!!\n")
print("Please follow the game instruction\n")
print("1. You can only enter number from 1-9\n")
print("2. Players take turns\n")
print("3. Player 1to align three of their marks in a row wins the game\n")
print("Enjoy playing Rk Tic Tac Toe, and the best player win!")
print("------------------------------------")


# This statement will print the game board
def myBoard(gameBoard):
    print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print("**********")
    print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print("**********")
    print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])


# player input data
def myPlayerData(gameBoard):
    playerInp = int(input("Please Enter number from 1 to 9: "))
    if playerInp >= 1 and playerInp <= 9 and gameBoard[playerInp-1] == "-":
        gameBoard[playerInp-1] = currentPlayer
    else:
        print("Box is taken try another number!")


# Ask if the player want to restart tic tac toe game
def restartGame(gameBoard):
    restart = input("Do you want to restart (yes/no):").strip().lower()
    if restart == "yes":
        print("you play again")


# checking if the game is win or tie
def checkHorizontaly(gameBoard):
    global Thewinner
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[1] != "-":
        Thewinner = gameBoard[0]
        return True

    elif gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != "-":
        Thewinner = gameBoard[3]
        return True

    elif gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] != "-":
        Thewinner = gameBoard[6]
        return True


# checking the game row
def checkGameRow(gameBoard):
    global Thewinner
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] != "-":
        Thewinner = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != "-":
        Thewinner = gameBoard[1]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != "-":
        Thewinner = gameBoard[2]
        return True


def checkDiagonally(gameBoard):
    global Thewinner
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != "-":
        Thewinner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] != "-":
        Thewinner = gameBoard[2]
        return True


# This function displa
def checktieGame(gameBoard):
    global gameRunning
    if "-" not in gameBoard:
        myBoard(gameBoard)
        print("The game is very tie!")
        gameRunning = False


# This function going to check the winner
def checkWinner():
    if checkDiagonally(gameBoard) or checkHorizontaly(gameBoard) or checkGameRow(gameBoard):
        print(f"The game winner is {Thewinner} congratulation")


# change player
def PlayerTurn():
    global currentPlayer
    if currentPlayer == "@":
        currentPlayer = "$"
    else:
        currentPlayer = "@"


# checking again game win or tie
while gameRunning:
    myBoard(gameBoard)
    myPlayerData(gameBoard)
    checkWinner()
    checktieGame(gameBoard)
    PlayerTurn()
    restartGame(gameBoard)
