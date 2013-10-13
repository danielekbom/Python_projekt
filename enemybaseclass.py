import graphics as g
from graphics import Image,Point,_root
import os
import itertools
import Tkinter as tk
from random import randint
import sys
import inspect

class Enemies(Image):
    def __init__(self,window):
        self.window=window
        g.GraphicsObject.__init__(self, [])
        imageDir=os.curdir + os.sep + "images" + os.sep + str(self.__class__).split('.')[1]
        images=[os.path.join(imageDir, f) for f in os.listdir(imageDir) if f.endswith(".gif")]
        images.sort()
        self.eliminatedImage=images.pop()
        self.imageId = Image.idCount
        Image.idCount = Image.idCount + len(images)
        self.photoImages=itertools.cycle([tk.PhotoImage(file=image, master=g._root) for image in images])
        self.img = next(self.photoImages)
        self.anchor = Point(window.getWidth(),randint(50,window.getHeight()-self.getHeight()))
        self.movementSpeed=10.0
        self.movementTick=0
        self.animationRatio=1.0
        self.animationTick=0
        self.eliminated=False
        self.hp=1
        self.draw(window)
    
    def walk(self,speedMultiplier=1.0):
        '''
        Gives one "tick" to the object. When enough ticks are
        reached, updates the animation and moves the object one
        step.
        
            Speed - A float multiplier from standard speed.
                    Defaults to 1.0
        '''
        if speedMultiplier==None: speedMultipier=1.0
        
        self.movementTick=self.movementTick+1
        self.animationTick=self.animationTick+1
        
        if self.movementTick>=100.0/(self.movementSpeed*speedMultiplier):
            self.move(-1,0)
            self.movementTick=0
        if self.animationTick>=100.0/(self.movementSpeed*speedMultiplier*self.animationRatio):
            self.undraw()
            self.img=next(self.photoImages)
            self.draw(self.window)
            self.animationTick=0

    def setAnimationRatio(self,animationRatio):
        '''The ratio of animations per movement'''
        self.animationRatio=animationRatio

    def getAnimationRatio(self):
        return self.animationRatio
    
    def setMovementSpeed(self,movementSpeed):
        '''movmentSpeed should be between 0 and 100'''
        if 0<movementSpeed<=100:
            self.speed=movementSpeed
        else:
            raise ValueError("speed should be between 0 and 100")

    def getMovementSpeed(self):
        return self.movementSpeed
    
    def kill(self,p,damage=1,radius=1):
        if hit(p):
            hp=hp-damage
            if hp<=0:
                self.eliminated=True
                self.img=self.eliminatedImage
                return True
        return False


class Boss(Enemies):
    '''Boss Base Class'''

def getEnemiesList():
    '''gives all enemies as a list of classes'''
    return [item[1] for item in inspect.getmembers(sys.modules["enemies"], lambda member: inspect.isclass(member) and member.__module__ == "enemies") if not issubclass(item[1],Boss)]

def getEnemiesUpToLevel(level):
    return [enemy for enemy in getEnemiesList() if enemy.level <= level]
