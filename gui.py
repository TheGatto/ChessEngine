from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

white, black ,red = (255,255,255),(0,0,0),(255,0,0)
pygame.init()
dimensions = (800,800)
backgroundRGB = (230, 230, 230)
gameDisplay = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Chess')
gameDisplay.fill(backgroundRGB)
pygame.display.flip()
running = True
pieces = ['','wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK']
assetList = ['', '', 'chessAssets/wN.png', 'chessAssets/wB.png', 'chessAssets/wR.png']
class Piece:
    def __init__(self, x:int, y:int, type:str):
        self.X = x * 80 - 5
        self.Y = y * 80 - 5
        self.type = type
        imp = pygame.image.load(assetList[pieces.index(type)]).convert_alpha()
        imp = pygame.transform.scale(imp, (90, 90))
        gameDisplay.blit(imp, (self.X, self.Y))

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
            pygame.draw.rect(gameDisplay, white, [SIZE * z, SIZE * i, SIZE, SIZE])
        else:
            pygame.draw.rect(gameDisplay, black, [SIZE * z, SIZE * i, SIZE, SIZE])
        cnt += 1
    cnt -= 1
#Add a nice boarder
pygame.draw.rect(gameDisplay, black, [SIZE, SIZE, boardLength * SIZE, boardLength * SIZE], 1)


rook = Piece(1, 8, 'wR')
knight = Piece(2, 8, 'wN')
bishop = Piece(3,8, 'wB')


pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()