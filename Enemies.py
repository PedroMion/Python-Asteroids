import pygame, random
from pygame.locals import *
from Meteor import Meteor

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
MAX_SPEED = 15
MIN_SPEED = 5
TWO_METEORS_TIME = 3
ONE_METEOR_TIME = 1.5

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.meteors = []

    def update(self, time):
        for meteor in self.meteors:
            if meteor.collided:
                self.destroyMeteor(meteor)
                continue
            meteor.update()
        
        self.createMeteorBasedOnTime(time)

    def draw(self, surface):
        for meteor in self.meteors:
            meteor.draw(surface)
    
    def getRandomDirection(self):
        

        return

    def createMeteor(self):
        direction, position = self.getRandomDirection()
        degree = random.randint(0, 359)
        speed = random.randint(MIN_SPEED, MAX_SPEED)
        meteor = Meteor(direction, position, degree, speed)
        self.meteors.append(meteor)
    
    def destroyMeteor(self, meteor):
        self.meteors.remove(meteor)
        del meteor
    
    def createMeteorBasedOnTime(self, time):
        meteorQuantity = 0
        if time % TWO_METEORS_TIME == 0:
            meteorQuantity = 2
        elif time % ONE_METEOR_TIME == 0:
            meteorQuantity = 1
        for i in range(meteorQuantity):
            self.createMeteor()
