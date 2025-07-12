import math

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a winner
def check_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if board is full
def is_full(board):
    return ' ' not in board

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Human move
def human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
        print("Invalid move. Try again.")

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.")
    print_board()
    
    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("You win! ")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! ")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()
