from graphics import *
import time
import random
import circle
import enemy1

def main():
   
	display = True
	win = GraphWin("Hej",1400,700)
	background = Image(Point(0,0),"images/grass.gif")
	background.draw(win)
	enemies = []
	
	while display:
		randNumber = random.randint(1,100)
		if(randNumber == 50):
			enemyTypes = [circle.Circle1(),enemy1.Enemy1()]
			enemies.append(enemyTypes[random.randint(0,len(enemyTypes) - 1)])
			lastCircle = len(enemies) - 1
			enemies[lastCircle].draw(win)
		if(len(enemies) > 0):
			count = 0
			for x in enemies:
				enemies[count].move()
				count = count + 1
		clicked = win.checkMouse()
		if clicked:
			click_x = clicked.getX()
			click_y = clicked.getY()
			count = 0
			for x in enemies:
				center_x = enemies[count].getCenter().getX()
				center_y = enemies[count].getCenter().getY()
				if((click_x > center_x-10 and click_x < center_x+10) and (click_y > center_y-10 and click_y < center_y+10)):
					enemies[count].changeColor(win)
				count = count + 1
		
		time.sleep(0.01)
main()
