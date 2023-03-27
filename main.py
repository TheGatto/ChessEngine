pieces = ['X','wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK']
class Board:
    def __init__(self, xlen:int=8, ylen:int=8) -> None:
        self.xlen = xlen
        self.ylen = ylen
        self.board = [[0 for i in range(self.xlen)] for i in range(self.ylen)]
    def move(self, xcoord:int, ycoord:int, newxcoord:int, newycoord:int) -> None:
        try:
            piece = self.board[xcoord][ycoord]
            self.board[xcoord][ycoord] = 0
            self.board[newxcoord][newycoord] = piece
        except:
            print("Illegal Move")
            self.board[xcoord][ycoord] = piece # noqa
    def __str__(self) -> str:
        printable = ''
        for row in self.board:  # Convert the 2D list to printable form
            for item in row:
                printable += str(pieces[item]) + '  '  # Add spacing
            printable += '\n'  # Add new line
        return printable
    def checkMove(self, xcoord: int, ycoord: int, newxcoord: int, newycoord: int) -> bool:
        if self.board[newxcoord][newycoord] != "X":
            pieceColour = pieces[self.board[xcoord][ycoord]][0]
            captureColour = pieces[self.board[newxcoord][newycoord]][0]
            if pieceColour == captureColour:
                return False
        if newycoord == ycoord and newxcoord == xcoord:
            return False # If attempting to move on the same place
        if newxcoord > 7 or newycoord > 7:
            return False # Outside board range
        piece = self.board[xcoord][ycoord]
        if piece == 4 or piece == 10: # Rook
            if newycoord == ycoord:
                for col in range(min(xcoord, newxcoord) + 1, max(xcoord, newxcoord)):
                    print("iterating through", col, ycoord)
                    if board.board[col][ycoord] != 0:
                        return False
                return True
            elif newxcoord == xcoord:
                for col in range(min(xcoord, newycoord) + 1, max(xcoord, newycoord)):
                    print("iterating through", xcoord, col)
                    if board.board[xcoord][col] != 0:
                        return False
                return True
            return False
        if piece == 3 or piece == 9: # Bishop
            distancex = abs(xcoord-newxcoord)
            distancey = abs(ycoord-newycoord)
            if distancex == distancey:  # bishop
                return True
            return False

board = Board()
board.board[0][0] = pieces.index('bR')
board.board[0][4] = pieces.index('bR')
print(board)
if board.checkMove(0,0,0,4):
    board.move(0,0,0,4)
else:
    print("illegal move")
print(board)
