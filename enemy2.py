from graphics import *
import time
import random
import itertools

class Enemy2:
	eliminated = False
	nextImageOrNot = 0
	
	def __init__(self):
		self.ball = Image(Point(1400,random.randint(50,580)),"images/enemy2/1.gif")
		self.currentImage = itertools.cycle('12345')
		self.nextImageOrNot = itertools.cycle([True,False,False,False,False])
	
	def draw(self,window):
		self.win=window
		self.ball.draw(window)
		
	def move(self):
		self.ball.move(-1,0)
		if next(self.nextImageOrNot):
			self.nextImage()
		
	def getCenter(self):
		return self.ball.getAnchor()
		
	def changeColor(self,window):
		self.eliminated = True
		self.ball.undraw()
		eliminated = Image(self.getCenter(),"images/enemy2/enemy2_eliminated.gif")
		eliminated.draw(window)
		
	
	def nextImage(self):
		self.ball.undraw()
		self.ball = Image(self.getCenter(),"images/enemy2/" + next(self.currentImage) +  ".gif")
		self.ball.draw(self.win)
		
