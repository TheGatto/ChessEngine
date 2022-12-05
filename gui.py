from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

beige, brown , black, white = (235, 209, 166), (163, 116, 79), (0, 0, 0), (255, 255, 255)
pygame.init()
dimensions = (800,800)
backgroundRGB = (230, 230, 230)
gameDisplay = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Chess')
gameDisplay.fill(backgroundRGB)
pygame.display.flip()
running = True
pieces = ['','wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK']
assetList = ['', 'chessAssets/wP.png', 'chessAssets/wN.png', 'chessAssets/wB.png', 'chessAssets/wR.png','chessAssets/wQ.png','chessAssets/wK.png','chessAssets/bP.png','chessAssets/bN.png','chessAssets/bB.png','chessAssets/bR.png','chessAssets/bQ.png','chessAssets/bK.png']

def addPiece(x:int, y:int, type:str):
    X = x * 80 - 5
    Y = y * 80 - 5
    imp = pygame.image.load(assetList[pieces.index(type)]).convert_alpha()
    imp = pygame.transform.scale(imp, (90, 90))
    gameDisplay.blit(imp, (X, Y))
def addPieceRow(y:int, type:str):
    Y = y * 80 - 5
    for i in range(8):
        imp = pygame.image.load(assetList[pieces.index(type)]).convert_alpha()
        imp = pygame.transform.scale(imp, (90, 90))
        gameDisplay.blit(imp, ((i+1)*80-5, Y))
class Board:
    def setup():
        addPiece(1, 8, 'wR')
        addPiece(2, 8, 'wN')
        addPiece(3, 8, 'wB')
        addPiece(4, 8, 'wQ')
        addPiece(5, 8, 'wK')
        addPiece(6, 8, 'wB')
        addPiece(7, 8, 'wN')
        addPiece(8, 8, 'wR')
        addPieceRow(7, 'wP')

        addPiece(1, 1, 'bR')
        addPiece(2, 1, 'bN')
        addPiece(3, 1, 'bB')
        addPiece(4, 1, 'bQ')
        addPiece(5, 1, 'bK')
        addPiece(6, 1, 'bB')
        addPiece(7, 1, 'bN')
        addPiece(8, 1, 'bR')
        addPieceRow(2, 'bP')
#Size of squares
SIZE = 80

#board length, must be even
boardLength = 8
gameDisplay.fill(white)

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(gameDisplay, beige, [SIZE * z, SIZE * i, SIZE, SIZE])
        else:
            pygame.draw.rect(gameDisplay, brown, [SIZE * z, SIZE * i, SIZE, SIZE])
        cnt += 1
    cnt -= 1
#Add a nice boarder
pygame.draw.rect(gameDisplay, black, [SIZE, SIZE, boardLength * SIZE, boardLength * SIZE], 3)

Board.setup()

pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()