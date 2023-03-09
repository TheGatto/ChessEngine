from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import gameReader
BOARD = [[0 for i in range(8)] for i in range(8)]
beige, brown, black, white, dimensions, backgroundRGB = (235, 209, 166), (163, 116, 79), (0, 0, 0), (255, 255, 255), (
800, 800), (230, 230, 230)
pygame.init()
gameDisplay = pygame.display.set_mode(dimensions)
gameDisplay.fill(backgroundRGB)
pygame.display.set_caption('Chess')
running = True
pieces = ['', 'wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']
assetList = ['', 'chessAssets/wP.png', 'chessAssets/wN.png', 'chessAssets/wB.png', 'chessAssets/wR.png',
             'chessAssets/wQ.png', 'chessAssets/wK.png', 'chessAssets/bP.png', 'chessAssets/bN.png',
             'chessAssets/bB.png', 'chessAssets/bR.png', 'chessAssets/bQ.png', 'chessAssets/bK.png']


def addPiece(x: int, y: int, type: int, size: int):
    X = x * size
    Y = y * size
    BOARD[y - 1][x - 1] = type
    imp = pygame.image.load(assetList[type]).convert_alpha()
    imp = pygame.transform.scale(imp, (size, size))
    gameDisplay.blit(imp, (X, Y))


class Board:
    @staticmethod
    def change(list):
        for num, row in enumerate(list):
            for num2, item in enumerate(row):
                addPiece(num2 + 1, num + 1, item, size) if item != 0 else ...

    @staticmethod
    def setup(size: int):

        default = [[10, 8, 9, 11, 12, 9, 8, 10], [7, 7, 7, 7, 7, 7, 7, 7], [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1], [4, 2, 3, 5, 6, 3, 2, 4]]
        Board.change(default)

    @staticmethod
    def draw(boardLength: int, SIZE: int):
        count = 0
        for i in range(1, boardLength + 1):
            for j in range(1, boardLength + 1):
                if count % 2 == 0:
                    pygame.draw.rect(gameDisplay, beige, [SIZE * j, SIZE * i, SIZE, SIZE])
                else:
                    pygame.draw.rect(gameDisplay, brown, [SIZE * j, SIZE * i, SIZE, SIZE])
                count += 1
            count -= 1
        pygame.draw.rect(gameDisplay, black, [SIZE, SIZE, boardLength * SIZE, boardLength * SIZE], 3)

    @staticmethod
    def update():
        gameDisplay.fill(backgroundRGB)
        Board.draw(boardLength, size)
        Board.change(BOARD)
        pygame.display.flip()

    @staticmethod
    def move(x, y, newx, newy):
        piece, BOARD[x][y] = BOARD[x][y], 0
        BOARD[newx][newy] = piece
        Board.update()

    @staticmethod
    def castle(turn, long):
        castleMoves = [[(((7, 4, 7, 6)), ((7, 7, 7, 5))), ((7, 4, 7, 2), (7, 0, 7, 3))], [((0, 4, 0, 6), (0, 7, 0, 5)), ((0, 4, 0, 2), (0, 0, 0, 3))]]
        for i in range(2):
            Board.move(*castleMoves[turn][long][i])
        Board.update()

size = 80
boardLength = 8

Board.draw(boardLength, size)
Board.setup(size)
pygame.display.flip()
notationGame = "e2-e4/e7-e5/g1-f3/b8-c6/f1-c4/g8-f6/d2-d3/d7-d6/O-O/c8-g4/c1-g5/d8-d7/b1-c3/O-O-O"
GAME, notationGame = gameReader.readCode(notationGame)
count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                try:
                    if len(GAME[count]) == 2:
                        Board.castle(*GAME[count])
                    else:
                        Board.move(*GAME[count])
                    count += 1
                except:
                    print("You've reached the last move")
            elif event.key == pygame.K_LEFT:
                if count > 0:
                    if count > 2 and notationGame[count - 3][0] == 'O':
                        Board.move(*(GAME[count - 1][2], GAME[count - 1][3], GAME[count - 1][0], GAME[count - 1][1]))
                        Board.move(*(GAME[count - 2][2], GAME[count - 2][3], GAME[count - 2][0], GAME[count - 2][1]))
                        Board.move(*(GAME[count - 3][2], GAME[count - 3][3], GAME[count - 3][0], GAME[count - 3][1]))
                        count -= 3
                    else:
                        count -= 1
                        Board.move(*(GAME[count][2], GAME[count][3], GAME[count][0], GAME[count][1]))
                else:
                    print("You've reached the first move")
            elif event.key == pygame.K_p:
                print(GAME)
                print(notationGame)
