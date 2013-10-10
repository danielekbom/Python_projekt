from graphics import *
import time
import random
import itertools

class Enemy1:
	
	def __init__(self):
		self.pos=Point(1400,random.randint(20,700))
		self.enemyImages = itertools.cycle([Image(Point(self.pos.getX()-int(x),self.pos.getY()),"images/enemy1/" + x +  ".gif") for x in '123456789'])
		self.ball = next(self.enemyImages)
		self.eliminated=False
	
	def draw(self,window):
		self.win=window
		self.ball.draw(window)
	
	def move(self):
		if(not self.eliminated):
			self.ball.undraw()
			self.ball.move(-10,0)
			self.ball = next(self.enemyImages)
			self.ball.draw(self.win)
			self.pos=self.ball.getAnchor()
		
	def getCenter(self):
		return self.pos

	def changeColor(self,window=None):
		if not window:
			window=self.win
		if self.eliminated:
			self.eliminated.undraw()
			del self
		else:
			self.ball.undraw()
			del self.ball
			del self.enemyImages
			self.eliminated = Image(self.pos,"images/enemy1_eliminated.gif")
			self.eliminated.draw(window)
	
		
