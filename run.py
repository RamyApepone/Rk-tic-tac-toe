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
    while True:
        try:
            playerInp = int(input("Please Enter number from 1 to 9: "))
            if playerInp >= 1 and playerInp <= 9 and gameBoard[playerInp-1] == "-":
                gameBoard[playerInp-1] = currentPlayer
                break
            else:
                print("Invalid input! Box is taken or out of range. Try again another number.")
        except ValueError:
            print("Please enter a valid number?")

# Ask if the player want to restart tic tac toe game
def restartGame():
    global gameBoard, Thewinner, currentPlayer, gameRunning
    restart = input("Do you want to restart (yes/no):").strip().lower()
    if restart == "yes":
        gameBoard = ["-", "-", "-",
                      "-", "-","-",
                     "-", "-", "-"]
    
        Thewinner = None
        currentPlayer = "@"
        gameRunning = True
        print("Game restarted now!")
    else:
        gameRunning = False
        print("Thanks for playing RK tic tac toe")

# checking if the game is win or tie
def checkHorizontaly(gameBoard):
    global Thewinner
    for i in range(0, 9, 3):
        if gameBoard[i] == gameBoard[i+1] == gameBoard[i+2] and gameBoard[i] != "-":
            Thewinner = gameBoard[i]
            return True
    return False


# checking the game row
def checkGameRow(gameBoard):
    global Thewinner
    for i in range(3):
        if gameBoard[i] == gameBoard[i+3] == gameBoard[i+6] and gameBoard[i] != "-":
            Thewinner = gameBoard[i]
            return True
    return False


def checkDiagonally(gameBoard):
    global Thewinner
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != "-":
        Thewinner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] != "-":
        Thewinner = gameBoard[2]
        return True
    return False


# This function displa
def checktieGame(gameBoard):
    global gameRunning
    if "-" not in gameBoard and Thewinner is None:
        myBoard(gameBoard)
        print("The game is a tie!")
        gameRunning = False


# This function checks for the game winner
def checkWinner():
    if checkDiagonally(gameBoard) or checkHorizontaly(gameBoard) or checkGameRow(gameBoard):
        myBoard(gameBoard)
        print(f"The game winner is {Thewinner}! congratulation!!!")
        return True
    return False


# change player
def PlayerTurn():
    global currentPlayer
    currentPlayer = "$" if currentPlayer == "@" else "@"


# Main loop
while gameRunning:
    myBoard(gameBoard)
    myPlayerData(gameBoard)
    if checkWinner():
        break
    checktieGame(gameBoard)
    PlayerTurn()
restartGame()
