from graphics import *
import time
import random
import enemy1
import enemy2
import enemy3
import enemy4
import enemy5
import enemy6
import enemy7
import boss1
import boss2

def main():
   
	display = True
	winWidth = 1400
	winHeight = 700
	win = GraphWin("Hej",winWidth,winHeight)
	background = Image(Point(700,350),"images/background2.gif")
	background.draw(win)
	hero = Image(Point(100,300),"images/hero/hero1.gif")
	hero.draw(win)
	heroShooting = False
	
	currentScore = 0
	displayScore = Text(Point(winWidth/2,18),"Score: " + str(currentScore))
	displayScore.setStyle("bold")
	displayScore.setSize(18)
	displayScore.draw(win)
	
	currentLife = 20
	displayLife = Text(Point(140,18),"Life: " + str(currentLife))
	displayLife.setStyle("bold")
	displayLife.setSize(18)
	displayLife.draw(win)
	
	enemies = []
	quitShooting = 0
	
	while display:
		quitShooting = quitShooting + 1
		if(heroShooting and quitShooting > 50):
			hero.undraw()
			hero = Image(Point(100,300),"images/hero/hero1.gif")
			hero.draw(win)
			heroShooting = False
			quitShooting = 0
		if(currentLife == 0):
			break
		randNumber = random.randint(1,100)
		if(randNumber == 50):
			enemyTypes = [enemy1.Enemy1,enemy2.Enemy2,enemy3.Enemy3,enemy4.Enemy4,boss1.Boss1,enemy5.Enemy5,enemy6.Enemy6,enemy7.Enemy7,boss2.Boss2]
			enemies.append(random.choice(enemyTypes)())
			lastCircle = len(enemies) - 1
			enemies[lastCircle].draw(win)
		if(len(enemies) > 0):
			count = 0
			for x in enemies:
				if(enemies[count].eliminated == False):
					enemies[count].move()
				count = count + 1
		clicked = win.checkMouse()
		if clicked:
			hero.undraw()
			hero = Image(Point(100,300),"images/hero/hero1_shoot.gif")
			hero.draw(win)
			heroShooting = True
			click_x = clicked.getX()
			click_y = clicked.getY()
			count = 0
			for x in enemies:
				center_x = enemies[count].getCenter().getX()
				center_y = enemies[count].getCenter().getY()
				if((click_x > center_x-10 and click_x < center_x+10) and (click_y > center_y-15 and click_y < center_y+15) and (enemies[count].eliminated == False)):
					enemies[count].changeColor(win)
					currentScore = currentScore + 1
					displayScore.setText("Score: " + str(currentScore))
				count = count + 1
		count = 0
		for x in enemies:
			center_x = enemies[count].getCenter().getX()
			if(center_x < -50):
				del(enemies[count])
				currentLife = currentLife - 10
				displayLife.setText("Life: " + str(currentLife))
			count = count + 1
		
		time.sleep(0.01)
		
	gameOverText = Text(Point(500,200),"Game Over")
	gameOverText.setStyle("bold")
	gameOverText.setSize(36)
	gameOverText.draw(win)
	wait = win.getMouse()
main()
