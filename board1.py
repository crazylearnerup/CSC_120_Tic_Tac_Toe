def board():
   board = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]
   for i in board:
       for j in i:
         print(j, end = "  ")
       print()

board()