import graphics
from graphics import _root,GraphWin,Point,Text
import time
import random
import enemyclasses
try:
	import Tkinter as tk
except:
	import tkinter as tk

try:
	from PIL import Image, ImageTk
except:
	from pil import Image, ImageTk

MARGIN_TOP_BOTTOM=72
MARGIN_SIDES=72

class Game(GraphWin):
	
	def __init__(self):
		
		#Runs in fullscreen
		_root.attributes('-fullscreen', True)
		
		#GraphWin.__init__
		master = tk.Toplevel(_root)
		width = master.winfo_screenwidth() #-MARGIN_SIDES
		height = master.winfo_screenheight() #-MARGIN_TOP_BOTTOM
		title="AlabamaMAN! Shootin' turtels and beavers and snakes and frikkin' BEATURAKES! AlabamaMAN!"
		master.protocol("WM_DELETE_WINDOW", self.close)
		tk.Canvas.__init__(self, master, width=width, height=height,cursor="cross")
		self.master.title(title)
		self.pack()
		#master.resizable(0,0)
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
	
	def play(self, level=1):
		'''
		Starts a new game.
		
		level - Start a game at level <level>
		
		Game loop idea taken from
		http://www.koonsolo.com/news/dewitters-gameloop/
		'''
		self.setBackground(level)
		hero=Hero(self)
		life=Life(self,3,self.width)
		currentScore=CurrentScore(self,self.width)
		enemyClassList=enemyclasses.getAllEnemies(maxLevel=1)
		enemies=[random.choice(enemyClassList)(self)]
		
		while self.gameRunning:
			mouseClick = self.checkMouse()
			if mouseClick:
				pass
				
			for enemy in enemies:
				enemy.walk()
			
			
			
			time.sleep(0.01)
			_root.update()
			
			del mouseClick
			if self.gameRunning and hero.isDead():
				self.gameOver()
		for enemy in enemies:
			del enemy
		del enemies
		del hero
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
		'''
		Overwrites the getMouse function in GraphWin
		
		Waits for mouse click. Aborts if gameRunning becomes False.

		Returns graphics.Point() with coordinates of mouse click, or
		None if gameRunning becomes False
		'''
		while self.gameRunning:
			mouseClick=self.checkMouse()
			if mouseClick==None:
				time.sleep(0.005)
			else:
				return mouseClick
		return None
		
	def setBackground(self,level):
		filename="images/background" + str(level) + ".gif"
		
		backgroundimg=Image.open(filename)
		
		rezimg=backgroundimg.resize((self.width, self.height), Image.ANTIALIAS)
		
		self.photoimg=ImageTk.PhotoImage(rezimg)
		
		self.create_image(0,0,anchor="nw",image=self.photoimg)
	

class Hero(graphics.Image):
	'''Our hero! Haz HP and shit!'''
	def __init__(self,window):
		self.window=window
		self.hp=100
		
		graphics.Image.__init__(self,Point(130,400),"images/hero/hero1.gif")
		self.draw(window)

	def isDead(self):
		'''Is he dead? Hell NO!'''
		return self.hp<=0
		
class Life(graphics.Image):
	def __init__(self,window,startLife,screenWidth):
		self.window = window
		positionX = screenWidth/2.4
		for x in range(startLife):
			graphics.Image.__init__(self,Point(positionX,30),"images/lifeIcon.gif")
			positionX = positionX + 30
			self.draw(window)
			
class CurrentScore(graphics.Text):
	def __init__(self,window,screenWidth):
		currentScore = 0
		self.window = window
		graphics.Text.__init__(self,Point(screenWidth/2,30),"Score: " + str(currentScore))
		self.setStyle("bold")
		self.setSize(18)
		self.draw(window)

def main():
	game=Game()
	while game.gameRunning:
		game.menu()

if __name__ == "__main__":
	main()
