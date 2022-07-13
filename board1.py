def board():
   board = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]
   for i in board:
       for j in i:
         print(j, end = "  ")
       print()

board()

def check_mark(board, symbol):

    valid_move = False
    while not valid_move:
        print(symbol + "'s move")
        row = int(input("Row: "))
        col = int(input("Col: "))
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Please try again.")
        else:
            board[row][col] = symbol
            valid_move = True


def check_row(board, row):
    symbol = board[row][0]
    for col in range(1, 3):
        if board[row][col] != symbol:
            return None
    return symbol


def check_column(board, col):
    symbol = board[0][col]
    for row in range(1, 3):
        if board[row][col] != symbol:
            return None
    return symbol


def check_diagonal(board):

    symbol = board[0][0]
    for row in range(1, 3):
        if board[row][row] != symbol:
            return None
    return symbol

   
