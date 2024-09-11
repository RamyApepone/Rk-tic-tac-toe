# tic toc toe game 
# setup board
gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
cur_player = "@"
player_winner = None
game_running = True
# This statement will print the game board
def myBoard(gameBoard):
  print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
  print("**********")
  print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
  print("**********")
  print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])

# player input data
def myPlayerData(myBoard):
    player_inp = int(input("Please Enter number from 1 to 9: "))
    if player_inp >= 1 and player_inp <= 9 and myBoard[player_inp-1] == "-":
        myBoard[player_inp-1] = cur_player
    else:
        print("There is already a player on the spot!")
# checking the game 
# player turn
# checking the game for win or tie
while game_running:
    myBoard(gameBoard)
    myPlayerData(gameBoard)