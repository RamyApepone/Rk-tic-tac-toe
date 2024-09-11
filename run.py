# tic toc toe game 
# setup board
gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
cur_player = "@"
player_winner = None
game_running = True
def myBoard(gameBoard):
  print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
  print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
  print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
myBoard(gameBoard)

# This statement will print the game board
# player input data
# checking the game 
# player turn
# checking the game for win or tie
