import pygame, random
from pygame.locals import *
from Meteor import Meteor

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
MAX_SPEED = 10
MIN_SPEED = 5
TWO_METEORS_TIME = 5
ONE_METEOR_TIME = 2.5
DEFAULT_DIRECTION = pygame.Vector2(0, -1)
DIRECTIONS = {
    "right": [1, 0],
    "left": [-1, 0],
    "up": [0, -1],
    "down": [0, 1],
}
CORNERS = {
    1: [0, 0],
    2: [SCREEN_WIDTH, SCREEN_HEIGHT]
}
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
        position, border, index = self.getPosition()
        direction = self.getDirection(border, index)

        return direction, position

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
    
    def getPosition(self):
        index = random.randint(1, 2)
        direction = []
        direction.append(CORNERS.get(index)[0])
        direction.append(CORNERS.get(index)[1])

        newValue = random.randint(0, 1)
        if newValue == 0:
            direction[newValue] = random.randrange(0.1 * SCREEN_WIDTH, 0.9 * SCREEN_WIDTH)
        elif newValue == 1:
            direction[newValue] = random.randrange(0.1 * SCREEN_HEIGHT, 0.9 * SCREEN_HEIGHT)

        return direction, index, newValue
    
    def getDirection(self, border, index):
        direction = DEFAULT_DIRECTION
        if border == 1 and index == 0:
            direction = DEFAULT_DIRECTION.rotate(-random.randrange(135, 225))
        elif border == 1 and index == 1:
            direction = DEFAULT_DIRECTION.rotate(random.randrange(45, 135))
        elif border == 2 and index == 0:
            direction = DEFAULT_DIRECTION.rotate(random.randrange(-45, 45))
        elif border == 2 and index == 1:
            direction = DEFAULT_DIRECTION.rotate(random.randrange(225, 270))
        
        return direction

