# tic toc toe game 
# setup board
gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
cur_player = "@"
player_winner = None
game_running = True

print("Welcome to RK tic tac toe game")

# This statement will print the game board
def myBoard(gameBoard):
  print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
  print("**********")
  print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
  print("**********")
  print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])

# player input data
def myPlayerData(gameBoard):
    player_inp = int(input("Please Enter number from 1 to 9: "))
    if player_inp >= 1 and player_inp <= 9 and gameBoard[player_inp-1] == "-":
        gameBoard[player_inp-1] = cur_player
    else:
        print("Please wait for your turn!")

# checking the game win or tie
def checkGameHorizontal(gameBoard):
    global winningPlayer
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[1] != "-":
        winningPlayer = gameBoard[0]
        return True
    elif gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != "-":
        winningPlayer = gameBoard[3]
        return True
    elif gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] != "-":
        winningPlayer = gameBoard[6]
        return True

def Check_the_row(gameBoard):
    global winningPlayer
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] != "-":
        winningPlayer = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != "-":
        winningPlayer = gameBoard[1]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != "-":
        winningPlayer = gameBoard[2]
        return True

def check_my_diag(gameBoard):
    global winningPlayer
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != "-":
        winningPlayer = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] != "-":
        winningPlayer = gameBoard[2]
        return True

def checktieGame(myBoard):
    global game_running
    if "-" not in gameBoard:
        myBoard(gameBoard)
        print("This is tie game")
        game_running = False



# change player
# checking again game win or tie
while game_running:
    myBoard(gameBoard)
    myPlayerData(gameBoard)