def possible(board,y,x,n):
    #check if n is in the row
    for i in range(0,9):
        if board[y][i] == n:
            return False
    #check if n is in the column
    for i in range(0,9):
        if board[i][x] == n:
            return False
    #check if n is in the 3x3 box
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == n:
                return False
    return True

def solve(board): 
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if possible(board,y,x,n):
                        board[y][x] = n
                        if solve(board):
                            return True
                        board[y][x] = 0
                return False
    return True
