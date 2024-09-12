# tic toc toe game 
# setup board
gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
cur_player = "@"
The_winner = None
game_running = True

print("--------------------------------")
print("Welcome to RK tic tac toe game\n")
print("Please follow the game instruction\n")
print("You can only enter number from 1-9\n")
print("Best of luck")
print("--------------------------------")

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
    global The_winner
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[1] != "-":
        The_winner = gameBoard[0]
        return True
    elif gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != "-":
        The_winner = gameBoard[3]
        return True
    elif gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] != "-":
        The_winner = gameBoard[6]
        return True

def Check_the_row(gameBoard):
    global The_winner
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] != "-":
        The_winner = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != "-":
        The_winner = gameBoard[1]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != "-":
        The_winner = gameBoard[2]
        return True

def check_my_diag(gameBoard):
    global The_winner
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != "-":
        The_winner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] != "-":
        The_winner = gameBoard[2]
        return True

def checktieGame(gameBoard):
    global game_running
    if "-" not in gameBoard:
        myBoard(gameBoard)
        print("The game is very tie!")
        game_running = False

def checkWinner():
    if check_my_diag(gameBoard) or checkGameHorizontal(gameBoard) or Check_the_row(gameBoard):
        print(f"The game winner is {The_winner} congratulation")

# change player
def PlayerTurn():
    global cur_player
    if cur_player == "@":
        cur_player = "$"
    else:
        cur_player = "@"

# checking again game win or tie
while game_running:
    myBoard(gameBoard)
    myPlayerData(gameBoard)
    checkWinner()
    checktieGame(gameBoard)
    PlayerTurn()