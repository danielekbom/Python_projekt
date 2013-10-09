from graphics import *
import time
import random
import circle
import enemy1

def main():
   
	display = True
	winWidth = 1400
	winHeight = 700
	win = GraphWin("Hej",winWidth,winHeight)
	background = Image(Point(0,0),"images/grass.gif")
	background.draw(win)
	currentScore = 0
	displayScore = Text(Point(winWidth/2,25),"Score: " + str(currentScore))
	displayScore.setStyle("bold")
	displayScore.setSize(18)
	displayScore.draw(win)
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
					currentScore = currentScore + 1
					displayScore.setText("Score: " + str(currentScore))
				count = count + 1
		
		time.sleep(0.01)
main()
