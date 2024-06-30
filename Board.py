import copy
class Board:
    # 28-06-Tamim: Defining jumping distance for player and opponent pieces
    DIR1 = [[0,1], [0,-1], [-1, 0], [1, 0]]
    DIR2 = [[0,2], [0,-2], [-2,0], [2,0]]

    # 18-06-NR Starting Board Class
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

    # 28-06-Tamim Starting Board Class
    # checking if row and column is valid
    @staticmethod
    def isValid(row, col):
        if (row>=0 and row<=7) and (col>=0 and col <= 7):
            return True
        else:
            return False

    # returning list of possible moves for side also includes double jumps
    def listMoves(self, side):
        player = side
        if player == 'X': 
            opponent = 'O'
        else:
            opponent = 'X'
        Moves = []
        for (r, c) in self.empty:
            for i in range(4):
                # row and column for DIR1, aka one block away
                row1 = r+self.DIR1[i][0]
                col1 = c+self.DIR1[i][1]
                # row and column for DIR2, aka two blocks away
                row2 = r+self.DIR2[i][0]
                col2 = c+self.DIR2[i][1]
                # checking if farther one is valid
                if Board.isValid(row2, col2):                 
                    #increment count wherever 'X' and 'O' in line
                    if (self.pieces[row1][col1] == opponent) and (self.pieces[row2][col2] == player):
                        Moves.append([(row2+1, col2+1), (r+1, c+1)])            
        # considering double moves
        for move in Moves:
            r1 = move[0][0]
            c1 = move[0][1]            
            r2 = move[1][0]
            c2 = move[1][1]
            # move is down
            if (r1-r2 == -2):
                # finding all valid moves down
                while Board.isValid(r2+1, c1-1) and self.pieces[r2][c1-1] == opponent and self.pieces[r2+1][c1-1] == '.':
                    Moves.append([move[0], (r2+2, c1)])
                    r1 += 2
                    r2 += 2             
            # move is up
            elif (r1-r2 == 2):
                # finding all valid moves up
                while Board.isValid(r2-3, c1-1) and self.pieces[r2-2][c1-1] == opponent and self.pieces[r2-3][c1-1] == '.':
                    Moves.append([move[0], (r2-2, c1)])
                    r1 -= 2
                    r2 -= 2               
            # move is right
            elif (c1-c2 == -2):
                # finding all valid moves to the right
                while Board.isValid(r1-1, c2+1) and self.pieces[r1-1][c2] == opponent and self.pieces[r1-1][c2+1] == '.':
                    Moves.append([move[0], (r1, c2+2)])
                    c1 += 2
                    c2 += 2                
            # move is left
            elif (c1-c2 == 2):
                # finding all valid moves to the left
                if Board.isValid(r1-1, c2-3) and self.pieces[r1-1][c2-2] == opponent and self.pieces[r1-1][c2-3] == '.':
                    Moves.append([move[0], (r1, c2-2)])
                    c1 -= 2
                    c2 -= 2       
        return Moves    
    # 28-06-Tamim Ending Board Class

    # 30-06-NR Starting Board Class
    # Method for returning move length difference
    def staticEvaluation(self, player):
        if player == 'X':
            opponent = 'O'
        else:
            opponent = 'X'
        return len(self.listMoves(player)) - len(self.listMoves(opponent))
    
    # the minimax function
    # since the depth is in multiple of 2, even => computer (max), odd => user (min)
    @staticmethod
    def minimax(board, player, depth, alpha, beta):
        if player == 'X':
            opponent = 'O'
        else:
            opponent = 'X'
        # end, perform static evaluation
        if depth == 1:
            return (board.staticEvaluation(player))
        # max node 
        if depth %2 == 0:
            moves = board.listMoves(player)
            for curMove in moves:
                next_board = copy.deepcopy(board)
                next_board.move(curMove[0][0], curMove[0][1], curMove[1][0], curMove[1][1])
                bv = Board.minimax(next_board, opponent, depth - 1, alpha, beta)
                if bv > alpha:
                    alpha = bv
                if alpha >= beta:
                    return beta
            return alpha
        # min node
        else:
            moves = board.listMoves(opponent)            
            for curMove in moves:
                next_board = copy.deepcopy(board)
                next_board.move(curMove[0][0], curMove[0][1], curMove[1][0], curMove[1][1]) 
                bv = Board.minimax(next_board, player, depth - 1, alpha, beta)
                if bv < beta:
                    beta = bv
                if beta <= alpha:
                    return alpha           
            return beta
    # 30-06-NR Ending Board Class
    