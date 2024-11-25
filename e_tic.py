import math

def print_board(board):
    for row in board:
        print("  |  ".join(row))
        print("-"*15)
    print()

def is_winner(board):
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!=" ":
            return row[0]
    
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!=" ":
            return board[0][col]
    
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=" ":
        return board[0][0]

    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=" ":
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def minmax(board,depth,ismax):
    win= is_winner(board)
    if win=="X":
       return -1
    if win=="O":
       return 1
    if is_draw(board):
       return 0
    
    if ismax:
        best=-math.inf
        for i in range(3):
            for  j in range(3):
                if board[i][j]==" ":
                    board[i][j]="X"
                    score=minmax(board,depth+1,False)
                    board[i][j]=" "
                    best=max(best,score)
        return best
    else:
        best=math.inf
        for i in range(3):
            for  j in range(3):
                if board[i][j]==" ":
                    board[i][j]="O"
                    score=minmax(board,depth+1,True)
                    board[i][j]=" "
                    best=min(best,score)
        return best

def best_move(board):
    best=-math.inf
    move=None
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="O"
                score=minmax(board,0,False)
                board[i][j]=" "
                if score>best:
                    best=score
                    move=(i,j)
    return move

board=[[" "for _ in range(3)] for _ in range(3)]
player = True
while(True):
    print_board(board)
    if is_draw(board) or is_winner(board):
        break
    if player:
        r=int(input("Enter row :  "))
        c=int(input("Enter col :  "))
        if board[r][c]!=" ":
            print("Invalide move try again")
        else:
            board[r][c]="X"
            player=False
    else:
        move=best_move(board)
        if move:
            board[move[0]][move[1]]="O"
            player=True
    win=is_winner(board)
    if win:
        print("Wineer !!",win)
    else:
        print("Draw!")

