import sys # Needed for exit
import copy
from Board import Board # Using the Board class form board.py
from Genetic import Genetic

# 18-06-NR Creating Initial Promt
count = 0
user = input("\nDo you want to play X or O? X goes first. (X/O): ")
if user == 'X':
    computer = 'O'
    count = 1
elif user == 'O':
    computer = 'X'
else:
    print("\nInvalid Input\n")
    sys.exit()

print("\n1) Minimax")
print("2) Genetic")
mode = int(input("\nEnter The Preffered Mode: "))
if(mode > 3 or mode <=0):
    print("\nInvalid Input\n")
    sys.exit()

game = Board()
# 26-06-Tamim Remove Middle Elements
game.remove(4,4)
game.remove(4,5)
# 26-06-Tamim Remove Middle Elements End
print()
game.print()
# 18-06-NR Creating Initial Promt End

if(mode == 1):
    # 30-06-NR Creating Game Calculations
    while True:
        # computer's turn
        if count%2 == 0:
            moves = game.listMoves(computer)
            # check if game is over
            if len(moves) == 0:
                print("\nPlayer Won\n")
                exit()        
            print("\nComputer's Turn: ", end = " ")
            bestVal = - sys.maxsize
            for move in moves:
                alpha = -1000
                beta = 1000
                temp = copy.deepcopy(game)
                temp.move(move[0][0], move[0][1], move[1][0], move[1][1])
                cbv = Board.minimax(temp, computer, 5, alpha, beta)       
                if cbv > bestVal:
                    bestVal = cbv
                    bestMove = move
            print("Move " + str(bestMove[0]) + " to " + str(bestMove[1]))
            game.move(bestMove[0][0], bestMove[0][1], bestMove[1][0], bestMove[1][1])   
        # player's turn
        else:
            moves = game.listMoves(user)
            # check if game is over
            if len(moves) == 0:
                print("\nComputer Won\n")
                exit()
            print("\nUser's Turn\n")
            # print all the available moves
            print("Available moves:")
            for i in range(len(moves)):
                print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))
            move = int(input("\nEnter the number of the move that you want to make: ")) - 1
            if(move + 1 > len(moves) or move + 1 <= 0):
                print("\nInvalid Input\n")
                sys.exit()
            game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
        game.print()
        count += 1
        # 30-06-NR Ending Game Calculations

elif(mode == 2):
    # 30-06-NR Creating Game Calculations
    while True:
        # computer's turn
        if count%2 == 0:
            moves = game.listMoves(computer)
            # check if game is over
            if len(moves) == 0:
                print("\nPlayer Won\n")
                exit()        
            print("\nComputer's Turn: ", end = " ")
            ans = Genetic.main()
            ans = ans % len(moves)
            bestMove = moves[ans]
            print("Move " + str(bestMove[0]) + " to " + str(bestMove[1]))
            game.move(bestMove[0][0], bestMove[0][1], bestMove[1][0], bestMove[1][1])   
        # player's turn
        else:
            moves = game.listMoves(user)
            # check if game is over
            if len(moves) == 0:
                print("\nComputer Won\n")
                exit()
            print("\nUser's Turn\n")
            # print all the available moves
            print("Available moves:")
            for i in range(len(moves)):
                print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))
            move = int(input("\nEnter the number of the move that you want to make: ")) - 1
            if(move + 1 > len(moves) or move + 1 <= 0):
                print("\nInvalid Input\n")
                sys.exit()
            game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
        print()
        game.print()
        count += 1
        # 30-06-NR Ending Game Calculations
