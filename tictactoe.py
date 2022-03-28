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

print("\033[95m-- TIC TAC TOE --\033[m\n")

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
        print("Ops, try again!")


#checking for winners horizontally
def check_horiz(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "*":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "*":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "*":
        winner = board[6]
        return True

#checking for winners vertically
def check_vert(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "*":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "*":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "*":
        winner = board[2]
        return True

#checking for winners diagonally
def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "*":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "*":
        winner = board[2]
        return True
    

#main function to check the winner
def check_winner():
    global game_running
    if check_horiz(board) or check_vert(board) or check_diag(board):
        print_board(board)
        print(f"The winner is {winner}")
        game_running = False


#checking for tie
def chack_tie(board):
    global game_running
    if "*" not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False


#switching players
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

#all functions
while game_running:
    print_board(board)
    player_input(board)
    check_winner()
    chack_tie(board)
    switch_player()
        
        


print("\033[93mGame Over\033[m")