
# 18-06-NR Starting Board Class

class Board:

    # initializing board with Xs and Os
    def __init__(self):
        self.pieces = []
        for j in range(8):
            row = []
            for i in range(8):
                if (j + i) % 2 == 1:
                    row.append('O')
                else:
                    row.append('X')
            self.pieces.append(row)
        self.empty = []

    # showing the current status of the board
    def print(self):
        print('   1  2  3  4  5  6  7  8')
        for row in range(8):
            print(row+1, end = "  ")
            for col in range(8):
                print(self.pieces[row][col], end = "  ")
            print()

    