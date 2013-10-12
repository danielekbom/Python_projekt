import graphics as g
from graphics import *
import time
import random
import enemies
import Tkinter as tk


class Game(GraphWin):
	
	def __init__(self):
		width = g._root.winfo_screenwidth()-72
		height = g._root.winfo_screenheight()-72
		#GraphWin.__init__
		title="AlabamaMAN! Shootin' turtels and beavers and snakes and frikkin' BEATURAKES! AlabamaMAN!"
		master = tk.Toplevel(g._root)
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
		master.lift()
		if self.autoflush: _root.update()
	
	def close(self):
		closeText = Text(Point(self.width/2,self.height/2),"Close?")
		closeText.setStyle("bold")
		closeText.setSize(36)
		closeText.draw(self)
		wait = self.getMouse()
		del closeText
		GraphWin.close(self)
		
	
	def play(self):
		background = Image(Point(self.width/2,self.height/2),"images/background1.gif")
		background.draw(self)
		enemy=enemies.enemy1(self)
		self.getMouse()
		while self.checkMouse()==None:
			enemy.walk()
			time.sleep(0.01)
		self.getMouse()
		self.gameOver()
		del background
		
	def highscore(self):
		pass
	
	def gameOver(self):
		gameOverText = Text(Point(self.width/2,self.height/2),"Game Over")
		gameOverText.setStyle("bold")
		gameOverText.setSize(36)
		gameOverText.draw(self)
		wait = self.getMouse()
		
		del gameOverText
		
	def menu(self):
		if False:
			return False
		self.endGame=False
		return True

def main():
	game=Game()
	while game.menu():
		game.play()
		game.highscore()

if __name__ == "__main__":
	main()
