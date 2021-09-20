from IPython.display import clear_output
import random

def display_board(board):
    # a function that displays the current state of the board

    print(board[7] + "|" + board[8] + "|" + board[9])
    print("_|_|_")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("_|_|_")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(" | | ")


def player_input():
    # functions to receive the and assign the marker for each player
    p1_marker = "empty"
    p2_marker = "empty"
    while p1_marker != "X" and p1_marker != "O":
        p1_marker = input("Player 1: Do you choose 'X' or 'O' for your marker? ")
        
    if p1_marker == "X":
        p2_marker = "O"
    else:
        p2_marker = "X"
    return p1_marker,p2_marker


def win_check(board, mark):
    # a functions that checks for a current winner
    result = "GameOn"
    if board[1] == board[2] == board[3] == mark:
        result = "Win"
    elif board[4] == board[5] == board[6] == mark:
        result = "Win"
    elif board[7] == board[8] == board[9] == mark:
        result = "Win"
    elif board[3] == board[6] == board[9] == mark:
        result = "Win"
    elif board[2] == board[5] == board[8] == mark:
        result = "Win"
    elif board[1] == board[4] == board[7] == mark:
        result = "Win"
    elif board[1] == board[5] == board[9] == mark:
        result = "Win"
    elif board[3] == board[5] == board[7] == mark:
        result = "Win"
        
    if result == "Win":
        return True
    else:
        return False

    
def choose_first():
    first_to_go = random.randint(1,2)
    return first_to_go


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    if not ' ' in board:
        return True
    else:
        return False


def player_choice(board):
    p_choice = int(input("What is your choice?\n" ))
    if space_check(board, p_choice):
        return p_choice

    else:
        print("Invalid choice")
        player_choice(board)

        
def place_marker(board, marker, position):
    # a functions that changes the board according to player moves
    board[position] = marker
    return board


def replay():
    answer = input("Do you want to play more?Yes/No ")
    if answer == "Yes":
        return True
    elif answer == "No":
        return False
    else:
        replay()
    
print('Welcome to Tic Tac Toe!')

while True:
    
    p1_mark, p2_mark = player_input()
    board = ["#"]+[" "] * 9
    if choose_first() == 1:
        player_1 = p1_mark
        player_2 = p2_mark
        print("Player 1 goes first.")
    else:
        print("Player 2 goes first.")
        player_2 = p1_mark
        player_1 = p2_mark

    game_on = True
    
    while game_on:
        display_board(board)
        if full_board_check(board):
            print('This game is a draw')
            break
        position = player_choice(board)
        board = place_marker(board, player_1, position)
        display_board(board)
        if win_check(board, player_1 ) == True:
            print("Congrats! Player 1 wins!")
            break
        clear_output()
        display_board(board)
        position = player_choice(board)
        board = place_marker(board, player_2, position)
        display_board(board)
        if win_check(board, player_2) == True:
            print("Congrats! Player 2 wins!")
            break
        clear_output()
        

    if not replay():
        break