import sys      # Needed for exit
from Board import Board     # Using the Board class form board.py

# 18-06-NR Creating Initial Promt

count = 0
user = input("Do you want to play X or O? X goes first. (X/O): ")
if user == 'X':
    computer = 'O'
    count = 1
elif user == 'O':
    computer = 'X'
else:
    print("Invalid Input")
    sys.exit()

game = Board()

# 26-06-Tamim Remove Middle Elements
game.remove(4,4)
game.remove(4,5)
# 26-06-Tamim Remove Middle Elements End

game.print()

# 18-06-NR Creating Initial Promt End