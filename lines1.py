#!/usr/bin/env python
import pygame
import random
pygame.display.init()
from random import randint as ri
from threading import Thread
scrn=pygame.display.set_mode((800, 600))
pygame.display.set_caption("lines - 2K pygame demo", "lines - 2K pygame demo")
sfclock=pygame.time.Clock()
progrun=1
fadesurf=pygame.Surface((800, 600)).convert()
fadesurf.set_alpha(10)
fadeit=0
def sfade():
	global fadeit
	while progrun:
		sfclock.tick(6)
		fadeit=1
#path object
class spl:
	def __init__(self):
		#position
		self.x=ri(0, scrn.get_width()-1)
		self.y=ri(0, scrn.get_height()-1)
		#direction, rollover x&y
		self.d=ri(0, 3)
		self.sx=scrn.get_width()-1
		self.sy=scrn.get_height()-1
		#turn-increment
		self.ci=ri(10, 100)
		self.ct=0
		#speed, thickness
		self.speed=ri(1, 3)
		self.thk=ri(1, 3)
		self.color=pygame.Color(ri(0, 255), ri(0, 255), ri(0, 255))
	def renpr(self):
		for x in [""]*self.speed:
			#direction changer
			if self.ct==self.ci:
				self.ct=0
				self.ci=ri(10, 100)
				self.d+=ri(-1, 1)
				if self.d==-1:
					self.d=3
				elif self.d==4:
					self.d=0
			else:
				self.ct += 1
			if self.d==0:
				self.x+=1
			if self.d==2:
				self.x-=1
			if self.d==1:
				self.y+=1
			if self.d==3:
				self.y-=1
			#xpos rollover
			if self.x>self.sx:
				self.x=-10
			if self.x<-10:
				self.x=self.sx
			#ypos rollover
			if self.y>self.sy:
				self.y=-10
			if self.y<-10:
				self.y=self.sy
			pygame.draw.line(scrn, self.color, (self.x+self.thk, self.y+self.thk), (self.x, self.y), 1)
efflist=[]
for eff in [""]*30:
	efflist.extend([spl()])
clock=pygame.time.Clock()
#fader timer
sideproc=Thread(target = sfade, args = [])
sideproc.start()
#main loop
while progrun:
	for eff in efflist:
		eff.renpr()
	clock.tick(60)
	#fader
	if fadeit:
		fadeit=0
		scrn.blit(fadesurf, (0, 0))
	pygame.display.update()
	#tiny event handler
	for event in pygame.event.get():
		if event.type==pygame.QUIT or event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
			progrun=0