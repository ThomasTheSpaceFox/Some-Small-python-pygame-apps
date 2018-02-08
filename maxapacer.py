#!/usr/bin/env python
import pygame
import random
pygame.display.init()
from random import randint as ri
from threading import Thread
screensurf=pygame.display.set_mode((700, 250))
pygame.display.set_caption("Max-a-pacer - 1 player", "Max-a-pacer - 1 player")
clock=pygame.time.Clock()
progrun=1
pygame.font.init()
simplefont = pygame.font.SysFont(None, 22)

def drawdisp(xpos, ypos, placenumber, endcolor, scorestr, play1highlight=0):
	pn=0
	xpl=60
	xwid=40
	xwid2=20
	while pn!=10:
		if play1highlight and playturn==1 and twoplay==1 and pn==placenumber:
			color=(0, 120, 255)
		elif pn==placenumber:
			color=(0, 255, 0)
		else:
			color=(255, 255, 255)
		pygame.draw.rect(screensurf, color, pygame.Rect(xpos, ypos, xwid, xwid))
		pygame.draw.rect(screensurf, (0, 0, 0), pygame.Rect(xpos+40, ypos, xwid2, xwid))
		xpos+=xpl
		pn+=1
	pygame.draw.rect(screensurf, endcolor, pygame.Rect(xpos-10, ypos, xwid2, xwid))
	score=simplefont.render(scorestr, True, (0, 0, 0), (255, 0, 0))
	screensurf.blit(score, (10+xpos, ypos+10))

def drawfeild(no1, no2, no3, sc1, sc2, sc3):
	pygame.draw.rect(screensurf, (255, 0, 0), pygame.Rect(0, 0, 700, 160))
	pygame.draw.rect(screensurf, (0, 120, 0), pygame.Rect(10, 10, 610, 140))
	drawdisp(10, 10, no1, (255, 0, 255), sc1, 1)
	drawdisp(10, 60, no2, (255, 255, 0), sc2)
	drawdisp(10, 110, no3, (0, 255, 255), sc3)

no1=10
no2=10
no3=10
old1=10
old2=10
old3=10
sp=0
sc=0
tie=0

keysdict={
pygame.K_0: 0,
pygame.K_KP0: 0,
pygame.K_1: 1,
pygame.K_KP1: 1,
pygame.K_2: 2,
pygame.K_KP2: 2,
pygame.K_3: 3,
pygame.K_KP3: 3,
pygame.K_4: 4,
pygame.K_KP4: 4,
pygame.K_5: 5,
pygame.K_KP5: 5,
pygame.K_6: 6,
pygame.K_KP6: 6,
pygame.K_7: 7,
pygame.K_KP7: 7,
pygame.K_8: 8,
pygame.K_KP8: 8,
pygame.K_9: 9,
pygame.K_KP9: 9}

twoplay=0
playturn=2
helpme=simplefont.render("pick a number from 0-9. The computer (cyan) will also pick 1.", True, (255, 255, 255), (0, 0, 0))
helpme2=simplefont.render("The one closest to the 'pacer' (yellow) will get a point.", True, (255, 255, 255), (0, 0, 0))
helpme3=simplefont.render("Press [n] for new game, [ESC] to quit, or [t] for 2 player.", True, (255, 255, 255), (0, 0, 0))
p1turn=simplefont.render("It is now player 1's turn.", True, (255, 255, 255), (0, 0, 0))
p2turn=simplefont.render("It is now player 2's turn.", True, (255, 255, 255), (0, 0, 0))
while progrun:
	newgame=0
	screensurf.fill((0, 0, 0))
	if not twoplay:
		drawfeild(no1, no2, no3, "you: "+str(sp), "tie: "+str(tie), "com: "+str(sc))
	else:
		drawfeild(no1, no2, no3, "p1: "+str(sp), "tie: "+str(tie), "p2: "+str(sc))
		if playturn==1:
			playturn=2
			screensurf.blit(p2turn, (0, 230))
		else:
			playturn=1
			screensurf.blit(p1turn, (0, 230))
	screensurf.blit(helpme, (0, 170))
	screensurf.blit(helpme2, (0, 190))
	screensurf.blit(helpme3, (0, 210))
	pygame.display.update()
	userent=0
	counttrack=60
	count=0
	timeoutbreak=0
	while not userent:
		clock.tick(30)
		for event in pygame.event.get():
			if userent:
				break
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_n:
					newgame=1
					sp=0
					sc=0
					tie=0
					twoplay=0
					userent=1
					pygame.display.set_caption("Max-a-pacer - 1 player", "Max-a-pacer - 1 player")
					break
				if event.key==pygame.K_t:
					newgame=1
					sp=0
					sc=0
					tie=0
					twoplay=1
					playturn=2
					userent=1
					pygame.display.set_caption("Max-a-pacer - 2 player", "Max-a-pacer - 2 player")
					break
				if event.key==pygame.K_ESCAPE:
					progrun=0
					userent=1
					break
				for key in keysdict:
					if event.key==key:
						if playturn==2 and twoplay==1:
							no3=keysdict[key]
							no2=ri(0, 9)
							userent=1
							break
						elif playturn==1 and twoplay==1:
							no1=keysdict[key]
							userent=1
							break
						elif twoplay==0:
							no1=keysdict[key]
							no2=ri(0, 9)
							no3=ri(0, 9)
							userent=1
							break
			if event.type==pygame.QUIT:
				progrun=0
				userent=1
				break
	if progrun and not newgame and (playturn==2 or twoplay==0) and not timeoutbreak:
		p1sm=abs(no2-no1)
		comsm=abs(no3-no1)
		if p1sm>comsm:
			sc += 1
		elif p1sm<comsm:
			sp += 1
		else:
			tie += 1
