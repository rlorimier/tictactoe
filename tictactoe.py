"""
TIC TAC TOE
"""
#variables
board = ["*", "*", "*",
        "*", "*", "*",
        "*", "*", "*"]
player = "X" #first player is always X
winner = None
game_running = True

#creating the board game
def print_board(board):
    print("-" *10)
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" *10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" *10)
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("-" *10)


#taking player input
def player_input(board):
    choice = int(input("Enter your move: "))
    if choice >= 1 or choice <= 9 and board[choice -1] != "*":
        board[choice -1] = player
    else:
        print("Ops")


#checking for winners


#switching players


#all functions
def main():
    while True:
        print_board(board)
        player_input(board)


print("TIC TAC TOE\n")
main()