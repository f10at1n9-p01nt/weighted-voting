# Battle Squares
# By Kevin Yaiko


import pygame,sys,random
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1024
WINDOWHEIGHT = 760
PLAYERSIZE = 30
MOVE = 20

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

player1rect = pygame.Rect(400,200,PLAYERSIZE,PLAYERSIZE)
player2rect = pygame.Rect(800,300,PLAYERSIZE,PLAYERSIZE)


def check_middle(player):
	'''Checks to make sure the player can't cross center line'''
	if player.right + MOVE < WINDOWWIDTH/2 or player.left - MOVE > WINDOWWIDTH/2:
		return MOVE
	else:
		return 0


def check_edge(player):
	'''Checks to make sure the player can't leave left and right edges'''
	if player.left - MOVE >= 0 and player.right + MOVE <= WINDOWWIDTH:
		return MOVE
	else:
		return 0


def check_top(player):
	if player.top - MOVE >= 0:
		return MOVE
	else:
		return 0
		

def check_bottom(player):
	if player.bottom + MOVE <= WINDOWHEIGHT:
		return MOVE
	else:
		return 0


def main():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #Can add pygame.RESIZABLE
	pygame.display.set_caption('Battle Squares')
	DISTANCE = MOVE
    
	while True:
		DISPLAYSURF.fill(WHITE)
		pygame.draw.line(DISPLAYSURF, BLACK, (WINDOWWIDTH/2,0), (WINDOWWIDTH/2,WINDOWHEIGHT),3)
		pygame.draw.rect(DISPLAYSURF, BLUE, player1rect)
		pygame.draw.rect(DISPLAYSURF, RED, player2rect)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if (event.key == K_d):
					player1rect.right += check_middle(player1rect)
				elif (event.key == K_a):
					player1rect.left -= check_edge(player1rect)
				elif (event.key == K_w):
					player1rect.top -= check_top(player1rect)
				elif (event.key == K_s):
					player1rect.bottom += check_bottom(player1rect)
				elif (event.key == K_DOWN):
					player2rect.bottom += check_bottom(player2rect)
				elif (event.key == K_UP):
					player2rect.top -= check_top(player2rect)
				elif (event.key == K_LEFT):
					player2rect.left -= check_middle(player2rect)
				elif (event.key == K_RIGHT):
					player2rect.right += check_edge(player2rect)
		pygame.display.update()

main()
