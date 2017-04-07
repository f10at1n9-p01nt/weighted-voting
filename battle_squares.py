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
BLUE = (0,0,255)



def check_coordinates(x,y,region,windowwidth,windowheight):
    '''Checks to make sure the player can't cross center line'''
    print(x)
    if region == "left":
		if x + 20 < windowwidth/2:
			return 5
		else:
			return 0
    if region == "right":
		return None

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #Can add pygame.RESIZABLE
    pygame.display.set_caption('Battle Squares')
    player1x = 400
    player1y = 300
    player2x = 800
    player2y = 500
    
    while True:
		DISPLAYSURF.fill(WHITE)
		pygame.draw.line(DISPLAYSURF, BLACK, (WINDOWWIDTH/2,0), (WINDOWWIDTH/2,WINDOWHEIGHT),3)
		pygame.draw.circle(DISPLAYSURF, RED, (player1x,player1y), 15)
		pygame.draw.circle(DISPLAYSURF, BLUE, (player2x,player2y), 15)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if (event.key == K_RIGHT):
					DISTANCE = check_coordinates(player1x, player1y, "left", WINDOWWIDTH, WINDOWHEIGHT)
					player1x += DISTANCE
				elif (event.key == K_LEFT):
					player1x -= DISTANCE
				elif (event.key == K_UP):
					player1y -= DISTANCE
				elif (event.key == K_DOWN):
					player1y += DISTANCE  
				elif (event.key == K_s):
					player2y += 5
				elif (event.key == K_w):
					player2y -= 5
				elif (event.key == K_a):
					player2x -= 5
				elif (event.key == K_d):
					player2x += 5
			DISTANCE = 5
		pygame.display.update()

main()
