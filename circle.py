from graphics import *
import time
import random

class Circle1:
	def __init__(self):
		self.ball = Circle(Point(1400,random.randint(20,700)),10)
		self.ball.setFill("red")
		self.ball.setWidth(3)
	
	def draw(self,window):
		self.ball.draw(window)
		
	def move(self):
		self.ball.move(-1,0)
		
	def getCenter(self):
		return self.ball.getCenter()
		
	def changeColor(self,window):
		self.ball.setFill("green")