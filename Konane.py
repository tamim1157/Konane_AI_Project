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
game.print()