# Battle Squares
# By Kevin Yaiko


import pygame,sys,random
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1024
WINDOWHEIGHT = 760

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #Can add pygame.RESIZABLE
    pygame.display.set_caption('Battle Squares')
    player1x = 100
    player1y = 300
    
    while True:
        DISPLAYSURF.fill(WHITE)
        pygame.draw.line(DISPLAYSURF, BLACK, (WINDOWWIDTH/2,0), (WINDOWWIDTH/2,WINDOWHEIGHT),3)
        pygame.draw.circle(DISPLAYSURF, RED, (player1x,player1y), 15) 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if (event.key == K_RIGHT):
                    player1x += 5
                elif (event.key == K_LEFT):
                    player1x -= 5
                elif (event.key == K_UP):
                    player1y -= 5
                elif (event.key == K_DOWN):
                    player1y += 5
        pygame.display.update()

main()
