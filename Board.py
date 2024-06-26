
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

    # 18-06-NR Ending Board Class

    # 26-06-Tamim Starting Board Class

    # removing a piece from the board
    def remove(self, row, col):
        temp = self.pieces[row - 1][col - 1]
        self.pieces[row - 1][col - 1] = '.'
        self.empty.append((row - 1, col - 1))
        return temp
    
    # Move a piece from start position (r1, c1) to end position at (r2, c2)
    def move(self, r1, c1, r2, c2):
        
        # determine if moving X or O
        player = self.pieces[r1-1][c1-1]
        
        # removing the moved piece
        self.remove(r1, c1)

        # moving the piece
        self.pieces[r2-1][c2-1] = player
        self.empty.remove((r2-1, c2-1))

        #going down
        if (r1-r2 < 0):
            other_r = r1 + 1
            while other_r < r2:
                self.remove(other_r, c1)
                other_r += 2
            
        # going up
        if (r1-r2 > 0):
            other_r = r1 - 1
            while other_r > r2:
                self.remove(other_r, c1)
                other_r -= 2

        # going right
        if (c1-c2 < 0):
            other_c = c1 + 1
            while other_c < c2:
                self.remove(r1, other_c)
                other_c += 2

        # going left
        if (c1-c2 > 0):            
            other_c = c1 - 1
            while other_c > c2:
                self.remove(r1, other_c)
                other_c -= 2

    # 26-06-Tamim Ending Board Class

    