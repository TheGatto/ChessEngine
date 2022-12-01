from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
white,black,red = (255,255,255),(0,0,0),(255,0,0)
pygame.init()
dimensions = (800,800)
backgroundRGB = (230, 230, 230)
gameDisplay = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Chess')
gameDisplay.fill(backgroundRGB)
pygame.display.flip()
running = True
#Size of squares
size = 80

#board length, must be even
boardLength = 8
gameDisplay.fill(white)

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
        else:
            pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
        cnt +=1
    cnt-=1
#Add a nice boarder
pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)

pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()