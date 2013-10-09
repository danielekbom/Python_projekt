from graphics import *
import time
import random

class Enemy1:
	def __init__(self):
		self.ball = Image(Point(1400,random.randint(20,700)),"images/enemy1.gif")
		pictures = [1,2,3,4,5,6,7,8,9]
		currentImage = self.
	
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
		self.ball = Image(self.getCenter(),"images/enemy1/" + x +  ".gif")
		eliminated.draw(window)
		