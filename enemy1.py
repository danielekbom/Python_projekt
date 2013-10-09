from graphics import *
import time
import random
import itertools

class Enemy1:
	def __init__(self):
		self.ball = Image(Point(1400,random.randint(20,700)),"images/enemy1/1.gif")
		self.currentImage = itertools.cycle('123456789')
	
	def draw(self,window):
		self.ball.draw(window)
		
	def move(self):
		self.ball.move(-1,0)
		
	def getCenter(self):
		return self.ball.getAnchor()
		
	def changeColor(self,window):
		self.ball.undraw()
		eliminated = Image(self.getCenter(),"images/enemy1_eliminated.gif")
		eliminated.draw(window)
	
	def nextImage(self):
		self.ball.undraw()
		self.ball = Image(self.getCenter(),"images/enemy1/" + next(self.currentImage) +  ".gif")
		self.ball.draw(window)
		
