#!/usr/bin/env python
import pygame
import random
pygame.display.init()
from random import randint as ri
from threading import Thread
screensurf=pygame.display.set_mode((800, 600))
pygame.display.set_caption("lines - 2K pygame demo", "lines - 2K pygame demo")
sfadeclock=pygame.time.Clock()
progrun=1
fadesurf=pygame.Surface((800, 600)).convert()
fadesurf.set_alpha(10)
fadeit=0
def screenfade():
	global fadeit
	while progrun:
		sfadeclock.tick(6)
		fadeit=1
		
class superpathline:
	def __init__(self):
		self.x=ri(0, screensurf.get_width()-1)
		self.y=ri(0, screensurf.get_height()-1)
		self.d=ri(0, 3)
		self.sx=screensurf.get_width()-1
		self.sy=screensurf.get_height()-1
		self.ci=ri(10, 100)
		self.ct=0
		self.speed=ri(1, 3)
		self.thickness=ri(1, 3)
		self.color=pygame.Color(ri(0, 255), ri(0, 255), ri(0, 255))
	def renprocess(self):
		for x in [""]*self.speed:
			self.ox=self.x
			self.oy=self.y
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
				self.x=0
			if self.x<0:
				self.x=self.sx
			#ypos rollover
			if self.y>self.sy:
				self.y=0
			if self.y<0:
				self.y=self.sy
			pygame.draw.line(screensurf, self.color, (self.x+self.thickness, self.y+self.thickness), (self.x, self.y), 1)
efflist=[]
for eff in [""]*30:
	efflist.extend([superpathline()])
clock=pygame.time.Clock()
sideproc=Thread(target = screenfade, args = [])
sideproc.start()
while progrun:
	for eff in efflist:
		eff.renprocess()
	clock.tick(60)
	if fadeit:
		fadeit=0
		screensurf.blit(fadesurf, (0, 0))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type==pygame.QUIT or event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
			progrun=0