from graphics import _root,GraphWin,Point,Image,Text
import time
import random
import enemies
try:
	import Tkinter as tk
except:
	import tkinter as tk

MARGIN_TOP_BOTTOM=72
MARGIN_SIDES=72

class Game(GraphWin):
	
	def __init__(self):
		#GraphWin.__init__
		master = tk.Toplevel(_root)
		width = master.winfo_screenwidth()-MARGIN_SIDES
		height = master.winfo_screenheight()-MARGIN_TOP_BOTTOM
		title="AlabamaMAN! Shootin' turtels and beavers and snakes and frikkin' BEATURAKES! AlabamaMAN!"
		master.protocol("WM_DELETE_WINDOW", self.close)
		tk.Canvas.__init__(self, master, width=width, height=height,cursor="cross")
		self.master.title(title)
		self.pack()
		master.resizable(0,0)
		self.foreground = "black"
		self.items = []
		self.mouseX = None
		self.mouseY = None
		self.bind("<Button-1>", self._onClick)
		self.height = height
		self.width = width
		self.autoflush = False
		self._mouseCallback = None
		self.trans = None
		self.closed = False
		self.gameClosing = False
		self.gameRunning = True
		master.lift()
		if self.autoflush: _root.update()
	
	def close(self):
		if self.gameClosing:
			return
		self.gameClosing=True
		closeText = Text(Point(self.width/2,self.height/2),"Close?")
		closeText.setStyle("bold")
		closeText.setSize(36)
		closeText.draw(self)
		wait = self.getMouse()
		closeText.undraw()
		del closeText
		self.gameRunning=False
	
	def play(self):
		'''Starts a new game. Game loop idea taken from http://www.koonsolo.com/news/dewitters-gameloop/'''
		background = Image(Point(self.width/2,self.height/2),"images/background1.gif")
		background.draw(self)
		hero=Hero()
		enemy=[enemies.enemy1(self)]
		
		
		while self.gameRunning:
			mouseClick = self.checkMouse()
			if mouseClick:
				pass
				
			for en in enemy:
				en.walk()
			
			
			
			time.sleep(0.01)
			_root.update()
			
			del mouseClick
			if self.gameRunning and hero.isDead():
				self.gameOver()
		for en in enemy:
			del en
		del enemy
		del hero
		del background
		GraphWin.close(self)
		
	def highscore(self):
		pass
	
	def gameOver(self):
		gameOverText = Text(Point(self.width/2,self.height/2),"Game Over")
		gameOverText.setStyle("bold")
		gameOverText.setSize(36)
		gameOverText.draw(self)
		wait = self.getMouse()
		gameOverText.undraw()
		del gameOverText
		self.highscore()
		
	def menu(self):
		''' TODO Lgga till meny
		Placeholder returnera om spelet ska fortstta eller inte.
		'''
		self.play()
	
	
	def getMouse(self):
		while self.gameRunning:
			mouseClick=self.checkMouse()
			if mouseClick==None:
				time.sleep(0.005)
			else:
				return mouseClick
		return None

class Hero():
	'''Our hero! Haz HP and shit!'''
	hp=100
	def isDead(self):
		'''Is he dead? Hell NO!'''
		return self.hp<=0

def main():
	game=Game()
	while game.gameRunning:
		game.menu()

if __name__ == "__main__":
	main()
