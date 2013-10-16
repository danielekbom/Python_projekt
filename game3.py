import graphics
from graphics import _root,GraphWin,Point,Text,Image
from PIL import Image as PIL_Image, ImageTk
import time
import random
import enemyclasses
try:
	import Tkinter as tk
except:
	import tkinter as tk

MARGIN_TOP_BOTTOM=72
MARGIN_SIDES=72

class Game(GraphWin):
	
	def __init__(self):
		
		#Runs in fullscreen
		
		#GraphWin.__init__
		_root.attributes('-fullscreen', True)
		master = tk.Toplevel(_root)
		master.attributes('-fullscreen', True)
		width = master.winfo_screenwidth() #-MARGIN_SIDES
		height = master.winfo_screenheight() #-MARGIN_TOP_BOTTOM
		title="AlabamaMAN! Shootin' turtels and beavers and snakes and frikkin' BEATURAKES! AlabamaMAN!"
		master.protocol("WM_DELETE_WINDOW", self.confirmClose)
		tk.Canvas.__init__(self, master, width = width, height = height, cursor="cross")
		self.master.bind("<Escape>", self.confirmClose)
		self.master.title(title)
		self.pack()
		#master.resizable(0,0)
		self.foreground = "black"
		self.items = []
		self.width = width
		self.height = height
		self.mouseX = None
		self.mouseY = None
		self.bind("<Button-1>", self._onClick)
		self.autoflush = True
		self._mouseCallback = None
		self.trans = None
		self.closed = False
		self.gameClosing = False
		self.gameRunning = True
		master.lift()
		if self.autoflush: _root.update()
	
	def confirmClose(self):
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
		self.closeGame()
	
	def play(self, level=1):
		'''
		Starts a new game.
		
		level - Start a game at level <level>
		
		Game loop idea taken from
		http://www.koonsolo.com/news/dewitters-gameloop/
		'''
		self.setBackground(level)
		self.hero=Hero(self)
		self.life=Life(self,3)
		enemyClassList=enemyclasses.getAllEnemies(maxLevel=level)
		self.enemies=[random.choice(enemyClassList)(self)]
		
		_root.update()
		
		self.after(0,self.gameloop)
		
	def closeGame(self):
		for enemy in self.enemies:
			del enemy
		del self.enemies
		del self.hero
		self.close()
		_root.quit()
		
	def gameloop(self):
		mouseClick = self.checkMouse()
		if mouseClick:
			pass
		
		for enemy in self.enemies:
			enemy.walk()
			self.tag_raise(enemy.imageId)
		
		
		_root.update()
		
		del mouseClick
		if self.gameRunning:
			if self.hero.isDead():
				self.gameOver()
			elif not self.gameClosing:
				self.after(10,self.gameloop)

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
		filename = "images/background" + str(level) + ".gif"
		
		self.bgImageObj = PIL_Image.open(filename)
		
		rezisedImageObj = self.bgImageObj.resize((self.getWidth(), self.getHeight()), PIL_Image.ANTIALIAS)
		
		self.bgImage = ImageTk.PhotoImage(rezisedImageObj)
		
		self.bgImageID = self.create_image(0,0,anchor="nw",image=self.bgImage)
		self.tag_lower(self.bgImageID)
	
	def removeBackground(self):
		self.delete(self.bgImageID)
		del self.bgImageID
		del self.bgImage
	

class Hero(graphics.Image):
	'''Our hero! Haz HP and shit!'''
	def __init__(self,window):
		self.window=window
		self.hp=100
		
		graphics.Image.__init__(self,Point(10,300),"images/hero/hero1.gif")
		self.draw(window)

	def isDead(self):
		'''Is he dead? Hell NO!'''
		return self.hp<=0
		
class Life(graphics.Image):
	def __init__(self,window,startLife):
		self.window = window
		positionX=100
		for x in range(startLife):
			graphics.Image.__init__(self,Point(positionX,30),"images/lifeIcon.gif")
			positionX = positionX + 30
			self.draw(window)

def main():
	game=Game()
	game.menu()
	_root.mainloop()

if __name__ == "__main__":
	main()
