def create_board():
    grid = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]
    for i in grid:
        print(i)


create_board()

print("Player " + ", it is your turn. ")
row = int(input("Pick a row:"
                "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
column = int(input("Pick a column:"
                   "[left column: enter 0, middle column: enter 1, right column enter 2]:"))


def player_turn(board, symbol):
    valid_move = False
    while not valid_move:
        print(symbol + "'s move")

        # Make sure the move is in empty space and is on the board.
        if row < 0 or row >= 3 \
                or column < 0 or column >= 3 \
                or board[row][column]:
            print("Invalid move.  Try again.")
        else:
            board[row][column] = symbol  # Record a valid move
            valid_move = True


def check_column(board, column):
    """
    Checks to see if one of the players got all the spaces in a column.  If so,
    it returns the symbol for that player.  If not, it returns None.
    """
    symbol = board[0][column]
    for row in range(1, 3):
        if board[row][column] != symbol:
            return None
    return symbol  # Will only get here is all symbols in column match


def check_down_diagonal(board):
    """
    Checks to see if one of the players got all the spaces in the diagonal
    going from top-left corner to bottom-right corner.  If so,
    it returns the symbol for that player.  If not, it returns None.
    """
    symbol = board[0][0]
    for row in range(1, 3):
        if board[row][row] != symbol:
            return None
    return symbol  # Will only get here is all symbols in diagonal match


def check_up_diagonal(board):
    """
    Checks to see if one of the players got all the spaces in the diagonal
    going from bottom-left corner to top-right corner.  If so,
    it returns the symbol for that player.  If not, it returns None.
    """
    symbol = board[0][2]
    for row in range(1, 3):
        if board[row][2 - row] != symbol:
            return None
    return symbol  # Will only get here is all symbols in diagonal match

