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
        if newycoord == ycoord and newxcoord == xcoord:
            return False
        piece = self.board[xcoord][ycoord]
        if piece == 4 or piece == 10:
            if newycoord == ycoord or newxcoord == xcoord:
                return True
            return False
        if piece == 3 or piece == 9:
            distancex = abs(xcoord-newxcoord)
            distancey = abs(ycoord-newycoord)
            if distancex == distancey:  # bishop
                # for i in range(xcoord, distancex):
                #     ...
                return True
            return False

board = Board()
board.board[0][0] = pieces.index('bR')
print(board)
if board.checkMove(0,0,4,0):
    board.move(0,0,4,0)
print(board)
