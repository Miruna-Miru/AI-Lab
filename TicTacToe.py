import math

# Function to print the board with improved formatting
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()  # Add a new line for better readability

# Function to check for a winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

# Function to check for a draw
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True  # Player is 'X', AI is 'O'
    
    while True:
        print_board(board)
        
        if check_winner(board) or is_draw(board):
            break
        
        if player_turn:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                player_turn = False
            else:
                print("Invalid move! Try again.")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
                player_turn = True
    
    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"{winner} wins!")
    else:
        print_board(board)
        print("It's a draw!")

# Start the game
play_game()
