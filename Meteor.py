import pygame, random
from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

class Meteor(pygame.sprite.Sprite):
    def __init__(self, direction, currentPosition, degree, speed, imageURL):
        super().__init__()
        self.degree = degree
        self.image = pygame.image.load(imageURL)
        self.rect = self.image.get_rect()
        self.rect.center = currentPosition
        self.direction = direction
        self.speed = speed
        self.ageInPosition = 0
        self.collided = False

    def update(self):
        self.moveForward()
        self.checkBorderHit()
        
        self.ageInPosition += 1

    def moveForward(self):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)

    def draw(self, surface):
        surface.blit(pygame.transform.rotate(self.image, self.degree), self.rect)

    def checkBorderHit(self):
        if self.ageInPosition < 24:
            return
        
        if self.rect.left <= 0:
            self.rect.left = SCREEN_WIDTH
            self.ageInPosition = 0
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = 0
            self.ageInPosition = 0
        elif self.rect.top <= 0:
            self.rect.top = SCREEN_HEIGHT
            self.ageInPosition = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.ageInPosition = 0

    def destroy(self):
        self.collided = True


class BigMeteor(Meteor):
    def __init__(self, direction, currentPosition, degree, speed):
        Meteor.__init__(self, direction, currentPosition, degree, speed, "./images/BigMeteor.png")
        self.type = "Big"

class SmallMeteor(Meteor):
    def __init__(self, direction, currentPosition, degree, speed):
        Meteor.__init__(self, direction, currentPosition, degree, speed, "./images/SmallMeteor.png")
        self.type = "Small"