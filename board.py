size = 3

def create_board(n):
    grid = []                   # Create empty grid
    for y in range(3):          # Create rows one at a time
        row = []
        for x in range(3):      # Build up each row by appending to a list
            row.append(None)
        grid.append(row)        # Append the row (list) onto grid
    return grid

def player_turn(board, symbol):
    valid_move = False
    while not valid_move:
        print(symbol + "'s move")
        row = int(input("Row: "))
        col = int(input("Col: "))
        # Make sure the move is in empty space and is on the board.
        if row < 0 or row >= 3 \
                or col < 0 or col >= 3 \
                or board[row][col]:
            print("Invalid move.  Try again.")
        else:
            board[row][col] = symbol  # Record a valid move
            valid_move = True


def check_row(board, row):
    """
    Checks to see if one of the players got all the spaces in a row.  If so,
    it returns the symbol for that player.  If not, it returns None.
    """
    symbol = board[row][0]
    for col in range(1, 3):
        if board[row][col] != symbol:   # If we find non-matching symbol then
            return None                 # there isn't a winner on this row.
    return symbol   # Will only get here if all symbols in row match


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

def check_winner(board):
    """
    Checks to see if one of the players got three in a row by checking
    all the rows, columns, and two diagonals on the board.  If a player
    got three in a row, return the symbol for that player.  If not,
    return None.
    """
    # Check rows
    for row in range(3):
        winner = check_row (board, row)
        if winner:
            return winner

    # Check columns
    for col in range(3):
        winner = check_column(board, col)
        if winner:
            return winner

    # Check diagonals
    winner = check_down_diagonal(board)
    if winner:
        return winner
    winner = check_up_diagonal(board)

    return winner   # This could be None if last check didn't find a winner


def flip_turn(symbol):
    """
    Flips the player (symbol) whose turn it is.
    """
    if symbol == 'X':
        return 'O'
    else:
        return 'X'


def print_row_separator(columns):
    """
    Prints a row separator line for the board.
    For example, if columns is 3, it will print:
    --+---+--
    """
    print("--+", end="")
    for i in range(1, columns - 1):
        print("---+", end="")
    print("--")


def print_board(board):
    """
    Prints out tic-tac-board board
    """
    rows = 3                   # Could have used SIZE, but wanted
    cols = 3                # to show a different way to do this.
    for y in range(3):
        for x in range(cols):
            symbol = board[y][x]
            if not symbol:              # Print a space if symbol is None
                symbol = " "
            print(symbol, end="")
            if x < 2:            # Print column separator if not at end of line
                print(" | ", end="")
            else:
                print("")               # Print "new line" at end of line
        if y < 2:                # Print row separator if not at end of grid
            print_row_separator(cols)


def main():
    """
    Play a two-player game of tic-tac-toe
    """
    winner = None
    board = create_board(size)
    player = 'X'                    # Player X goes first
    num_moves = 0
    while winner == None:           # Take turns until we have winner
        print_board(board)
        player_turn(board, player)
        num_moves += 1              # Keep track of total moves made
        winner = check_winner(board)
        if not winner:
            if num_moves == 3 ** 2:  # If all spaces on board are filled
                winner = "No one"       # then there is no winner.
        player = flip_turn(player)

    print_board(board)
    print(winner + " won!")


if __name__ == '__main__':
    main()
